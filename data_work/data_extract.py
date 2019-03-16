import pickle

def main():

    fl = open('../data/corpus1_clear', 'r')
    dist_words = []
    dist_set = set({})
    word2ind = {}
    word_counts = []

    for line in fl.readlines():
        for word in line.split():

            if word in dist_set:
                word_counts[word2ind[word]] += 1
                continue
            
            dist_words.append(word)
            word_counts.append(1)
            word2ind[word] = len(dist_words) - 1
            dist_set.add(word)

    corpus_word_data = {'dist_words' : dist_words, 'word2ind' : word2ind, 'word_counts' : word_counts}
    fl.close()
    fl = open('../data/corpus_word_data', 'ab')
    pickle.dump(corpus_word_data, fl)
    fl.close()

if __name__ == '__main__':
    main()