def mean(seq): #simplest computation of mean
    n = len(seq)
    return sum(seq)/float(n)

def transpose(seqseq): #simple 2-dimensional transpose
    return zip(*seqseq)
