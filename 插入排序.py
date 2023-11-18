def insert_sort(arr):
    for i in range(1, len(arr)):
        print(i)
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j] # 大的 往后移动
            j -= 1 # key 插入位置的变化
        arr[j + 1] = key # key 插入位置


arr = [64, 34, 25, 12, 22, 11, 90]
insert_sort(arr)
print("排序后的数组：", arr)
