from copy import copy
import numpy as np
import itertools
from Estoque import *


class Chromossome:
    SIZE = 30
    ESTOQUE = None

    def __init__(self, chromossome: list = None, estoque: Estoque = None, maxId=2) -> None:
        self.ESTOQUE = estoque
        if chromossome == None:
            self.shape = np.random.randint(0, maxId + 1, (self.SIZE,))
            self.adaptation = 0
            self.fitness()
        elif len(chromossome) == self.SIZE:
            self.shape = np.array(chromossome)
            self.adaptation = 0
            self.fitness()
        else:
            # print(f'Chromossome\'s lenght is not compatible!')
            exit()

    def __str__(self) -> str:
        chromossome_string = '['
        for i in self.shape:
            chromossome_string += str(i) + ' '
        chromossome_string += ']'

        return chromossome_string.replace(' ]', ']') + f' -> {self.adaptation}'

    def fitness(self) -> None:
        self.adaptation = 0
        volume_total = 0
        preco_total = 0

        for i in range(self.SIZE):
            result, produto = self.ESTOQUE.getProduto(self.shape[i])
            if result:
                volume_total += produto.volume
                preco_total += produto.preco

        # print(f'volume = {volume_total}, preco = {preco_total}')
        self.adaptation = volume_total - preco_total


class Population:

    SIZE = 10
    OFFSET = 5            # n | n < SIZE
    CROSSOVER_RATE = 0.4  # 0 - 1
    MUTATION_RATE = 0.7   # 0 - 1
    INVERTION_RATE = 0.7  # 0 - 1
    MAX_AGES = 5000

    def __init__(self, estoque: Estoque, capacidade=200, dinheiro_max=1000.0) -> None:
        self.estoque = estoque
        self.capacidade = capacidade
        self.dinheiro_max = dinheiro_max
        self.chromossomes = self.generate()
        self.offspring = []
        self.age = 0

    def __str__(self) -> str:
        population_string = f'--- Population ----------------------\n'
        count = 1
        for chromossome in self.chromossomes:
            population_string += f'{count} - ' + str(chromossome) + '\n'
            count += 1

        return population_string

    def generate(self) -> list:
        chromossomes = []
        for _ in range(self.SIZE):
            chromossomes.append(Chromossome(
                estoque=self.estoque, maxId=self.estoque.totalProdutos))

        return chromossomes

    def sort(self, order='desc') -> None:
        i = 0
        for i in range(len(self.chromossomes) - 1):
            for j in range(i+1, len(self.chromossomes)):
                if order == 'desc':
                    if self.chromossomes[j].adaptation > self.chromossomes[i].adaptation:
                        self.swap(i, j)
                elif order == 'asc':
                    if self.chromossomes[j].adaptation < self.chromossomes[i].adaptation:
                        self.swap(i, j)

    def swap(self, i: int, j: int) -> None:
        aux = self.chromossomes[i]
        self.chromossomes[i] = self.chromossomes[j]
        self.chromossomes[j] = aux

    def crossover(self) -> None:
        for i in range(self.OFFSET - 1):
            for j in range(i + 1, self.OFFSET):
                if np.random.random() <= self.CROSSOVER_RATE:
                    # print('Entrou | {} <-> {}'.format(i+1, j+1))
                    cut = np.random.randint(0, Chromossome.SIZE)

                    desc1 = list(itertools.chain(
                        self.chromossomes[i].shape[:cut], self.chromossomes[j].shape[cut:]))
                    desc2 = list(itertools.chain(
                        self.chromossomes[j].shape[:cut], self.chromossomes[i].shape[cut:]))

                    chromossome1 = Chromossome(
                        desc1, self.estoque, self.estoque.totalProdutos)
                    chromossome2 = Chromossome(
                        desc2, self.estoque, self.estoque.totalProdutos)

                    # print(chromossome1)
                    # print(chromossome2)

                    if not self.isMonster(chromossome1):
                        self.offspring.append(chromossome1)

                    if not self.isMonster(chromossome2):
                        self.offspring.append(chromossome2)

    def mutation(self) -> None:
        for i in range(self.OFFSET):
            if np.random.random() <= self.MUTATION_RATE:
                # print(f'mutation on {i+1}o chromosome!')
                descendant = self.chromossomes[i].shape.copy()
                for j in range(Chromossome.SIZE):
                    if np.random.randint(2) == 1:
                        # print(f'mutation in gen[{j}]')
                        descendant[j] = np.random.randint(
                            0, self.estoque.totalProdutos + 1)

                chromossome = Chromossome(
                    list(descendant), self.estoque, self.estoque.totalProdutos)

                if not self.isMonster(chromossome):
                    self.offspring.append(chromossome)

    def inversion(self) -> None:
        for n in range(self.OFFSET):
            if np.random.random() <= self.INVERTION_RATE:
                # print(self.chromossomes[n])
                # print(f'Inverteu no {n+1}o cromossomo!')
                descendant = self.chromossomes[n].shape.copy()

                p1 = np.random.randint(0, Chromossome.SIZE - 1)
                p2 = np.random.randint(p1 + 1, Chromossome.SIZE)

                # print(f'pivos: {p1} e {p2}')
                descendant = list(itertools.chain(descendant[:p1], reversed(
                    descendant[p1:p2+1]), descendant[p2+1:]))

                chromossome = Chromossome(
                    descendant, self.estoque, self.estoque.totalProdutos)

                # print(f'descendant -> ' + str(chromossome))

                if not self.isMonster(chromossome):
                    self.offspring.append(chromossome)

    def showOffspring(self) -> None:
        count = 1
        # print(f'--- Offspring ----------------------')
        for chromossome in self.offspring:
            # print(f'{count} - ' + str(chromossome))
            count += 1

    def isMonster(self, chromossome: Chromossome, mode='categoria'):
        volume_total = 0
        preco_total = 0

        for i in range(Chromossome.SIZE):
            result, produto = self.estoque.getProduto(chromossome.shape[i])
            if result:
                volume_total += produto.volume
                preco_total += produto.preco

        if volume_total > self.capacidade or preco_total > self.dinheiro_max:
            return True
        return False

    def isEmpty(self, ChromossomeList) -> bool:
        return len(ChromossomeList) == 0

    def merge(self) -> None:
        # print(f'--- Merging ...')
        while not self.isEmpty(self.offspring):
            self.chromossomes.append(self.offspring.pop())

    def selection(self, selectionMode: str) -> None:
        if selectionMode == 'elitism':
            self.elitism()
        else:
            # print(f'Invalid selection mode!')
            exit()

    def elitism(self) -> None:
        self.merge()
        self.sort()
        while len(self.chromossomes) > self.SIZE:
            self.chromossomes.pop()

    def stopCondition(self):
        return self.age > self.MAX_AGES

    def incrementAge(self):
        self.age += 1

    def printSolution(self, chromossome: Chromossome):
        pass

    def run(self, selectionMode: str = 'elitism') -> None:
        while not self.stopCondition():
            self.sort()
            self.crossover()
            self.mutation()
            self.inversion()
            self.selection(selectionMode)
            self.incrementAge()
            times = (self.age / self.MAX_AGES) * 100
            print(f'\rAGE: ' + "{:>7}".format(self.age) + ' [' + f'{Color.SUCCESS}█'*int(
                times) + ' '*int(100 - times) + f'{Color.RESET}]', end='')

        print(f'\nProblem\'s solution: ' + str(self.chromossomes[0]))
