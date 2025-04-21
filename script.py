import textwrap

def translate(seq1):
    seq1 = seq1.upper() #convert to uppercase
    seq = ''

    for nucleotide in seq1:
        match nucleotide:
            case 'A':
                seq += 'U'
            case 'T':
                seq += 'A'
            case 'G':
                seq += 'C'
            case 'C':
                seq += 'G'
    
    seq = seq.replace(" ", "").replace("\n", "").replace("\r", "") # removing new line and spaces
    index = seq.find("AUG") # Finding starting codon
    if index == -1:
        return ('Strating codon not found, sequence can\'t be translated.')

    new_seq = seq[index:] # The sequence is sliced from the start codon onward.
    list_seq = textwrap.wrap(new_seq, 3)
    trans_seq = []
    
    # slicing sequence from stop codon
    for codon in list_seq:
        if codon == 'UAA' or codon == 'UAG' or codon == 'UGA':
            break
        else:
            trans_seq.append(codon)

    amino_seq = ''
    for codon in trans_seq:
        match codon:
            case 'AUG':
                amino_seq += 'M'
            case 'UUU':
                amino_seq += 'F'
            case 'UUC':
                amino_seq += 'F'
            case 'UUA':
                amino_seq += 'L'
            case 'UUG':
                amino_seq += 'L'
            case 'CUU':
                amino_seq += 'L'
            case 'CUC':
                amino_seq += 'L'
            case 'CUA':
                amino_seq += 'L'
            case 'CUG':
                amino_seq += 'L'
            case 'AUU':
                amino_seq += 'I'
            case 'AUC':
                amino_seq += 'I'
            case 'AUA':
                amino_seq += 'I'
            case 'GUU':
                amino_seq += 'V'
            case 'GUA':
                amino_seq += 'V'
            case 'GUC':
                amino_seq += 'V'
            case 'GUG':
                amino_seq += 'V'
            case 'UCU':
                amino_seq += 'S'
            case 'UCG':
                amino_seq += 'S'
            case 'UCA':
                amino_seq += 'S'
            case 'UCC':
                amino_seq += 'S'
            case 'CCU':
                amino_seq += 'P'
            case 'CCC':
                amino_seq += 'P'
            case 'CCA':
                amino_seq += 'P'
            case 'CCG':
                amino_seq += 'P'
            case 'ACU':
                amino_seq += 'T'
            case 'ACA':
                amino_seq += 'T'
            case 'ACC':
                amino_seq += 'T'
            case 'ACG':
                amino_seq += 'T'
            case 'GCU':
                amino_seq += 'A'
            case 'GCC':
                amino_seq += 'A'
            case 'GCA':
                amino_seq += 'A'
            case 'GCG':
                amino_seq += 'A'
            case 'UAU':
                amino_seq += 'Y'
            case 'UAC':
                amino_seq += 'Y'
            case 'CAU':
                amino_seq += 'H'
            case 'CAC':
                amino_seq += 'H'
            case 'CAA':
                amino_seq += 'Q'
            case 'CAG':
                amino_seq += 'Q'
            case 'AAU':
                amino_seq += 'N'
            case 'AAC':
                amino_seq += 'N'
            case 'AAA':
                amino_seq += 'K'
            case 'AAG':
                amino_seq += 'K'
            case 'GAU':
                amino_seq += 'D'
            case 'GAC':
                amino_seq += 'D'
            case 'GAA':
                amino_seq += 'E'
            case 'GAG':
                amino_seq += 'E'
            case 'UGU':
                amino_seq += 'C'
            case 'UGC':
                amino_seq += 'C'
            case 'UGG':
                amino_seq += 'W'
            case 'GGU':
                amino_seq += 'G'
            case 'GGC':
                amino_seq += 'G'
            case 'GGA':
                amino_seq += 'G'
            case 'GGG':
                amino_seq += 'G'
            case 'AGA':
                amino_seq += 'R'
            case 'AGG':
                amino_seq += 'R'
            case 'AGU':
                amino_seq += 'S'
            case 'AGC':
                amino_seq += 'S'
            case 'CGC':
                amino_seq += 'R'
            case 'CGA':
                amino_seq += 'R'
            case 'CGG':
                amino_seq += 'R'
            case 'CGU':
                amino_seq += 'R'
            case _:
                amino_seq += 'Invalid codon found in your sequence'
                break

    new_seq = list(amino_seq)
    return ('-'.join(new_seq))


seq = 'atggtactggtcagatgcctgcatcgatcgctgctagctagctaaggctag'

print(translate(seq))