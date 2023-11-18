def bucket_sort(arr):
    # 创建空桶
    buckets = [[] for _ in range(len(arr))]

    print(buckets)
    
    # 将元素分配到对应的桶中
    for num in arr:
        index = int(num * len(arr))
        # print(index)
        buckets[index].append(num)
    
    # 对每个桶中的元素进行排序
    for bucket in buckets:
        bucket.sort()
    
    # 将排序后的桶合并
    sorted_arr = [num for bucket in buckets for num in bucket]
    
    return sorted_arr

# 示例
arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
sorted_arr = bucket_sort(arr)
print(sorted_arr)
