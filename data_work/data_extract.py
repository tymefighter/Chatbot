import pickle

def main():

    fl = open('../data/corpus1_clear', 'r')
    dist_words = []
    dist_set = set({})
    word2ind = {}

    for line in fl.readlines():
        for word in line.split():

            if word in dist_set:
                continue
            
            dist_words.append(word)
            word2ind[word] = len(dist_words) - 1
            dist_set.add(word)

    corpus_word_data = {'dist_words' : dist_words, 'word2ind' : word2ind}
    fl.close()
    fl = open('../data/corpus_word_data', 'ab')
    pickle.dump(corpus_word_data, fl)
    fl.close()

if __name__ == '__main__':
    main()