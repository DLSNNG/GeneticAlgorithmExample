import numpy as np

class Organism:
    
    genes = None
    fitness = None
    logger = None
    
    def __init__(self, numGenes=None, genes=None, logger=None):
        
        if(genes):
            self.genes = genes
        else:
            self.genes = np.random.uniform(0,1,numGenes)
            
        self.logger = logger
        self.logger.info("setting genes: \n %s", self.genes)
    
    def pickRandomGene(self):
        self.logger.debug("calling pickRandomGene")
        numGenes = len(self.genes)
        index = np.random.randint(0,numGenes)
        self.logger.info("num genes = %s", numGenes)
        self.logger.info("index = %s", index)
        return index
    
    def pickRandomDirection(self):
        self.logger.info("calling pickRandomDirection")
        direction = 2*np.random.randint(0,2) - 1
        self.logger.info("picked direction = %s", direction)
        return direction
    
    def createGene(self, parentGene, mutationRate=0):
        self.logger.info("calling createGene")
        chance = np.random.randint(0,100)
        self.logger.info("chance = %s", chance)
        if mutationRate > chance:
            self.logger.debug("mutating gene")
            newGene = np.random.uniform(0,1)
        else:
            newGene = parentGene
        self.logger.info("new gene = %s", newGene)
        return newGene
    
    def determineFitness(self, fitnessFunc, data):
        self.fitness = fitnessFunc(self, data)
        
    def mateWith(self, partner, mutationRate=0, fitnessFunc=None, data=None):
        self.logger.info("calling mateWith")
        crossingpoint = self.pickRandomGene()
        direction = self.pickRandomDirection()
        genes1 = self.genes
        genes2 = partner.genes
        childGenes = []
        for i in range(0, len(genes1)):
            if(direction*i <= direction*crossingpoint):
                parentGene = genes1[i]
                newGene = self.createGene(parentGene, mutationRate)
                self.logger.info("inserting value = %s", newGene)
                childGenes.append(newGene)
            else:
                parentGene = genes2[i]
                newGene = self.createGene(parentGene, mutationRate)
                self.logger.info("inserting value = %s", newGene)
                childGenes.append(newGene)
        child = Organism(5, childGenes, logger=self.logger)
        if fitnessFunc:
            child.determineFitness(fitnessFunc, data)
        return child
    
    def __str__(self):
        return str(self.genes)
    
    def __repr__(self):
        return str(self.fitness)
        
        