import random

class Cromossomo:
    def __init__(self, binary_value: str) -> None:
        self.binary_value = binary_value
        self.decimal_value = int(binary_value, 2)
    
    def get_fitness(self) -> float:
        return (self.decimal_value * 15 ) - (self.decimal_value **2) 

    def __str__(self) -> str:
        return f'{self.binary_value}'

def generate_population(population_size: int, cromossomo_size: int) -> list:
    return [Cromossomo(''.join([str(random.randint(0, 1)) for _ in range(cromossomo_size)])) for _ in range(population_size)]


def main():
    population = generate_population(2, 4)
    for cromossomo in population:
        print(cromossomo)
        print(cromossomo.get_fitness())
        print('---')
    
    

if __name__ == '__main__':
    main()