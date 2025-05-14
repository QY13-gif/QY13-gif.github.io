import numpy as np #import numpy
from Bio import SeqIO  #using Biopython and SeqIo
def load_fasta(filename):  #Define the load_fasta, input the file, output the sequence
    with open(filename) as f:
        record = SeqIO.read(f, "fasta")
    return str(record.seq)
#Get these three sequences
human_seq=load_fasta(r"C:\Users\cqy111\Desktop\IBI1\QY13-gif.github.io\practical 13\P04179(human).fasta")
mouse_seq=load_fasta(r"C:\Users\cqy111\Desktop\IBI1\QY13-gif.github.io\practical 13\P09671(mouse).fasta")
random_seq=load_fasta(r"C:\Users\cqy111\Desktop\IBI1\QY13-gif.github.io\practical 13\random sequence.fasta")

#Define the load_blosum, input the blosum matrix file, output a dictionary, including the AA name and the scores
def load_blosum(filename):
    blosum={}
    with open(filename) as f:
        while True: #Ensure just selecting useful words
            line = f.readline() 
            if not line.startswith("#"):
                break
        #Make a list
        amino_acids = line.strip().split()
        #Remove blank lines
        for line in f:
            if line.strip() == "":
                continue
            parts = line.strip().split()
            aa = parts[0]
            scores = list(map(int, parts[1:]))
            blosum[aa] = {k:v for k,v in zip(amino_acids, scores)}
    
    return blosum
#Get the blosum62 function
blosum62 = load_blosum(r"C:\Users\cqy111\Desktop\IBI1\QY13-gif.github.io\practical 13\BLOSUM62.txt")

#Make the calculate_alingnment function, input the sequences and the matrix, output the score and identity
def calculate_alignment(seq1, seq2, matrix):
    score=0 #Initialize the score and the identical
    identical=0
    for aa1, aa2 in zip(seq1, seq2): #Selectt the corresponding AAs in these 2 sequences
        score += matrix[aa1][aa2] #Get the score by using the matrix
        #If the 2 AAs are same, change the identical
        if aa1 == aa2:
            identical += 1
    #Get the identity, equal to the proportion of same AAs in all AAs
    percent_identity = (identical / len(seq1)) * 100
    #Get the score and identity
    return score, percent_identity
#Show the scores and identities in these 3 comparing groups
print("comparing results")
score1,identity1=calculate_alignment(human_seq,mouse_seq,blosum62)
print(f"human-mouse: score={score1}, identity={identity1}%")
score2,identity2=calculate_alignment(human_seq,random_seq,blosum62)
print(f"human-random: socre={score2}, identity={identity2}%")
score3,identity3=calculate_alignment(mouse_seq,random_seq,blosum62)
print(f"mouse-random: score={score3}, identity={identity3}%")
