def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10


    # print(output,count,sep="\n")

    for i in range(n):
        # 当前末位数 index % 10
        index = arr[i] // exp

        # 末位数数量加1
        count[index % 10] += 1


    print(count)

    for i in range(1, 10):
        # 大于当前尾数的数量
        count[i] += count[i - 1]
    
    print(count)

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

    print("-"*50)
    print("{:=^50s}".format("Split Line"))
def radix_sort(arr):
    max_element = max(arr)
    exp = 1
    while max_element // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# 使用示例
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("Sorted array:", arr)
