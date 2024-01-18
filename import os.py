import gzip
import seaborn as sns
import matplotlib.pyplot as plt 

#data = "aaaaaaaaaaaaaaababaaaaaaaaaaaaaaabbaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccc"

i = 0
j = 0
k_mers = ""
occ = 0
tab={}

def read_fastq(file_path):
    sequences = []
    with gzip.open(file_path, "rt") as file:
        for line in file:
            sequences.append(line.strip())
    return sequences

    
def count_occ(n, data):
    global i, j, k_mers, occ 
    while i < len(data):
        k_mers = data[i:n+i]
        if len(k_mers) == n :
            while j < len(data):
                if k_mers == data[j:n+j]:
                    occ += 1
                j += 1
            i += 1
            j = 0
            tab[k_mers] = occ
            occ = 0
        else:
            break


def plot(tab):
    sns.lineplot(x=list(tab.keys()), y = list(tab.values()))
    plt.xlabel("Sous-séquence")
    plt.ylabel("Nombre d'occurrences")
    plt.show()

#count_occ(20, data)
#print(tab)

data = read_fastq("C:/Users/HD/Downloads/chry5_S14_L001_R1_001.fastq.gz")
