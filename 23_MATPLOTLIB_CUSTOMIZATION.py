```python id="m3p8ks"
# ===================== 23_MATPLOTLIB_CUSTOMIZATION.py =====================


import matplotlib.pyplot as plt


# .........................Basic Customization.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y,
    color="blue",
    marker="o",
    linewidth=2
)

plt.title("Basic Customization")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.grid()

plt.show()


# .........................Line Color and Style.........................#

x = [1, 2, 3, 4, 5]

y = [15, 25, 20, 35, 30]

plt.plot(
    x,
    y,
    color="green",
    linestyle="--",
    linewidth=2
)

plt.title("Line Color and Style")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.show()


# .........................Marker Customization.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y,
    marker="o",
    markersize=10,
    markerfacecolor="yellow",
    markeredgecolor="black",
    markeredgewidth=2
)

plt.title("Marker Customization")

plt.show()


# .........................Line and Marker Customization.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y,
    color="purple",
    linestyle="-.",
    linewidth=3,
    marker="s",
    markersize=8,
    markerfacecolor="white",
    markeredgecolor="purple"
)

plt.title("Line and Marker")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.grid()

plt.show()


# .........................Title Customization.........................#

x = [1, 2, 3, 4, 5]

y = [20, 25, 30, 35, 40]

plt.plot(
    x,
    y,
    marker="o"
)

plt.title(
    "Sales Growth",
    fontsize=18,
    pad=15
)

plt.xlabel(
    "Month",
    fontsize=12
)

plt.ylabel
```
