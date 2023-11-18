from joblib import Parallel, delayed
import time, math

def my_fun(i):
    """ We define a simple function here.
    """
    time.sleep(1)
    return math.sqrt(i**2)



start = time.time()
num = 10
# n_jobs is the number of parallel jobs
Parallel(n_jobs=10)(delayed(my_fun)(i) for i in range(num))
end = time.time()
print('{:.4f} s'.format(end-start))



"""
除了并行计算功能外，Joblib还具有以下功能：

快速磁盘缓存：Python函数的memoize或make-like功能，适用于任意Python对象，包括大型numpy数组。
快速压缩：替代pickle，使用joblib.dump和joblib.load可以提高大数据的读取和存储效率。

"""