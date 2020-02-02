#!usr/bin/env python3
# -*- coding: UTF-8 -*-
# author: lz
# date: 2020.02.01
'''
    using python to realize a example of HMM
'''
import numpy as np

# return the list max element's index
def list_max_i(l):
    max = 0
    for i in range(len(l)):
        if max < l[i]:
            max = l[i]
            max_index = i
    return int(max_index)

def forward_algorithm(O, hmm_model):
    '''HMM Forward Algorithm
    Args: param O: observations O = (o1, o2, o3, ..., oT)
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
    # recurrence from a1 to a2 to a3 to .. to aT
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
    Args: param O: observations O = (o1, o2, o3, ..., oT)
          param hmm_model: (pi, A, B)
    return: the probability of HMM_model generating O
    '''

    pi, A, B = hmm_model
    T = len(O)
    N = len(pi)
    prob = 0.0
    # define the back_prob β（replace of b）
    b = np.zeros((T,N))
    # step-1: initialize b
    for i in range(N):
        b[T-1][i] = 1
    # step-2: from bT to bT-1 to bT-2 to bT-3 ..., to b1
    for t in range(T-2, -1, -1):
        for i in range(N):
            sum_before = 0
            for j in range(N):
                sum_before += A[i][j] * b[t+1][j]
            b[t][i] += sum_before * B[i][O[t]]
    # step-3: calculate the prob
    for n in range(N):
        prob += pi[i] * b[0][n] * B[n][O[0]]
    return prob

def viterbi_algorithm(O, hmm_model):
    '''HMM Viterbi Algorithm
    Args: param O: observations O = (o1, o2, o3, ..., oT)
          param hmm_model: (pi, A, B)
    return: the probability of the best state sequence && the best state sequence
    '''

    pi, A, B = hmm_model
    T = len(O)
    N = len(pi)
    best_prob, best_path = 0.0, []

    # define the max_var d, the best_path y
    d = np.zeros((T,N))
    y = np.zeros((T,N),dtype=int)
    # step-1: initilize d & y
    for i in range(N):
        d[0][i] = pi[i] * B[i][O[0]]
        y[0][i] = 0

    # step-2: from d0 to d1 to d2 to ..., to dT
    for t in range(1, T):
        for i in range(N):
            max_list = []
            for j in range(N):
                max_list.append(d[t-1][j] * A[j][i])
            d[t][i] = max(max_list) * B[i][O[t]]
            y[t][i] = list_max_i(max_list)

    # step-3: calculate the best_prob
    d_last = d[T-1:]
    best_prob = max(max(d_last))

    # step-4: calculate the best_path
    # obtain the last observation value
    end_observ = list_max_i(max(d_last))
    best_path.append(end_observ + 1)
    # obtain the remain observations
    for n in range(T-1, 0, -1):
        best_path.append(y[n][end_observ] + 1)
        end_observ = y[n][end_observ]

    return best_prob, best_path

def main():
    color2id = {0: 'T', 1: 'H'}
    # model parameters
    pi = [1/3, 1/3, 1/3]
    A = [[0.9, 0.05, 0.05],
         [0.45, 0.1, 0.45],
         [0.45, 0.45, 0.1]]
    B = [[0.5, 0.5],
         [0.75, 0.25],
         [0.25, 0.75]]
    # input
    observations = (0, 1, 1)
    hmm_model = (pi, A, B)
    # process
    observ_prob_forward = forward_algorithm(observations, hmm_model)
    print('前向算法的THH概率: {}'.format(observ_prob_forward))

    observ_prov_backward = backward_algorithm(observations, hmm_model)
    print('后向算法的THH概率: {}'.format(observ_prov_backward))

    best_prob, best_path = viterbi_algorithm(observations, hmm_model)
    print('Viterbi算法的THH概率: {}, THH的最佳序列状态: {},这里的{}指的是第{}个硬币'.format(best_prob, best_path, best_path[0], best_path[0]))

if __name__ == "__main__":
    main()