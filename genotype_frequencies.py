# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 14:39:22 2016

@author: Zach
"""
# import whats needed to plot the data
import pylab
import random
import matplotlib.pyplot as plt

# read input file with genotype relative fitness and allele frequencies
inputFile = open("SelctionAgainst_HomoRec.txt","r")
inputs =[]
for line in inputFile:
    arg = float(line)
    inputs.append(arg)
# set variables for allele freqeuncy
DominantAllelePercent = float(inputs[0])
RecessiveAllelePercent = float(inputs[1])
# record the relative fitness of each genotype
HomoRecFitness = float(inputs[2])
HomoDomFitness = float(inputs[3])
HeteroFitness = float(inputs[4])



# create an empty list to store all the gene frequencies needed to graph
RecessiveAlleleFreqs=[]
DominantAlleleFreqs=[]
HomoDomFreqs=[]
HomoRecFreqs=[]
HeteroFreqs=[]


#initialize Genotypic frequencies
HomoRecFreq = RecessiveAllelePercent**2
HomoDomFreq = DominantAllelePercent**2
HeteroFreq= 2*RecessiveAllelePercent*DominantAllelePercent
# do the genotype frequency calculation for 100 generations
# we can think of i as a generation
for i in range(100):
    '''
    if i < 3:
        print("Generation " + str(i) + ": ")
        print("Homozygous Dominant frequency: " + str(HomoDomFreq))
        print("Homozygous Reccessive frequency: " + str(HomoRecFreq))
        print("Heterozygous frequency: " + str(HeteroFreq))
        print("Dominant Allele frequency: " + str(DominantAllelePercent))
        print("Recessive Allele frequency: " + str(RecessiveAllelePercent))
        print()
    '''
    #get genotype frequency without fitness applied yet
    HomoRecFreq = RecessiveAllelePercent**2
    HomoDomFreq = DominantAllelePercent**2
    HeteroFreq= 2*RecessiveAllelePercent*DominantAllelePercent

    #record the genotype frequencies for this generation
    HomoRecFreqs.append(HomoRecFreq) #HomoRecFreq)
    HomoDomFreqs.append(HomoDomFreq)
    HeteroFreqs.append(HeteroFreq)
    #record the allelic frequencies
    RecessiveAlleleFreqs.append(RecessiveAllelePercent)
    DominantAlleleFreqs.append(DominantAllelePercent)


    #################################################################
    #calculate next generation genotypes and allelic frequencies
    #################################################################

    #get temporary genotypic freqs that apply the fitness
    tempHomoRecFreq = HomoRecFreq*HomoRecFitness
    tempHomoDomFreq= HomoDomFreq*HomoDomFitness
    tempHeteroFreq = HeteroFreq*HeteroFitness
    # get normalizing wbar factor, should be less than 1
    wbar = tempHeteroFreq+tempHomoDomFreq+tempHomoRecFreq
    # normalize the genotypic frequencies. This applies the fitness to get the new genotypic frequencies
    # add them all up and it should equal 1
    HomoRecFreq= tempHomoRecFreq/wbar
    HomoDomFreq= tempHomoDomFreq/wbar
    HeteroFreq= tempHeteroFreq/wbar

    # calculate new allelic frequencies
    # A freq = AA+ (1/2)Aa
    RecessiveAllelePercent = HomoRecFreq + 0.5*HeteroFreq
    DominantAllelePercent = HomoDomFreq+ 0.5*HeteroFreq



#plot the gene frequencies
ReccessiveLegend, = plt.plot(RecessiveAlleleFreqs, label='Reccesive allele frequency (a)')
DominantLegend, = plt.plot(DominantAlleleFreqs, label='Dominant allele frequency (A)')
plt.legend(handles=[ReccessiveLegend, DominantLegend])

plt.ylabel('Proportion of population (0.0-1.0)')
plt.title("Allele Frequency over time")
plt.xlabel("number of generations")
plt.show()
print("dominant frequency makes up {:.2f} % of the population".format(DominantAllelePercent*100))
inputFile.close()

HomoRecLegend, = plt.plot(HomoRecFreqs, label='Homozygous recessive frequency (aa)')
HomoDomLegend, = plt.plot(HomoDomFreqs, label='Homozygous dominant frequency (AA)')
HeteroLegend, = plt.plot(HeteroFreqs, label='Heterozygous frequency (Aa)')
plt.legend(handles=[HomoRecLegend,HomoDomLegend,HeteroLegend])
plt.title("Genotype Frequencies over time")
plt.xlabel("Number of generations")
plt.ylabel("Genotype frequency")
plt.show()