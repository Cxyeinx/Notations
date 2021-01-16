import json
import matplotlib.pyplot as plt

with open("time.json", "r") as f:
    data = json.load(f)

fig, a = plt.subplots(2, constrained_layout=True)

a[0].set_title("O(1) vs O(n) vs O(log n) vs O(n log n)")
a[0].plot([x for x in range(len(data["O(n)"]))], data["O(n)"], color="red")
a[0].plot([x for x in range(len(data["O(1)"]))], data["O(1)"], color="blue")
a[0].plot([x for x in range(len(data["O(log n)"]))], data["O(log n)"], color="green")
a[0].plot([x for x in range(len(data["O(n log n)"]))], data["O(n log n)"], color="violet")
a[0].legend(["O(n)", "O(1)", "O(log n)", "O(n log n)"])

a[1].set_title("O(1) vs O(n) vs O(log n)")
a[1].plot([x for x in range(len(data["O(n)"]))], data["O(n)"], color="red")
a[1].plot([x for x in range(len(data["O(1)"]))], data["O(1)"], color="blue")
a[1].plot([x for x in range(len(data["O(log n)"]))], data["O(log n)"], color="green")
a[1].legend(["O(n)", "O(1)", "O(log n)"])
plt.show()
