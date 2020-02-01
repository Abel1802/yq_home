# HMM
## Three basic problems:

* **Probability compute(estimate)**    
* **Decoding problem(prediction)**  
* **Learning problem(training)**  
- - -  

## The jsyyx's homework:  
+ 投掷硬币
    + 三枚硬币，随机选择一枚，进行抛掷，记录抛掷结果。可以描述为一个三个状态的隐马尔科夫模型λ。  
    + λ = (S, V, A, B, π)，（其中S为状态集合，V为观察集合）S = {1, 2, 3}, V = {H, T}   
    + A = 
         0.9  | 0.05 | 0.05  
         0.45 | 0.1  | 0.45  
         0.45 | 0.45 | 0.1   
    + B = 
         0.5  | 0.75 | 0.25  
         0.5  | 0.25 | 0.75  
    + π = {1/3, 1/3, 1/3}
- - -
+ 根据硬币的例题，计算THH输出的概率以及对应的最佳状态序列（即硬币序列）。
- - -
