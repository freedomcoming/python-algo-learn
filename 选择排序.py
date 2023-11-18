def selection_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        # 假设当前位置是最小值的索引
        min_index = i
        
        # 在未排序的部分中找到最小值的索引
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # 将找到的最小值交换到已排序部分的末尾
        arr[i], arr[min_index] = arr[min_index], arr[i]

# 示例
arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print("排序后的数组：", arr)
