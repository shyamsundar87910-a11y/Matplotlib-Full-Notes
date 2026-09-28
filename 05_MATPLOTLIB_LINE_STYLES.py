```python
# ===================== 05_MATPLOTLIB_LINE_STYLES.py =====================


import matplotlib.pyplot as plt


# .........................Simple Line Style.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y,
    linestyle="-"
)

plt.title("Solid Line")

plt.show()


# .........................Dashed Line.........................#

x = [1, 2, 3, 4, 5]

y = [20, 30, 25, 40, 35]

plt.plot(
    x,
    y,
    linestyle="--"
)

plt.title("Dashed Line")

plt.show()


# .........................Dotted Line.........................#

x = [1, 2, 3, 4, 5]

y = [15, 25, 20, 35, 30]

plt.plot(
    x,
    y,
    linestyle=":"
)

plt.title("Dotted Line")

plt.show()


# .........................Dash Dot Line.........................#

x = [1, 2, 3, 4, 5]

y = [10, 25, 20, 35, 40]

plt.plot(
    x,
    y,
    linestyle="-."
)

plt.title("Dash Dot Line")

plt.show()


# .........................Short Style Symbols.........................#

x = [1, 2, 3, 4, 5]

y = [20, 35, 25, 40, 45]

plt.plot(
    x,
    y,
    ls="--"
)

plt.title("Short Line Style")

plt.show()


# .........................Line Width.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 30, 25, 40]

plt.plot(
    x,
    y,
    linestyle="-",
    linewidth=3
)

plt.title("Line Width")

plt.show()


# .........................Thin Line.........................#

x = [1, 2, 3, 4, 5]

y = [15, 25, 20, 35, 45]

plt.plot(
    x,
    y,
    linewidth=1
)

plt.title("Thin Line")

plt.show()


# .........................Multiple Line Styles.........................#

x = [1, 2, 3, 4, 5]

sales = [20, 30, 25, 40, 35]

expenses = [15, 20, 18, 25, 22]

profit = [5, 10, 7, 15, 13]

plt.plot(
    x,
    sales,
    linestyle="-"
)

plt.plot(
    x,
    expenses,
    linestyle="--"
)

plt.plot(
    x,
    profit,
    linestyle=":"
)

plt.title("Sales, Expenses and Profit")

plt.xlabel("Month")

plt.ylabel("Amount")

plt.show()


# .........................Line Style with Marker.........................#

x = [1, 2, 3, 4, 5]

y = [10, 25, 20, 35, 45]

plt.plot(
    x,
    y,
    linestyle="--",
    marker="o"
)

plt.title("Dashed Line with Marker")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.show()


# .........................Line Width with Marker.........................#

x = [1, 2, 3, 4, 5]

y = [20, 30, 25, 40, 50]

plt.plot(
    x,
    y,
    linestyle="-",
    linewidth=3,
    marker="o"
)

plt.title("Line Width and Marker")

plt.show()


# .........................Sales Example.........................#

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
    28000,
    35000
]

plt.plot(
    months,
    sales,
    linestyle="--",
    linewidth=2,
    marker="o"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid()

plt.show()


# .........................Student Marks Example.........................#

students = [
    "Aman",
    "Rahul",
    "Priya",
    "Sneha",
    "Rohit"
]

marks = [
    65,
    72,
    88,
    78,
    92
]

plt.plot(
    students,
    marks,
    linestyle="-.",
    linewidth=2,
    marker="o"
)

plt.title("Student Marks")

plt.xlabel("Student")

plt.ylabel("Marks")

plt.grid()

plt.show()


# .........................Common Line Styles.........................#

# "-"   -> Solid line
# "--"  -> Dashed line
# ":"   -> Dotted line
# "-."  -> Dash-dot line


# .........................Line Style Parameter.........................#

# linestyle="--"
#
# Short form:
#
# ls="--"


# .........................Line Width Parameter.........................#

# linewidth=2
#
# Short form:
#
# lw=2


# .........................Important Syntax.........................#

# plt.plot(
#     x,
#     y,
#     linestyle="--",
#     linewidth=2,
#     marker="o"
# )
```
