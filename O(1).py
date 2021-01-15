from timeit import timeit
import json

code = """
def test(n):
    return n % 2

test({})
"""

lst = []
for i in range(100):
    time = timeit(code.format(i), number=100)
    lst.append(time)

with open("time.json", "r") as f:
    data = json.load(f)

data["O(1)"] = lst

with open("time.json", "w") as f:
    json.dump(data, f)
