import re

def loadData():
    # load the file
    f = open('/Volumes/Data/nick/Downloads/rosalind_splc.txt', 'r')

    # get the lines in the file
    lines = f.readlines()
    # the dna string
    s = lines[0].split('\n')[0]
    # the introns
    introns = []
    for i in lines[1:]:
        introns.append(i.split('\n')[0])

    # close the file
    f.close()

    return (s, introns)

def load_prot_table():
    f = open('prot_lookup.txt')

    lookup = {}

    for line in f.readlines():
        [codon, acid] = line.split('\n')[0].split(' ')
        lookup[codon] = acid

    f.close()

    return lookup

def main():
    # load the protein lookup table
    lookup = load_prot_table()

    # load the data from the file
    [s, introns] = loadData()

    clean = s
    
    # find the position of each intron in s
    for intron in introns:
        r = re.search(intron, clean)
        clean = clean[:r.start()] + clean[r.end():]

    # replace T with U
    l =  list(clean)
    for i in range(len(l)):
        if l[i] == 'T':
            l[i] = 'U'

    clean = ''.join(l)
    
    p = []

    for i in range(0, len(clean), 3):
        p.append(lookup[clean[i:i+3]])

    print ''.join(p[:-1])

    return

if __name__ == '__main__':
    main()
