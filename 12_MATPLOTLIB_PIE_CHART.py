```python
# ===================== 12_MATPLOTLIB_PIE_CHART.py =====================


import matplotlib.pyplot as plt


# .........................Simple Pie Chart.........................#

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor"
]

sales = [
    40,
    30,
    20,
    10
]

plt.pie(
    sales,
    labels=products
)

plt.title("Product Sales Distribution")

plt.show()


# .........................Pie Chart with Percentages.........................#

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor"
]

sales = [
    40,
    30,
    20,
    10
]

plt.pie(
    sales,
    labels=products,
    autopct="%1.1f%%"
)

plt.title("Product Sales")

plt.show()


# .........................Pie Chart with Colors.........................#

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor"
]

sales = [
    40,
    30,
    20,
    10
]

colors = [
    "red",
    "blue",
    "green",
    "orange"
]

plt.pie(
    sales,
    labels=products,
    colors=colors
)

plt.title("Product Sales")

plt.show()


# .........................Pie Chart with Percentages and Colors.........................#

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor"
]

sales = [
    40,
    30,
    20,
    10
]

colors = [
    "red",
    "blue",
    "green",
    "orange"
]

plt.pie(
    sales,
    labels=products,
    colors=colors,
    autopct="%1.1f%%"
)

plt.title("Product Sales Distribution")

plt.show()


# .........................Explode Pie Chart.........................#

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor"
]

sales = [
    40,
    30,
    20,
    10
]

explode = [
    0.1,
    0,
    0,
    0
]

plt.pie(
    sales,
    labels=products,
    explode=explode,
    autopct="%1.1f%%"
)

plt.title("Product Sales")

plt.show()


# .........................Explode Multiple Slices.........................#

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor"
]

sales = [
    40,
    30,
    20,
    10
]

explode = [
    0.1,
    0,
    0.05,
    0
]

plt.pie(
    sales,
    labels=products,
    explode=explode,
    autopct="%1.1f%%"
)

plt.title("Product Sales")

plt.show()


# ..........
```
