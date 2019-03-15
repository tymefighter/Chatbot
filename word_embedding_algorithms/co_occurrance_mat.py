import pickle
import numpy as np
from sklearn.decomposition import TruncatedSVD

def co_occ(fl_corpus, dist_words, word2ind, window_size = 4):
    n = len(dist_words)
    M = np.zeros((n, n))

    for line in fl_corpus.readlines():
        line = line.split()
        for k in range(len(line)):

            start = max(k - window_size, 0)
            end = max(k - 1, 0)
            for r in range(start, end+1):
                M[word2ind[line[k]], word2ind[line[r]]] += 1

            start = min(k + 1, len(line) - 1) 
            end = min(k + window_size, len(line) - 1)
            for r in range(start, end+1):
                M[word2ind[line[k]], word2ind[line[r]]] += 1
    return M

def reduce_dim(M, k):

    n_iters = 10
    M_reduced = None

    svd = TruncatedSVD(n_components = k, algorithm='randomized', n_iter = n_iters)
    M_reduced = svd.fit_transform(M)

    return M_reduced

def main():

    fl_corpus = open('../data/corpus1_clear', 'r')
    fl = open('../data/corpus_word_data', 'rb')
    corpus_word_data = pickle.load(fl)
    dist_words = corpus_word_data['dist_words']
    word2ind = corpus_word_data['word2ind']
    fl.close()

    M = co_occ(fl_corpus, dist_words, word2ind)
    M_reduced = reduce_dim(M, 50)
    fl_corpus.close()

    fl = open('../data/co_occ', 'ab')
    pickle.dump(M_reduced, fl)
    fl.close()

    


if __name__ == '__main__':
    main()