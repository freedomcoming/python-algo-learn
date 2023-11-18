s = [1, 5, 6, 1, 7, 9, 3, 10, 66]


"""
gpt 版本

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # 选择基准元素
    left = [x for x in arr if x < pivot]  # 小于基准的放在左边
    middle = [x for x in arr if x == pivot]  # 等于基准的放在中间
    right = [x for x in arr if x > pivot]  # 大于基准的放在右边
    
    return quick_sort(left) + middle + quick_sort(right)

# 示例
arr = [5, 1, 9, 3, 7, 6, 8]
sorted_arr = quick_sort(arr)
print(sorted_arr)


"""

def fast_sort(arr):
    
    if len(arr) < 2:
        return arr

    else:
        mid = len(arr) // 2
        left = []
        right = []
        for item in arr:
            if item < arr[mid]:
                left.append(item)
            if item > arr[mid]:
                right.append(item)
            else:
                m = arr[mid]
        return fast_sort(left) + [m] + fast_sort(right)


if __name__ == "__main__":
    print(fast_sort(s))
