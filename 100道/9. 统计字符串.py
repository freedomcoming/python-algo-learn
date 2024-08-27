from collections import Counter




print("".join(map(lambda x: x[0]+str(x[1]),Counter("AABBCC").most_common())))