import functools

n = [2,3,4,5]
o = [1,2,3,54]

print(list(map(lambda x:x**2, n)))

print(list(filter(lambda x:x>2, n)))

print(functools.reduce(lambda x,y:x*y, n))

print(list(zip(n,o)))

import mem_profile

print(mem_profile.memory_usage_resource())