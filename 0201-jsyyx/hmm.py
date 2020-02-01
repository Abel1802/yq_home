#!usr/bin/env python3
# -*- coding: UTF-8 -*-
# author: lz
# date: 2020.02.01
'''
    using python to realize a example of HMM
'''
import numpy as np

def forward_algorithm(O, hmm_model):
    '''HMM Forward Algorithm
    Args:
         param O: observations O = (o1, o2, o3, ..., oT)
         param hmm_model: (pi, A, B)
    return: the probability of HMM_model generating O
    '''

    pi, A, B = hmm_model
    T = len(O)
    N = len(pi)
    prob = 0.0

    # define the forward_prob 'α'( replace of 'a')
    a = np.zeros((T, N))
    prob_list = []
    # initilization
    for i in range(N):
        a[0][i] = pi[i] * B[i][O[0]]
    # recurrence
    for t in range(1, T):
        for i in range(N):
            sum = 0
            for j in range(N):
                sum += a[t-1][j] * A[j][i]
            a[t][i] = sum * B[i][O[t]]

    # calculate the prob
    for n in range(N):
        prob += a[T-1][n]
    return prob

def backward_algorithm(O, hmm_model):
    '''HMM Backward Algorithm
    Args:
        param O: observations O = (o1, o2, o3, ..., oT)
        param hmm_model: (pi, A, B)
    return: the probability of HMM_model generating O
    '''

    pi, A, B = hmm_model
    T = len(O)
    N = len(pi)
    prob = 0.0

    return prob

def viterbi_algorithm(O, hmm_model):
    '''HMM Viterbi Algorithm
    Args:
        param O: observations O = (o1, o2, o3, ..., oT)
        param hmm_model: (pi, A, B)
    return: the probability of the best state sequence
            the best state sequence
    '''

    pi, A, B = hmm_model
    T = len(O)
    N = len(pi)
    best_prob, best_path = 0.0, []

    return best_prob, best_path

def main():
    color2id = {'H': 0, 'T' :1}
    # model parameters
    pi = [1/3, 1/3, 1/3]
    A = [[0.9, 0.05, 0.05],
         [0.45, 0.1, 0.45],
         [0.45, 0.45, 0.1]]
    B = [[0.5, 0.5],
         [0.75, 0.25],
         [0.25, 0.75]]
    # input
    observations = (0, 0, 1)
    hmm_model = (pi, A, B)
    # process
    observ_prob_forward = forward_algorithm(observations, hmm_model)
    print('observ_prob_forward: {}'.format(observ_prob_forward))

    observ_prov_backward = backward_algorithm(observations, hmm_model)
    print('observ_prob_backward: {}'.format(observ_prov_backward))

    best_prob, best_path = viterbi_algorithm(observations, hmm_model)
    print('best_prob: {}, best_path: {}'.format(best_prob, best_path))

if __name__ == "__main__":
    main()