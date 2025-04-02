import re
def extract_gene_name(header):
    match=re.search(r'gene:(\S+)',header)
    return match.group(1) if match else header.spilt()[0]
def has_tata_box(sequence):
    return re.search(r'TATAAA|TATATA|TATATAA',sequence) is not None
def process_fasta(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        current_seq = []
        current_header = None
        for line in infile:
            if line.startswith('>'):
                if current_header and current_seq:
                    full_seq =''.join(current_seq)
                    if has_tata_box(full_seq):
                        gene_name=extract_gene_name(current_header)
                        outfile.write(f'>{gene_name}\n{full_seq}\n')
                current_header=line.strip()
                current_seq=[]
            else:
                current_seq.append(line.strip())
        if current_header and current_seq:
            full_seq = ''.join(current_seq)
            if has_tata_box(full_seq):
                gene_name = extract_gene_name(current_header)
                outfile.write(f'>{gene_name}\n{full_seq}\n')
input_fasta =r'C:\Users\cqy111\Downloads\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_fasta ='tata_genes.fa'
output_fasta = r'C:\Users\cqy111\Desktop\tata_genes.fa'
process_fasta(input_fasta,output_fasta)

