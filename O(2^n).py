from timeit import timeit
import json


code = """
def test(n):
    for i in range(n):
        pass

test({})
"""

lst = []
for i in range(25):
    n = 2 ** i
    time = timeit(code.format(n), number=100)
    lst.append(time)

with open("time.json", "r") as f:
    data = json.load(f)

data["O(2^n)"] = lst

with open("time.json", "w") as f:
    json.dump(data, f)
