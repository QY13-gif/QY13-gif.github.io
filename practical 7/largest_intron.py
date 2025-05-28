import re 
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA' #Give the sequence
max_length=0 #Initialize the max length
matches = re.finditer(r'GT.*?AG', seq) #Set up the match points and select them from the sequence
for match in matches:
    intron_length=len(match.group())
    if intron_length > max_length:
        max_length=intron_length
print("The longest length of introns is",max_length)


