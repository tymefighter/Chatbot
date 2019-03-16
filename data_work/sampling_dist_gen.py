import pickle
import numpy as np

def main():

    with open('../data/corpus_word_data', 'rb') as fl:

        corpus_word_data = pickle.load(fl)
        word_counts = corpus_word_data['word_counts']
        word_counts = np.array(word_counts)
    
    word_counts = (word_counts) ** (3.0/4.0)
    prob_samp = word_counts / np.sum(word_counts)

    with open('../data/prob_samp', 'wb') as fl:

        pickle.dump(prob_samp, fl)

if __name__ == '__main__':
    main()