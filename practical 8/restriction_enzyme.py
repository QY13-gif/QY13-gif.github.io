dna_sequence=input("the dna_sequence is:")
enzyme_sequence=input("the restriction enzyme is:")
def find_cut_sites(dna_sequence,enzyme_sequence):
    for i in range(len(dna_sequence)-len(enzyme_sequence)+1):
        if dna_sequence[i:i + len(enzyme_sequence)] == enzyme_sequence:
            return i + 1
        
    return "No"
print(find_cut_sites(dna_sequence,enzyme_sequence))
#example
print(find_cut_sites("ACTCCGTAA","CCGT"))
#It will print"4"