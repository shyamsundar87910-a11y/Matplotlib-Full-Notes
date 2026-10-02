```python
# ===================== 15_MATPLOTLIB_BOX_PLOT.py =====================


import matplotlib.pyplot as plt


# .........................Simple Box Plot.........................#

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

plt.boxplot(
    marks
)

plt.title("Student Marks")

plt.ylabel("Marks")

plt.show()


# .........................Box Plot with Labels.........................#

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

plt.boxplot(
    marks
)

plt.title("Marks Distribution")

plt.xlabel("Students")

plt.ylabel("Marks")

plt.show()


# .........................Horizontal Box Plot.........................#

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

plt.boxplot(
    marks,
    vert=False
)

plt.title("Horizontal Box Plot")

plt.xlabel("Marks")

plt.show()


# .........................Box Plot with Patch Color.........................#

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

box = plt.boxplot(
    marks,
    patch_artist=True
)

for item in box["boxes"]:
    item.set_facecolor("skyblue")

plt.title("Colored Box Plot")

plt.ylabel("Marks")

plt.show()


# .........................Multiple Box Plots.........................#

python_marks = [
    55,
    60,
    65,
    70,
    75,
    80,
    85,
    90
]

sql_marks = [
    50,
    58,
    62,
    68,
    72,
    78,
    84,
    88
]

excel_marks = [
    60,
    65,
    70,
    75,
    80,
    85,
    90,
    95
]

data = [
    python_marks,
    sql_marks,
    excel_marks
]

plt.boxplot(
    data,
    labels=[
```
