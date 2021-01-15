from timeit import timeit
import math
import json

code = """
def test(n):
    for i in range(int(n)):
        pass

test({})
"""

lst = []
for i in range(1, 100):
    log = math.log(i)
    time = timeit(code.format(log), number=100)
    lst.append(time)

with open("time.json", "r") as f:
    data = json.load(f)

data["O(log n)"] = lst

with open("time.json", "w") as f:
    json.dump(data, f)

