from timeit import timeit
import json


code = """
def test(n):
    for i in range(n):
        pass

test({})
"""

lst = []
for i in range(10):
    n = i ** i
    time = timeit(code.format(n), number=10)
    lst.append(time)

with open("time.json", "r") as f:
    data = json.load(f)

data["O(n^n)"] = lst

with open("time.json", "w") as f:
    json.dump(data, f)
