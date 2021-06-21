import time
import timeit



def func_one(n):
	return [str(num) for num in range(n) ]


def func_two(n):
	return list(map(str,range(n)))


start_time = time.time()
res1 = func_one(1000000)
#print (res1)
end_time = time.time()
elapsed_time = end_time - start_time
print (elapsed_time)



start_time1 = time.time()
res2 = func_two(1000000)
#print(res2)
end_time1 = time.time()

elapsed_time2 = end_time1 - start_time1
print (elapsed_time2)



setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

stmt = 'func_one(100)'

res3 = timeit.timeit(stmt,setup,number=100000)
print ("Timeit result for func_one is {}".format(res3))



setup2 = '''
def func_two(n):
    return list(map(str,range(n)))
'''

stmt2 = 'func_two(100)'


res4 = timeit.timeit(stmt,setup,number=100000)
print ("Timeit result for func_two is {}".format(res4))