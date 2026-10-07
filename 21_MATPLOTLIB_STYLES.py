```python
# ===================== 21_MATPLOTLIB_STYLES.py =====================


import matplotlib.pyplot as plt


# .........................Default Style.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y,
    marker="o"
)

plt.title("Default Style")

plt.show()


# .........................Available Styles.........................#

# Print all styles available in your Matplotlib version

print(plt.style.available)


# .........................Classic Style.........................#

plt.style.use("classic")

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y,
    marker="o"
)

plt.title("Classic Style")

plt.show()


# .........................ggplot Style.........................#

plt.style.use("ggplot")

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May"
]

sales = [
    20000,
    25000,
    30000,
    35000,
    40000
]

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title("Sales Using ggplot Style")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()


# .........................Bmh Style.........................#

plt.style.use("bmh")

x = [1, 2, 3, 4, 5]

y = [15, 25, 20, 35, 30]

plt.plot(
    x,
    y,
    marker="s"
)

plt.title("Bmh Style")

plt.show()


# .........................Dark Background Style.........................#

plt.style.use("dark_background")

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y,
    marker="o"
)

plt.title("Dark Background Style")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.show()


# .........................Fivethirtyeight Style.........................#

plt.style.use("fivethirtyeight")

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May"
]

sales = [
    20000,
    25000,
    30000,
    35000,
    40000
]

plt.bar(
    months,
    sales
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()


# .........................Style with Bar Chart.........................#

plt.style.use("ggplot")

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor"
]

sales = [
    50000,
    35000,
    20000,
    15000
]

plt.bar(
    products,
    sales
)

plt.title("Product Sales")

plt.xlabel("Products")

plt.ylabel("Sales")

plt.show()


# .........................Style with Scatter Plot.........................#

plt.style.use("bmh")

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

plt.scatter(
    hours,
    marks,
    s=100
)

plt.title("Study Hours and Marks")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.show()


# .........................Style with Histogram.........................#

plt.style.use("ggplot")

marks = [
    45,
    50,
    55,
    60,
    65,
    70,
    75,
    80,
    85,
    90,
    95
]

plt.hist(
    marks,
    bins=5,
    edgecolor="black"
)

plt.title("Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Number of Students")

plt.show()


# .........................Style with Multiple Lines.........................#

plt.style.use("fivethirtyeight")

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May"
]

sales = [
    20000,
    25000,
    30000,
    35000,
    40000
]

expenses = [
    15000,
    18000,
    22000,
    25000,
    28000
]

plt.plot(
    months,
    sales,
    marker="o",
    label="Sales"
)

plt.plot(
    months,
    expenses,
    marker="s",
    label="Expenses"
)

plt.title("Sales and Expenses")

plt.xlabel("Month")

plt.ylabel("Amount")

plt.legend()

plt.show()


# .........................Reset Default Style.........................#

plt.style.use("default")

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y,
    marker="o"
)

plt.title("Default Style Restored")

plt.show()


# .........................Important Function.........................#

# plt.style.use()
#       -> Applies a style to Matplotlib plots
#
# Example:
#
# plt.style.use("ggplot")


# .........................Common Styles.........................#

# "default"
#       -> Default Matplotlib appearance
#
# "classic"
#       -> Classic Matplotlib appearance
#
# "ggplot"
#       -> Similar to the ggplot plotting style
#
# "bmh"
#       -> Uses the Bayes Methodology style
#
# "dark_background"
#       -> Uses a dark background
#
# "fivethirtyeight"
#       -> Uses the FiveThirtyEight-inspired style


# .........................Important Notes.........................#

# 1. Styles change the overall appearance of charts.
#
# 2. A style can affect colors, gridlines,
#    fonts and backgrounds.
#
# 3. Available styles can differ by Matplotlib version.
#
# 4. Check available styles using:
#
# print(plt.style.available)
#
# 5. The selected style remains active for later plots
#    until another style is selected.


# .........................Important Syntax.........................#

# import matplotlib.pyplot as plt
#
# plt.style.use("ggplot")
#
# plt.plot(
#     x,
#     y
# )
#
# plt.title("My Plot")
#
# plt.show()
```
