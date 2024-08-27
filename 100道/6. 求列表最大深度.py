a = [2, [3, [1, 2]]]


def list_depth(item):
    if isinstance(item, list):
        max_depth = 1

        for i in item:
            max_depth = max(list_depth(i) + 1, max_depth)


        return max_depth
    
    return 0


print(list_depth(a))
