import json
import matplotlib.pyplot as plt

with open("time.json", "r") as f:
    data = json.load(f)

plt.plot([x for x in range(len(data["O(n)"]))], data["O(n)"], color="red")
plt.plot([x for x in range(len(data["O(1)"]))], data["O(1)"], color="blue")
plt.plot([x for x in range(len(data["O(log n)"]))], data["O(log n)"], color="green")
plt.plot([x for x in range(len(data["O(n log n)"]))], data["O(n log n)"], color="violet")
plt.legend(["O(n)", "O(1)", "O(log n)", "O(n log n)"])
plt.show()
