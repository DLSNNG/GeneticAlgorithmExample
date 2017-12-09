import numpy as np
from Organism import Organism

def defaultFitnessFunc(organism, data=None):
    return np.sum(organism.genes)

class Population:
    
    organisms = []
    matingPool = 100
    mutationRate = 0
    fitnessFunc = defaultFitnessFunc
    data = None
    logger = None
    
    def __init__(self, numGenes = 5, size=1000, matingPool=100, 
                 mutationRate=0, fitnessFunc=defaultFitnessFunc, data=None, logger=None):
        
        del self.organisms[:]
        self.matingPool = matingPool
        self.mutationRate = mutationRate
        self.fitnessFunc = fitnessFunc
        self.data = data
        self.logger = logger
        self.logger.info("Initiating Population")
        print "Data received %s" % self.data
        
        for i in range(0,size):
            organism = Organism(numGenes=numGenes, logger=logger)
            organism.determineFitness(fitnessFunc, data)
            self.organisms.append(organism)
            
    def churn(self, generations=100):
        for i in range(0, generations):
            self.advanceGeneration()
        
    def advanceGeneration(self):
        self.orderByFitness()
        self.cull()
        self.repopulate()
        self.logger.info("Advancing generation")
        
    def getMostFit(self):
        self.orderByFitness()
        mostFit = self.organisms[0]
        return mostFit
        
    def orderByFitness(self, reverse=False):
        self.organisms = sorted(self.organisms, key=self.getFitness, reverse=reverse)
        
    def cull(self):
        #kill off the bottom of the pool (least fit)
        organisms = self.organisms
        self.logger.info("Mating Pool: %s", self.matingPool)
        for i in range(0, self.matingPool):
            organisms.pop()
        self.organisms = organisms
        self.logger.info("Culled Population: %s", self.organisms)
            
    def repopulate(self):
        organisms = self.organisms
        matingPool = self.matingPool
        mutationRate = self.mutationRate
        fitnessFunc = self.fitnessFunc
        data = self.data
        
        for i in range(0, matingPool):
            mate1 = organisms[i]
            mate2Index = np.random.randint(i, len(organisms))
            mate2 = organisms[mate2Index]
            child = mate1.mateWith(mate2, mutationRate, fitnessFunc, data)
            organisms.append(child)
            
        self.organisms = organisms
        self.logger.info("Repopulated Population: %s", self.organisms)
        
    def getFitness(self, organism):
        return organism.fitness
            
    def __str__(self):
        return str(self.organisms)
    
    def __repr__(self):
        return str(self.organisms)
        
            
    
            