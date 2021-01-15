from timeit import timeit
import matplotlib.pyplot as plt
import math


code = """
def test(n):
    for i in range(n):
        pass
        
test({})
"""

lst = []
for i in range(14):
    print(i)
    n = math.factorial(i)
    time = timeit(code.format(n), number=1)
    lst.append(time)

plt.plot([x for x in range(len(lst))], lst)
plt.show()

print(lst)
