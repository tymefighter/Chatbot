import pickle
import numpy as np

def main():

    fl = open("../data/corpus_word_data", 'rb')
    corpus_word_data = pickle.load(fl)
    fl.close()

    dist_words = corpus_word_data['dist_words']
    n = len(dist_words)

    one_hot = np.identity(n)

    fl = open("../data/one_hot", 'wb')
    pickle.dump(one_hot, fl)
    fl.close()

if __name__ == '__main__':

    main()
