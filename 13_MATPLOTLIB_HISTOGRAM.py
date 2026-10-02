```python id="f5f1r2"
# ===================== 13_MATPLOTLIB_HISTOGRAM.py =====================


import matplotlib.pyplot as plt


# .........................Simple Histogram.........................#

marks = [
    45,
    50,
    55,
    60,
    65,
    70,
    72,
    75,
    80,
    85,
    90,
    95
]

plt.hist(
    marks
)

plt.title("Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Number of Students")

plt.show()


# .........................Histogram with Bins.........................#

marks = [
    45,
    50,
    55,
    60,
    65,
    70,
    72,
    75,
    80,
    85,
    90,
    95
]

plt.hist(
    marks,
    bins=5
)

plt.title("Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Students")

plt.show()


# .........................Histogram with More Bins.........................#

marks = [
    45,
    50,
    55,
    60,
    65,
    70,
    72,
    75,
    80,
    85,
    90,
    95
]

plt.hist(
    marks,
    bins=10
)

plt.title("Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Students")

plt.show()


# .........................Histogram with Color.........................#

marks = [
    45,
    50,
    55,
    60,
    65,
    70,
    72,
    75,
    80,
    85,
    90,
    95
]

plt.hist(
    marks,
    bins=5,
    color="skyblue"
)

plt.title("Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Students")

plt.show()


# .........................Histogram with Edge Color.........................#

marks = [
    45,
    50,
    55,
    60,
    65,
    70,
    72,
    75,
    80,
    85,
    90,
    95
]

plt.hist(
    marks,
    bins=5,
    color="lightgreen",
    edgecolor="black"
)

plt.title("Marks Distribution")

plt.show()


# .........................Histogram with Transparency.........................#

marks = [
    45,
    50,
    55,
    60,
    65,
    70,
    72,
    75,
    80,
    85,
    90,
    95
]

plt.hist(
    marks,
    bins=5,
    alpha=0.7
)

plt.title("Marks Distribution")

plt.show()


# .........................Histogram with Grid.........................#

marks = [
    45,
    50,
    55,
    60,
    65,
    70,
    72,
    75,
    80,
    85,
    90,
    95
]

plt.hist(
    marks,
    bins=5,
    color="orange",
    edgecolor="black"
)

plt.title("Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Students")

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.6
)

plt.show()


# .........................Student Marks Example.........................#

marks = [
    45,
    55,
    60,
    62,
    65,
    68,
    70,
    72,
    75,
    78,
    80,
    82,
    85,
    88,
    90,
    92,
    95
]

plt.hist(
    marks,
    bins=5,
    color="steelblue",
    edgecolor="black"
)

plt.title("Student Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Number of Students")

plt.grid(
    axis="y"
)

plt.show()


# ...........
```
