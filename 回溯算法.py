def backtrack(nums, path, result):
    if not nums:
        result.append(path)
        return
    
    for i in range(len(nums)):
        print(i)
        backtrack(nums[:i] + nums[i+1:], path + [nums[i]], result)

def permute(nums):
    result = []
    backtrack(nums, [], result)
    return result

# 示例
nums = [1, 2, 3]
permutations = permute(nums)
print(permutations)

if __name__ == '__main__':
    nums = [1, 2, 3]
    i = 0
    print(nums[:i] + nums[i+1:])