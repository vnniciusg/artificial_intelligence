import random
from typing import List

import matplotlib.pyplot as plt

class Cromossomo:
    def __init__(self, binary_value: str) -> None:
        self.binary_value = binary_value
        self.decimal_value = int(binary_value, 2)
    
    def get_fitness(self) -> float:
        return (self.decimal_value * 15 ) - (self.decimal_value **2) 

    def __str__(self) -> str:
        return f'{self.binary_value}'

def generate_population(population_size: int, cromossomo_size: int) -> List[Cromossomo]:
    return [Cromossomo(''.join([str(random.randint(0, 1)) for _ in range(cromossomo_size)])) for _ in range(population_size)]


def mean_fitness(population: List[Cromossomo]) -> float:
    return sum([cromossomo.get_fitness() for cromossomo in population]) / len(population)


def selection(population: List[Cromossomo]) -> Cromossomo:
    total_fitness = sum([cromossomo.get_fitness() for cromossomo in population])
    r = random.uniform(0, total_fitness)
    accumulator = 0
    for individual in population:
        accumulator += individual.get_fitness()
        if accumulator >= r:
            return individual

def crossover(parent_1: Cromossomo, parent_2: Cromossomo) -> Cromossomo:
    crossover_point = random.randint(0, len(parent_1.binary_value) - 1)
    child_binary = parent_1.binary_value[:crossover_point] + parent_2.binary_value[crossover_point:]
    return Cromossomo(child_binary)

def mutation(individual: Cromossomo, mutation_strength: float = 0.1) -> Cromossomo:
    binary_value = list(individual.binary_value)
    for i in range(len(binary_value)):
        if random.random() < mutation_strength:
            binary_value[i] = '1' if binary_value[i] == '0' else '0'
    return Cromossomo(''.join(binary_value))

def main():
    POPULATION_SIZE = 10
    CROMOSSOMO_SIZE = 4
    MUTATION_STRENGTH = 0.01
    GENERATIONS = 100
    ELITISM = True
    ELITISM_SIZE = 3

    population = generate_population(POPULATION_SIZE, CROMOSSOMO_SIZE)
    best_fitnesses = []
    history = []

    for generation in range(GENERATIONS):
        new_population = []
        print(f'Generation {generation} Mean Fitness: {mean_fitness(population)}')
        for _ in range(POPULATION_SIZE - ELITISM_SIZE if ELITISM else POPULATION_SIZE):
            parent_1 = selection(population)
            parent_2 = selection(population)
            child = crossover(parent_1, parent_2)
            child = mutation(child, MUTATION_STRENGTH)
            new_population.append(child)

            print(f'Parent 1: {parent_1} Parent 2: {parent_2} Child: {child}')
        
       
            if ELITISM:
                population.sort(key=lambda x: x.get_fitness(), reverse=True)
                new_population.extend(population[:ELITISM_SIZE])
        
        history.append(mean_fitness(population))

        print("============================================")
        
        population = new_population
        best_fitnesses.append(max([cromossomo.get_fitness() for cromossomo in population]))
    
    plt.plot(range(len(history)), history)
    plt.grid(True, zorder=0)
    plt.title("Evolução do fitness médio ao longo das gerações")
    plt.xlabel("Geração")
    plt.ylabel("Fitness medio")
    plt.show()


if __name__ == '__main__':
    main()

    