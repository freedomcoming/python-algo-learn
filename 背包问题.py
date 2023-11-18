# 背包问题是动态规划中的一个经典问题，它包括 0-1 背包问题和背包问题。

# ### 0-1 背包问题

# 0-1 背包问题是指在限定总重量的情况下，从一组物品中选择部分物品装入背包，使得装入的物品价值最大化。

# 以下是一个用Python实现的 0-1 背包问题解决方案：


def knapsack_01(weights, values, total_weight):
    n = len(weights)
    dp = [[0] * (total_weight + 1) for _ in range(n + 1)]

    print(dp)

    for i in range(1, n + 1): # 物品
        for j in range(1, total_weight + 1): # 最大重量
            if weights[i - 1] <= j: # 重量小于目标重量时，dp进行状态转移 | 大于时无法进行
                dp[i][j] = max(
                    values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j]
                )
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp)
    return dp[n][total_weight]


# 示例
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
total_weight = 5

result = knapsack_01(weights, values, total_weight)
print(result)  # 输出: 7


# 在这段代码中，`knapsack_01` 函数接受三个参数：`weights` 是物品的重量列表，`values` 是对应的价值列表，`total_weight` 是背包的总重量限制。

# 1. `dp` 是一个二维数组，`dp[i][j]` 表示在前 i 个物品中，总重量不超过 j 的情况下，可以获得的最大价值。

# 2. 利用两层循环遍历所有可能的情况，根据状态转移方程更新 `dp` 数组。

# 3. 最终，`dp[n][total_weight]` 就是在给定重量限制下，可以获得的最大价值。


### 无限背包问题

# 无限背包问题是指在限定总重量的情况下，可以选择多个相同物品装入背包，使得装入的物品价值最大化。

# 以下是一个用Python实现的无限背包问题解决方案：


def knapsack_unbounded(weights, values, total_weight):
    n = len(weights)
    dp = [0] * (total_weight + 1)
    print(dp)
    for i in range(1, total_weight + 1):
        for j in range(n):
            if weights[j] <= i:  # 重量小于目标重量时，dp进行状态转移 | 大于时无法进行
                dp[i] = max(dp[i], values[j] + dp[i - weights[j]])  # dp[] values 最大list
    print(dp)
    return dp[total_weight]


# 示例
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
total_weight = 5

result = knapsack_unbounded(weights, values, total_weight)
print(result)  # 输出: 8


# 这段代码实现了无限背包问题的解决方案，其基本原理与0-1背包问题类似，但在状态转移方程的设计上有所区别。

# 无限背包问题中的状态转移方程为：`dp[i] = max(dp[i], values[j] + dp[i-weights[j]])`，它表示在考虑第 j 个物品时，可以选择将其放入背包，并更新总价值。

# 无论是0-1背包问题还是无限背包问题，都是经典的动态规划应用场景。你可以根据具体的问题需求选择合适的背包问题解决方案。
