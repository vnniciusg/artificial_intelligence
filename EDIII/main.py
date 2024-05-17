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


def selection_by_roulette(population: List[Cromossomo],  fitness: List[float]) -> Cromossomo:
    max_fitness = sum(fitness)
    pick = random.uniform(0, max_fitness)
    current = 0
    for i, cromossomo in enumerate(population):
        current += fitness[i]
        if current > pick:
            return cromossomo


def crossover(parent_1: Cromossomo, parent_2: Cromossomo) -> Cromossomo:
    crossover_point = random.randint(0, len(parent_1.binary_value) - 1)
    child_binary = parent_1.binary_value[:crossover_point] + parent_2.binary_value[crossover_point:]
    return Cromossomo(child_binary)

def mutation(individual: Cromossomo, mutation_strength: float = 0.1) -> Cromossomo:
    mutated_binary = ''.join(
        [gene if random.random() > mutation_strength else str(1 - int(gene)) for gene in individual.binary_value]
    )
    return Cromossomo(mutated_binary)



def main():
    POPULATION_SIZE = 100
    CROMOSSOMO_SIZE = 4
    MUTATION_STRENGTH = 0.01
    GENERATIONS = 100
    PERCENTAGE_REPRODUCTION = 0.7

    population = generate_population(POPULATION_SIZE, CROMOSSOMO_SIZE)
    mean_fitness_by_generation = []
    best_fitness_by_generation = []

    for _ in range(GENERATIONS):

        fitness = [cromossomo.get_fitness() for cromossomo in population]
        new_population = []
        best_fitness_by_generation.append(max(fitness))
        mean_fitness_by_generation.append(mean_fitness(population))

        while len(new_population) < POPULATION_SIZE * PERCENTAGE_REPRODUCTION:
            parent1 = selection_by_roulette(population, fitness)
            parent2 = selection_by_roulette(population, fitness)

            son1 = mutation(crossover(parent1, parent2), MUTATION_STRENGTH)
            son2 = mutation(crossover(parent1, parent2), MUTATION_STRENGTH)

            new_population.append(son1)

            if len(new_population) < POPULATION_SIZE * PERCENTAGE_REPRODUCTION:
                new_population.append(son2)

            

        while len(new_population) < POPULATION_SIZE:
            new_population.append(selection_by_roulette(population, fitness))
        
        population = new_population[:POPULATION_SIZE]
    
    plt.plot(mean_fitness_by_generation, label='Médio')
    plt.plot(best_fitness_by_generation, label='Melhor', linestyle='--')

    plt.grid(True, zorder=0)
    plt.title("Evolução do fitness médio ao longo das gerações")
    plt.xlabel("Geração")
    plt.ylabel("Fitness")
    plt.legend()  
    plt.show()


if __name__ == '__main__':
    main()

    