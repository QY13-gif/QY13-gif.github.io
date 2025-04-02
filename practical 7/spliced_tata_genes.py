import re
import os

def extract_gene_name(header):
    #Define the extract_gene_name
    match = re.search(r'gene:(\S+)', header)
    return match.group(1) if match else header.split()[0]

def count_tata_boxes(sequence):
    #Define the times the tata appears
    return len(re.findall(r'TATAAA|TATATA|TATATAA', sequence))

def has_splice_pattern(sequence, pattern):
    #Define the splice pattern
    donor = pattern[:2]  #Define the donor position
    acceptor = pattern[2:]  #Define the acceptor position
    
    donor_positions = [m.start() for m in re.finditer(f'(?={donor})', sequence)]
    
    for pos in donor_positions:
        remaining_seq = sequence[pos+2:]
        if acceptor in remaining_seq:
            return True
    return False

def process_spliced_genes(input_file, output_file, splice_pattern):
    #Making a process of the input file
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        current_seq = []
        current_header = None
        
        for line in infile:
            if line.startswith('>'):
                if current_header and current_seq:
                    full_seq = ''.join(current_seq)
                    tata_count = count_tata_boxes(full_seq)
                    if tata_count > 0 and has_splice_pattern(full_seq, splice_pattern):
                        gene_name = extract_gene_name(current_header)
                        outfile.write(f'>{gene_name} TATA_count:{tata_count}\n{full_seq}\n')
                
                current_header = line.strip()
                current_seq = []
            else:
                current_seq.append(line.strip())
        
        if current_header and current_seq:
            full_seq = ''.join(current_seq)
            tata_count = count_tata_boxes(full_seq)
            if tata_count > 0 and has_splice_pattern(full_seq, splice_pattern):
                gene_name = extract_gene_name(current_header)
                outfile.write(f'>{gene_name} TATA_count:{tata_count}\n{full_seq}\n')

def main():
    #Making a model for the interaction 
    valid_patterns = ['GTAG', 'GCAG', 'ATAG']
    while True:
        splice_pattern = input("Enter splice donor/acceptor combination (GTAG, GCAG, or ATAG): ").upper()
        if splice_pattern in valid_patterns:
            break
        print("Invalid pattern. Please try again.")
    
    input_fasta = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
    output_file = f'{splice_pattern}_spliced_genes.fa'
    
    if not os.path.exists(input_fasta):
        print(f"Error: Input file '{input_fasta}' not found!")
        return
    
    process_spliced_genes(input_fasta, output_file, splice_pattern)
    print(f"Results saved to: {output_file}")

if __name__ == "__main__":
    main()  