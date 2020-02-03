#!usr/bin/env python3
# -*- coding: UTF-8 -*-
# author: lz
# date: 2020.02.01
'''
    计算语言学 第六章 HMM课后作业：
    投掷硬币：
            三枚硬币，随机选择一枚，进行抛掷，记录抛掷结果。可以描述为一个三个状态的隐马尔科夫模型λ。

            λ = (S, V, A, B, π)，（其中S为状态集合，V为观察集合）S = {1, 2, 3}, V = {H, T}

            A =
                0.9 | 0.05 | 0.05
                0.45 | 0.1 | 0.45
                0.45 | 0.45 | 0.1

            B =
                0.5 | 0.75 | 0.25
                0.5 | 0.25 | 0.75

            π = {1/3, 1/3, 1/3}
    根据硬币的例题，计算THH输出的概率以及对应的最佳状态序列（即硬币序列）
'''
import numpy as np

def forward_algorithm(O, hmm_model):
    '''
    HMM--前向算法
    param O: 观察序列 = (o1, o2, o3, ..., oT)
    param hmm_model: HMM模型的三个参数(pi, A, B)
    return: 观测序列的概率
    '''
    pi, A, B = hmm_model
    T = len(O)
    N = len(pi)
    prob = 0.0

    # 定义前向概率 'α'( replace of 'a')
    a = np.zeros((T, N))
    prob_list = []
    # 初始化前向概率 a(t=0)
    for i in range(N):
        a[0][i] = pi[i] * B[i][O[0]]
    # 递推a在（t=1,2,...T-1）下的概率
    for t in range(1, T):
        for i in range(N):
            sum = 0
            for j in range(N):
                sum += a[t-1][j] * A[j][i]
            a[t][i] = sum * B[i][O[t]]
    # 求出最终的观测序列的概率prob
    for n in range(N):
        prob += a[T-1][n]
    return prob

def backward_algorithm(O, hmm_model):
    '''
    HMM--后向算法
    param O: 观察序列 = (o1, o2, o3, ..., oT)
    param hmm_model: HMM模型的三个参数(pi, A, B)
    return: 观测序列O的概率
    '''

    pi, A, B = hmm_model
    T = len(O)
    N = len(pi)
    prob = 0.0
    # 定义后向概率 β（replace of b）
    b = np.zeros((T,N))
    # 初始化后向概率 （b在t=T-1时刻）
    for i in range(N):
        b[T-1][i] = 1
    # 递推，计算b在t=T-2,T-3,...,0
    for t in range(T-2, -1, -1):
        for i in range(N):
            sum_before = 0
            for j in range(N):
                sum_before += A[i][j] * b[t+1][j]
            b[t][i] += sum_before * B[i][O[t]]
    # 计算观测序列的概率prob
    for n in range(N):
        prob += pi[i] * b[0][n] * B[n][O[0]]
    return prob

def viterbi_algorithm(O, hmm_model):
    '''
    HMM--Viterbi算法
    param O: 观察序列 = (o1, o2, o3, ..., oT)
    param hmm_model: HMM模型的三个参数(pi, A, B)
    return: 观测序列的最佳概率，以及观测序列的最佳状态序列
    '''

    pi, A, B = hmm_model
    T = len(O)
    N = len(pi)
    best_prob, best_path = 0.0, []

    # 定义两个变量δ，ψ，（以下用delta, psi表示）
    delta = [[0 for i in range(4)] for i in range(T)]
    psi = np.zeros((T,N),dtype=int)
    # 初始化delta, psi
    for i in range(N):
        delta[0][i] = pi[i] * B[i][O[0]]
        psi[0][i] = 0
    # 递推
    for t in range(1, T):
        for i in range(N):
            # 初始化一个临时列表，用于存放3种概率
            temDetla = [0] * 4
            for j in range(N):
                temDetla[j] = delta[t-1][j] * A[j][i]
            # 找到最大的那个δ
            maxDelta = max(temDetla)
            # 记录最大值对应的状态,然后放入ψ中
            maxDeltaIndex = temDetla.index(maxDelta)
            psi[t][i] = maxDeltaIndex
            # 将找到的最大值乘以b放入δ
            delta[t][i] = maxDelta * B[i][O[t]]

    # 获得最佳概率best_prob(找到T-1时刻的最大值)
    best_prob = max(delta[T - 1])
    # 终止，开始生成状态链，best_path
    # 获取最后一个状态的最大状态概率对应的索引
    i_opt = delta[T - 1].index(max(delta[T - 1]))
    # 将索引添加到best_path
    best_path.append(i_opt)
    # 最后一步，最优路径回溯
    # 从后向前遍历整条链
    for t in range(T-1, 0, -1):
        # 不断地从当前时刻t的ψ列表中读取到t-1的最优状态
        i_opt = psi[t][i_opt]
        # 放入最佳路径best_path中
        best_path.append(i_opt)
    # 因为是从后往前将状态放入的列表，所以这里需要翻转一下，变成了从前往后
    best_path.reverse()
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
    print('Viterbi算法的THH概率: {}, THH的最佳序列状态: {},这里的{}指的是第{}个硬币'.format(best_prob, best_path, best_path[0], best_path[0] + 1))

if __name__ == "__main__":
    main()