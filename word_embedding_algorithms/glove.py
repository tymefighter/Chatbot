import pickle
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

def initialize_params(n, k):

    # U: target words, V: context words
    U = tf.get_variable('U', shape = (n, k, 1), dtype = tf.float32, initializer = tf.random_normal_initializer(seed=0))
    V = tf.get_variable('V', shape = (n, k, 1), dtype = tf.float32, initializer = tf.random_normal_initializer(seed=0))

    bt = tf.get_variable('bt', shape = (n, 1, 1), dtype = tf.float32, initializer = tf.random_normal_initializer(seed=0))
    bc = tf.get_variable('bc', shape = (n, 1, 1), dtype = tf.float32, initializer = tf.random_normal_initializer(seed=0))

    return U, V, bt, bc

def compute_cost(U, V, bt, bc, X, n):

    cost = tf.get_variable('cost', shape = (1, 1), initializer = tf.zeros_initializer)
    for i in range(n):
        for j in range(n):
            # i: target, j: context
            cost += tf.cond(tf.equal(X[j][i], tf.constant(0.0)), lambda: tf.constant(0.0), lambda: (tf.matmul(tf.transpose(U[i]), V[j]) + bt[i] + bc[j] - tf.log(X[j][i]))**2)

    return cost

def model(dist_words, word2ind, M, k = 50, iters = 100):

    U, V, bt, bc = initialize_params(len(dist_words), k)
    X = tf.placeholder(dtype = tf.float32, shape = M.shape, name = 'M')

    cost = compute_cost(U, V, bt, bc, X, len(dist_words))
    train = tf.train.AdamOptimizer(0.001).minimize(cost)
    init = tf.global_variables_initializer()

    costs = []
    with tf.Session() as sess:
        
        sess.run(init)
        for i in range(iters):
            sess.run(train, feed_dict = {X : M})
            costs.append(np.float(sess.run(cost, feed_dict = {X: M})))

        E = (sess.run(U) + sess.run(V)) / 2.0
    
    plt.plot(costs, 'b+')
    plt.show()
    return E
def main():

    fl1 = open('../data/corpus_word_data', 'rb')
    fl2 = open('../data/co_occ', 'rb')

    corpus_word_data = pickle.load(fl1)
    co_occ = pickle.load(fl2)

    fl1.close()
    fl2.close()

    dist_words = corpus_word_data['dist_words']
    word2ind = corpus_word_data['word2ind']
    M = co_occ['M']
    
    E = model(dist_words, word2ind, M, k = 50, iters = 700)

    fl = open('../data/glove', 'wb')
    pickle.dump(E, fl)

if __name__ == '__main__':
    main()