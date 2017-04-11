# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 14:39:22 2016

@author: Zach
"""
# import whats needed to plot the data
import pylab
import random 

# ask user for the relative fitness and genotype frequency of the recessive genotype
recessive=float(input("recessive gene frequency: "))
recessive_fitness=float(input("recessive relative fitness: "))
print()

# ask user for the relative fitness and genotype frequency of the dominant genotype
dominant=float(input("dominant gene frequency: "))
dominant_fitness=float(input("dominant relative fitness: "))

# create an empty list to store all the gene frequencies needed to graph
list_of_gene_freq=[]
yes=[]

#random_variation=0

# do the genotype frequency calculation for 100 generations
# we can think of i as a generation
for i in range(100):
    
    #wbar represents the sum of the frequencies and fitnesses multiplied
    #wbar will be greater than 1, but frequencies must add up to 1
    # we will later divide the geneotype frequencies by this number to obtain the new gene frequencies
    w_bar = (recessive*recessive_fitness)+(dominant*dominant_fitness)
    
    #random_variation=random.uniform(0.99,1.01)
    
    
    #multiply genotype frequencies by their fitness
    dominant*=dominant_fitness #*random_variation
    recessive*=recessive_fitness #*random_variation
    
    #divide genotype frequencies by wbar
    dominant/=w_bar
    recessive/=w_bar
    
    #add recessive frequency to a list o we can graph
    #its easy to just graph the recessive frequency, I intend to graph the dominant frequency too
    list_of_gene_freq.append(recessive)
    
    if recessive>0.5:
        yes.append(i)
        
   # print("{:.3f} : {:.3f}".format(dominant, recessive))

#plot the gene frequencies
pylab.plot(list_of_gene_freq)
print("dominant frequency makes up {:.2f} % of the population".format(dominant*100))