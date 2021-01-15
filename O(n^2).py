from timeit import timeit
import json

code = """
def test(n):
    for i in range(n):
        pass

test({})
"""

lst = []
for i in range(100):
    n = i ** 2
    time = timeit(code.format(n), number=100)
    lst.append(time)

with open("time.json", "r") as f:
    data = json.load(f)

data["O(n^2)"] = lst

with open("time.json", "w") as f:
    json.dump(data, f)
