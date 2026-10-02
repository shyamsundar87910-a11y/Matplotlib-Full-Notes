```python
# ===================== 14_MATPLOTLIB_SCATTER_PLOT.py =====================


import matplotlib.pyplot as plt


# .........................Simple Scatter Plot.........................#

x = [
    1,
    2,
    3,
    4,
    5
]

y = [
    10,
    20,
    15,
    30,
    25
]

plt.scatter(
    x,
    y
)

plt.title("Simple Scatter Plot")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.show()


# .........................Scatter Plot with Color.........................#

x = [
    1,
    2,
    3,
    4,
    5
]

y = [
    10,
    20,
    15,
    30,
    25
]

plt.scatter(
    x,
    y,
    color="blue"
)

plt.title("Scatter Plot")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.show()


# .........................Scatter Plot with Marker Size.........................#

x = [
    1,
    2,
    3,
    4,
    5
]

y = [
    10,
    20,
    15,
    30,
    25
]

plt.scatter(
    x,
    y,
    s=100
)

plt.title("Scatter Plot with Marker Size")

plt.show()


# .........................Different Marker Sizes.........................#

x = [
    1,
    2,
    3,
    4,
    5
]

y = [
    10,
    20,
    15,
    30,
    25
]

sizes = [
    50,
    100,
    150,
    200,
    250
]

plt.scatter(
    x,
    y,
    s=sizes
)

plt.title("Different Marker Sizes")

plt.show()


# .........................Scatter Plot with Transparency.........................#

x = [
    1,
    2,
    3,
    4,
    5
]

y = [
    10,
    20,
    15,
    30,
    25
]

plt.scatter(
    x,
    y,
    alpha=0.5
)

plt.title("Transparent Scatter Plot")

plt.show()


# .........................Scatter Plot with Edge Color.........................#

x = [
    1,
    2,
    3,
    4,
    5
]

y = [
    10,
    20,
    15,
    30,
    25
]

plt.scatter(
    x,
    y,
    color="skyblue",
    edgecolor="black"
)

plt.title("Scatter Plot with Edge")

plt.show()


# .........................Scatter Plot with Grid.........................#

x = [
    1,
    2,
    3,
    4,
    5,
    6
]

y = [
    20,
    35,
    25,
    40,
    30,
    50
]

plt.scatter(
    x,
    y,
    color="green"
)

plt.title("Scatter Plot")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.grid()

plt.show()


# .........................Study Hours and Marks.........................#

hours = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8
]

marks = [
    45,
    50,
    55,
    60,
    68,
    72,
    80,
    90
]

plt.scatter(
    hours,
    marks,
    color="purple",
    s=80
)

plt.title("Study Hours and Marks")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.grid()

plt.show()


# .........................Age and Salary Example.........................#

age = [
    20,
    22,
    24,
    26,
    28,
    30,
    32,
    35
]

salary = [
    18000,
    22000,
    25000,
    30000,
    35000,
    40000,
    45000,
    50000
]

plt.scatter(
    age,
    salary,
    color="orange",
    s=100
)

plt.title("Age and Salary")

plt.xlabel("Age")

plt.ylabel("Salary")

plt.show()


# .........................Two Scatter Plots.........................#

python_hours = [
    1,
    2,
    3,
    4,
    5,
    6
]

python_marks = [
    45,
    50,
    60,
    65,
    75,
    85
]

sql_hours = [
    1,
    2,
    3,
    4,
    5,
    6
]

sql_marks = [
    40,
    48,
    55,
    62,
    70,
    80
]

plt.scatter(
    python_hours,
    python_marks,
    color="blue",
    label="Python"
)

plt.scatter(
    sql_hours,
    sql_marks,
    color="red",
    label="SQL"
)

plt.title("Python and SQL Performance")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.legend()

plt.grid()

plt.show()


# .........................Scatter Plot with Different Sizes and Colors.........................#

x = [
    1,
    2,
    3,
    4,
    5
]

y = [
    20,
    30,
    25,
    40,
    35
]

sizes = [
    50,
    100,
    150,
    200,
    250
]

colors = [
    "red",
    "blue",
    "green",
    "orange",
    "purple"
]

plt.scatter(
    x,
    y,
    s=sizes,
    c=colors
)

plt.title("Different Sizes and Colors")

plt.show()


# .........................Sales and Advertising Example.........................#

advertising = [
    10,
    20,
    30,
    40,
    50,
    60,
    70
]

sales = [
    15,
    22,
    30,
    38,
    45,
    52,
    65
]

plt.scatter(
    advertising,
    sales,
    color="teal",
    s=100
)

plt.title("Advertising and Sales")

plt.xlabel("Advertising Cost")

plt.ylabel("Sales")

plt.grid()

plt.show()


# .........................Scatter Plot with Figure Size.........................#

hours = [
    1,
    2,
    3,
    4,
    5,
    6
]

marks = [
    45,
    50,
    60,
    65,
    75,
    85
]

plt.figure(
    figsize=(8, 5)
)

plt.scatter(
    hours,
    marks,
    color="green",
    s=100
)

plt.title("Study Hours and Marks")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.show()


# .........................Important Functions.........................#

# plt.scatter()
#       -> Creates a scatter plot
#
# s
#       -> Changes marker size
#
# color
#       -> Changes marker color
#
# c
#       -> Can be used for multiple colors
#
# alpha
#       -> Controls transparency
#
# edgecolor
#       -> Changes marker border color
#
# plt.legend()
#       -> Displays labels
#
# plt.grid()
#       -> Adds grid lines


# .........................What Scatter Plot Shows.........................#

# Scatter plot is mainly used to:
#
# 1. Find relationships between variables
# 2. Find patterns
# 3. Compare numerical data
# 4. Identify possible outliers
# 5. Understand positive or negative relationships


# .........................Important Syntax.........................#

# plt.scatter(
#     x,
#     y
# )
#
# plt.scatter(
#     x,
#     y,
#     s=100,
#     color="blue",
#     alpha=0.5
# )
```
```python
# ===================== 14_MATPLOTLIB_SCATTER_PLOT.py =====================


import matplotlib.pyplot as plt


# .........................Simple Scatter Plot.........................#

x = [
    1,
    2,
    3,
    4,
    5
]

y = [
    10,
    20,
    15,
    30,
    25
]

plt.scatter(
    x,
    y
)

plt.title("Simple Scatter Plot")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.show()


# .........................Scatter Plot with Color.........................#

x = [
    1,
    2,
    3,
    4,
    5
]

y = [
    10,
    20,
    15,
    30,
    25
]

plt.scatter(
    x,
    y,
    color="blue"
)

plt.title("Scatter Plot")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.show()


# .........................Scatter Plot with Marker Size.........................#

x = [
    1,
    2,
    3,
    4,
    5
]

y = [
    10,
    20,
    15,
    30,
    25
]

plt.scatter(
    x,
    y,
    s=100
)

plt.title("Scatter Plot with Marker Size")

plt.show()


# .........................Different Marker Sizes.........................#

x = [
    1,
    2,
    3,
    4,
    5
]

y = [
    10,
    20,
    15,
    30,
    25
]

sizes = [
    50,
    100,
    150,
    200,
    250
]

plt.scatter(
    x,
    y,
    s=sizes
)

plt.title("Different Marker Sizes")

plt.show()


# .........................Scatter Plot with Transparency.........................#

x = [
    1,
    2,
    3,
    4,
    5
]

y = [
    10,
    20,
    15,
    30,
    25
]

plt.scatter(
    x,
    y,
    alpha=0.5
)

plt.title("Transparent Scatter Plot")

plt.show()


# .........................Scatter Plot with Edge Color.........................#

x = [
    1,
    2,
    3,
    4,
    5
]

y = [
    10,
    20,
    15,
    30,
    25
]

plt.scatter(
    x,
    y,
    color="skyblue",
    edgecolor="black"
)

plt.title("Scatter Plot with Edge")

plt.show()


# .........................Scatter Plot with Grid.........................#

x = [
    1,
    2,
    3,
    4,
    5,
    6
]

y = [
    20,
    35,
    25,
    40,
    30,
    50
]

plt.scatter(
    x,
    y,
    color="green"
)

plt.title("Scatter Plot")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.grid()

plt.show()


# .........................Study Hours and Marks.........................#

hours = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8
]

marks = [
    45,
    50,
    55,
    60,
    68,
    72,
    80,
    90
]

plt.scatter(
    hours,
    marks,
    color="purple",
    s=80
)

plt.title("Study Hours and Marks")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.grid()

plt.show()


# .........................Age and Salary Example.........................#

age = [
    20,
    22,
    24,
    26,
    28,
    30,
    32,
    35
]

salary = [
    18000,
    22000,
    25000,
    30000,
    35000,
    40000,
    45000,
    50000
]

plt.scatter(
    age,
    salary,
    color="orange",
    s=100
)

plt.title("Age and Salary")

plt.xlabel("Age")

plt.ylabel("Salary")

plt.show()


# .........................Two Scatter Plots.........................#

python_hours = [
    1,
    2,
    3,
    4,
    5,
    6
]

python_marks = [
    45,
    50,
    60,
    65,
    75,
    85
]

sql_hours = [
    1,
    2,
    3,
    4,
    5,
    6
]

sql_marks = [
    40,
    48,
    55,
    62,
    70,
    80
]

plt.scatter(
    python_hours,
    python_marks,
    color="blue",
    label="Python"
)

plt.scatter(
    sql_hours,
    sql_marks,
    color="red",
    label="SQL"
)

plt.title("Python and SQL Performance")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.legend()

plt.grid()

plt.show()


# .........................Scatter Plot with Different Sizes and Colors.........................#

x = [
    1,
    2,
    3,
    4,
    5
]

y = [
    20,
    30,
    25,
    40,
    35
]

sizes = [
    50,
    100,
    150,
    200,
    250
]

colors = [
    "red",
    "blue",
    "green",
    "orange",
    "purple"
]

plt.scatter(
    x,
    y,
    s=sizes,
    c=colors
)

plt.title("Different Sizes and Colors")

plt.show()


# .........................Sales and Advertising Example.........................#

advertising = [
    10,
    20,
    30,
    40,
    50,
    60,
    70
]

sales = [
    15,
    22,
    30,
    38,
    45,
    52,
    65
]

plt.scatter(
    advertising,
    sales,
    color="teal",
    s=100
)

plt.title("Advertising and Sales")

plt.xlabel("Advertising Cost")

plt.ylabel("Sales")

plt.grid()

plt.show()


# .........................Scatter Plot with Figure Size.........................#

hours = [
    1,
    2,
    3,
    4,
    5,
    6
]

marks = [
    45,
    50,
    60,
    65,
    75,
    85
]

plt.figure(
    figsize=(8, 5)
)

plt.scatter(
    hours,
    marks,
    color="green",
    s=100
)

plt.title("Study Hours and Marks")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.show()


# .........................Important Functions.........................#

# plt.scatter()
#       -> Creates a scatter plot
#
# s
#       -> Changes marker size
#
# color
#       -> Changes marker color
#
# c
#       -> Can be used for multiple colors
#
# alpha
#       -> Controls transparency
#
# edgecolor
#       -> Changes marker border color
#
# plt.legend()
#       -> Displays labels
#
# plt.grid()
#       -> Adds grid lines


# .........................What Scatter Plot Shows.........................#

# Scatter plot is mainly used to:
#
# 1. Find relationships between variables
# 2. Find patterns
# 3. Compare numerical data
# 4. Identify possible outliers
# 5. Understand positive or negative relationships


# .........................Important Syntax.........................#

# plt.scatter(
#     x,
#     y
# )
#
# plt.scatter(
#     x,
#     y,
#     s=100,
#     color="blue",
#     alpha=0.5
# )
```
