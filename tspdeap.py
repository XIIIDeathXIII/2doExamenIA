
import array
import random
import json

import numpy
from deap import algorithms
from deap import base
from deap import creator
from deap import tools



with open("gr17.json", "r") as tsp_data:
    tsp = json.load(tsp_data)

distance_map = tsp["DistanceMatrix"]
IND_SIZE = tsp["TourSize"]

def generar_indices(IND_SIZE):
    IND_SIZE=IND_SIZE-1
    array = [0]
    for _ in range(IND_SIZE):
        num = random.randint(1, IND_SIZE)
        while num in array:
            num = random.randint(1, IND_SIZE)
        array.append(num)
    return array


creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", array.array, typecode='i', fitness=creator.FitnessMin)
toolbox = base.Toolbox()
toolbox.register("indices", generar_indices, IND_SIZE)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalTSP(individual):
    distance = distance_map[individual[-1]][individual[0]]
    for gene1, gene2 in zip(individual[0:-1], individual[1:]):
        distance += distance_map[gene1][gene2]
    return distance,

toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evalTSP)

def main():
    random.seed(150)

    pop = toolbox.population(n=16)
    
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)
    
    algorithms.eaSimple(pop, toolbox, 0.7, 0.2, 40, stats=stats, 
                        halloffame=hof)
    print(pop[1], "eval", evalTSP(pop[1]))
    print((hof))
    return pop, stats, hof

if __name__ == "__main__":
    main()
    
"""minim=numpy.min
      for i in range(16):
          if evalTSP(pop[i])!=minim:
             print("a")
             print(pop[i])"""  