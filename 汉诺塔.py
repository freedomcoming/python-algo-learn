def hanoi(n, source, auxiliary, target):
    if n > 0:
        # 递归调用将 n-1 个盘子从源柱子移动到辅助柱子
        hanoi(n-1, source, target, auxiliary)
        
        # 将最底下的盘子从源柱子移动到目标柱子
        if source:
            target.append(source.pop())
            print_moves()
        
        # 递归调用将 n-1 个盘子从辅助柱子移动到目标柱子
        hanoi(n-1, auxiliary, source, target)

def print_moves():
    print("Source:", source)
    print("Auxiliary:", auxiliary)
    print("Target:", target)
    print("")

# 初始化三根柱子
source = [4, 3, 2, 1]
auxiliary = []
target = []

# 执行汉诺塔算法
hanoi(len(source), source, auxiliary, target)
