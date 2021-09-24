import matplotlib.pyplot as plt

x = list(range(11))
y = [n**2 for n in x]
y2 = [n+5 for n in y]
y3 = [n+15 for n in y]

plt.bar(x, y)
plt.plot(x, y2)
plt.scatter(x, y3)
plt.savefig("simplegrapgh.png")
plt.show()
