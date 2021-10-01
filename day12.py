# import matplotlib.pyplot as plt

# x = list(range(11))
# y = [n**2 for n in x]
# y2 = [n+5 for n in y]
# y3 = [n+15 for n in y]

# plt.bar(x, y)
# plt.plot(x, y2)
# plt.scatter(x, y3)
# plt.savefig("simplegrapgh.png")
# plt.show()

import random
from collections import Counter

six_dices = [random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) +
             random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) for n in range(100_000)]
top_values = Counter(six_dices)
print(top_values)
