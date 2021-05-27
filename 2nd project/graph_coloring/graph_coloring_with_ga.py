import random

# valid genes/ characters for chromosomes/ strings
GENES = '01'

# targer chromosome/ string 
# TARGET = '10000010000000101010100010001000001000000010000010000000100000100000001000001'
TARGET = '10000010000000101010100010001000001'


def create_gene():
    '''
    Create a random gene from the string of valid genes.

    Returns: A random valid gene.
    '''
    return random.choice(GENES)
    

def create_chromosome():
    '''
    Create a random, valid, chromosome the size 
    of the target chromosome using createGene().

    Returns: A random valid chromosome.
    '''
    chromosome = ''
    for _ in range(len(TARGET)):
        chromosome += create_gene()
    return chromosome


def mate(mating_pool):
    '''
    Perform mating and produce new offspring using single-point crossover.
    
    Returns: A new generation of chromosomes
    '''
    new_generation = []
    for i in range(len(mating_pool)):
        # create a random point where the chromosomes will be split
        crossover_point = random.randint(0, len(mating_pool[i])-1)
        
        # inside a try-except because when then loop reaches 
        # the last individual the next one will be out of bounds, so 
        # we handle the error and produce a random position for the 
        # second parent in order for the last individual to mate
        try:
            # split each chromosome at the crossover point and 
            # concatenate them in order to produce 2 offsprings
            new_generation.append(mating_pool[i][:crossover_point] + mating_pool[i+1][crossover_point:])
            new_generation.append(mating_pool[i+1][:crossover_point] + mating_pool[i][crossover_point:])
        except IndexError:
            randPosition = random.randint(0, len(mating_pool)-1)
            new_generation.append(mating_pool[i][:crossover_point] + mating_pool[randPosition][crossover_point:])
            new_generation.append(mating_pool[randPosition][:crossover_point] + mating_pool[i][crossover_point:])
    return new_generation


def calculate_fitness(chromosome):
    '''
    Calculating the fitness of the given chromosome by comparing 
    each gene to the corresponding gene in the target chromosome.
    The lower the fitness value the closer the chromosome is 
    to matching the target chromosome.

    Returns: The fitness score of the given chromosome.
    '''
    fitness = 0
    for test_gene, target_gene in zip(chromosome, TARGET):
        if test_gene != target_gene:
            fitness += 1
    return fitness


def select_parents(population, population_fitness_score):
    '''
    Parent selection process using the Roulette Wheel method.

    Returns: A list with the parents to mate
    '''
    mating_pool = []

    # calculate the sum of fitness values for all of the chromosomes
    fitness_sum = 0
    for score in population_fitness_score:
        fitness_sum += score

    # generate a random number between (0, fitness_sum)
    # in order to spin the wheel and select a fitness value
    rand = random.randint(0, fitness_sum)

    # recalculate a partial sum of fitness values, if the
    # partial sum is >= of the random number, append the 
    # chromosome at that position to the mating pool
    partialSum = 0
    for index, score in enumerate(population_fitness_score):
        partialSum += score
        if partialSum >= rand:
            partialSum = 0
            mating_pool.append(population[index])   

    return mating_pool

#! Επιλέξτε αν θέλετε να κάνετε και μερική ανανέωση πληθυσμού σε κάποιο ποσοστό 
#! π.χ. 50% και μετάλλαξη ενός ψηφίου π.χ. στο 10% του πληθυσμού.
def main():
    '''
    Handles the flow of the algorithm.
    '''
    # initialize the population of chromosomes and their corresponding fitness value.
    # These lists are parallel, thus each individual inside population[] has 
    # its fitness score at the same index but inside populationFitnessScore[]
    population = []
    population_fitness_score = []

    # initialize the generation count
    generation = 1

    # number of individuals in initial generation
    POPULATION_SIZE = 100

    for _ in range(POPULATION_SIZE):
        # creating an initial population, calculating the fitness scores
        # and populating the 2 lists.
        init_population = create_chromosome() 
        population.append(init_population)
        population_fitness_score.append(calculate_fitness(init_population))

    # create new generations until one individual matches the target chromosome
    while True:
        # create a mating pool with the parents to mate
        mating_pool = select_parents(population, population_fitness_score)
        
        # checking if the parents inside the pool are adequate in order to mate
        while len(mating_pool) < 100:
            mating_pool = select_parents(population, population_fitness_score)

        # perform mating process and produce the next generation
        next_generation = mate(mating_pool)

        # check every element inside the new generation if it matches the target chromosome
        if TARGET in next_generation:
            print('\nFOUND')
            break
        
        print('\nGeneration: ', generation)

        # advance to the next generation
        generation += 1

        # make the next generation the current population 
        # and recalculate the fitness score for the new population
        population = next_generation
        population_fitness_score = []
        for chromosome in population:
            population_fitness_score.append(calculate_fitness(chromosome))
        

if __name__ == '__main__':
    main()