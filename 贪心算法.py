# 贪心算法是一种解决优化问题的算法，它每步都选择当前状态下的最优解，从而希望能够获得全局最优解。

# 以下是一个用Python实现的贪心算法示例——找零钱问题：


def make_change(coins, amount):
    coins.sort(reverse=True)  # 按面额从大到小排序

    num_coins = 0
    i = 0

    while amount > 0 and i < len(coins):
        if coins[i] <= amount:
            num_coins += amount // coins[i] # 最大面额的数量 贪心
            amount = amount % coins[i] # 除去最大面额的硬币，剩余的额度
        i += 1

    return num_coins if amount == 0 else -1


# 示例
coins = [1, 5, 10, 25]
amount = 36

result = make_change(coins, amount)
print(result)  # 输出: 4 (需要1个25美分，1个10美分，1个1美分)


# 在这段代码中，`make_change` 函数接受一个硬币面额的列表 `coins` 和一个需要找零的金额 `amount`。

# 1. 首先，将硬币按面额从大到小排序。

# 2. 使用一个循环，在每一步中，尽可能选择当前面额可以使用的最大数量，直到找零完毕或者所有面额都尝试过。

# 3. 如果成功找零完毕，返回所使用的硬币数量，否则返回 -1。

# 这是一个简单的贪心算法示例，解决了找零钱的问题。需要注意的是，贪心算法并不总是能够得到全局最优解，但在某些情况下，它可以提供一个接近最优解的解决方案。

# 在实际应用中，需要根据具体问题的特性来确定是否可以使用贪心算法。有些问题适合用贪心算法解决，而有些问题可能需要更复杂的算法来找到最优解。
