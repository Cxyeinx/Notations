from timeit import timeit
import json

code = """
def test(n):
    return sum(n)

test({})
"""

lst = []
for i in range(100):
    no = [j for j in range(i)]
    time = timeit(code.format(no), number=100)
    lst.append(time)

with open("time.json", "r") as f:
    data = json.load(f)

data["O(n)"] = lst

with open("time.json", "w") as f:
    json.dump(data, f)
