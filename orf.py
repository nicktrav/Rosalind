import re

def translate(s, d):
    trans = []
    
    for i in range(0, len(s), 3):
        trans.append(d[s[i:i+3]])

    return ''.join(trans)

def reverse_complement(s):
    s_rev = s[::-1]

    rc = []

    for i in s_rev:
        if i == 'A':
            rc.append('T')
        elif i == 'C':
            rc.append('G')
        elif i == 'G':
            rc.append('C')
        elif i == 'T':
            rc.append('A')   

    return ''.join(rc)         

def generate_lookup():
    f = open('dna_to_acid_lookup.txt')

    lines = f.readlines()

    d = {}
    for line in lines:
        [dna, acid] = line.split('\n')[0].split(' ')
        d[dna] = acid

    f.close()

    return d

def find_start_codons(s):
    res = re.finditer('ATG', s)
    start = []

    for i in res:
        start.append(i.start())

    return start

def find_stop_codons(s):
    res = re.finditer('TAA|TAG|TGA', s)
    end = []

    for i in res:
        end.append(i.start())

    return end

def find_start_stop_pairs(start_codons, stop_codons):
    pairs = []

    for i in start_codons:
        # find the first valid stop codon
        for j in stop_codons:
            if (i - j) % 3 == 0 and i < j:
                pairs.append((i, j))
                break

    return pairs

def generate_strings(start_stop_pairs, s, d):
    ORFs = []
    for pair in start_stop_pairs:
        ORFs.append(translate(s[pair[0]:pair[1]], d))

    return ORFs

def main():
    # open the file
    f = open('/Volumes/Data/nick/Downloads/rosalind_orf.txt')

    # read in the string
    s = f.readline().split('\n')[0]
    s_rc = reverse_complement(s)

    # close the file
    f.close()

    # import the codon lookup table
    lookup = generate_lookup()

    # find the indices of the start codons
    start_codons = find_start_codons(s)

    # find the indices of the stop codons
    stop_codons = find_stop_codons(s)

    # find the indices of the start and stop codons in reverse
    start_codons_rc = find_start_codons(s_rc)
    stop_codons_rc = find_stop_codons(s_rc)

    
    # find the valid pairs of start and stop positions for the string and its r.c
    start_stop_pairs = find_start_stop_pairs(start_codons, stop_codons)
    start_stop_pairs_rc = find_start_stop_pairs(start_codons_rc, stop_codons_rc)

    # generate the valid, translated strings for the string and its r.c
    valid_strings = generate_strings(start_stop_pairs, s, lookup)
    valid_strings_rc = generate_strings(start_stop_pairs_rc, s_rc, lookup)

    # eliminate repeats
    unique_strings = set().union(*[valid_strings, valid_strings_rc])

    for i in unique_strings:
        print i

if __name__ == '__main__':
    main()
