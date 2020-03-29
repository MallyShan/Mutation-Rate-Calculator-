# Mutation-Rate-Calculator-
Calculates the mutation rate between two genomic sequences, specficially variations in the coronavirus
Three files:
1) MutationComparison.py - Python file that has two functions/methods: The Comparison function iterates through both genomic sequences and compares each base to see if they are equal. If they are not, that position is added into an array that saves all the positions in the genomes where there are differences in the base pair. The MutationRate function calculates the mutation rate from the array generated before, by dividing the length of the array which represents the total number of mutations by the length of the smallest genome or two times one of the genome's length if they are of the same length.

2) Virus text files - Text files that contain the genomic sequences of each variation of the gene marked by the origin of the country. 

3) Graph files - pictures of the graphs created by the output from the program in the combinations of the eleven countries. 
