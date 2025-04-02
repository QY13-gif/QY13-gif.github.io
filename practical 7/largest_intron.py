import re 
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
max_length=0
matches = re.finditer(r'GT.*?AG', seq)
for match in matches:
    intron_length=len(match.group())
    if intron_length > max_length:
        max_length=intron_length
print("The longest length of introns is",max_length)


