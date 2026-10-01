```python id="xq2m8v"
# ===================== 07_MATPLOTLIB_LEGEND.py =====================


import matplotlib.pyplot as plt


# .........................Simple Legend.........................#

x = [1, 2, 3, 4, 5]

sales = [10, 20, 30, 25, 40]

plt.plot(
    x,
    sales,
    label="Sales"
)

plt.title("Sales Data")

plt.legend()

plt.show()


# .........................Multiple Lines with Legend.........................#

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
    label="Sales"
)

plt.plot(
    months,
    expenses,
    label="Expenses"
)

plt.title("Sales and Expenses")

plt.xlabel("Month")

plt.ylabel("Amount")

plt.legend()

plt.show()


# .........................Three Lines with Legend.........................#

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
    18000,
    25000,
    28000
]

profit = [
    5000,
    10000,
    12000,
    10000,
    12000
]

plt.plot(
    months,
    sales,
    label="Sales"
)

plt.plot(
    months,
    expenses,
    label="Expenses"
)

plt.plot(
    months,
    profit,
    label="Profit"
)

plt.title("Business Analysis")

plt.xlabel("Month")

plt.ylabel("Amount")

plt.legend()

plt.show()


# .........................Legend Position - Upper Left.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y,
    label="Data"
)

plt.legend(
    loc="upper left"
)

plt.show()


# .........................Legend Position - Upper Right.........................#

x = [1, 2, 3, 4, 5]

y = [15, 25, 20, 35, 30]

plt.plot(
    x,
    y,
    label="Data"
)

plt.legend(
    loc="upper right"
)

plt.show()


# .........................Legend Position - Lower Left.........................#

x = [1, 2, 3, 4, 5]

y = [20, 30, 25, 40, 35]

plt.plot(
    x,
    y,
    label="Data"
)

plt.legend(
    loc="lower left"
)

plt.show()


# .........................Legend Position - Lower Right.........................#

x = [1, 2, 3, 4, 5]

y = [10, 25, 20, 35, 45]

plt.plot(
    x,
    y,
    label="Data"
)

plt.legend(
    loc="lower right"
)

plt.show()


# .........................Legend Position - Center.........................#

x = [1, 2, 3, 4, 5]

y = [20, 35, 25, 40, 50]

plt.plot(
    x,
    y,
    label="Data"
)

plt.legend(
    loc="center"
)

plt.show()


# .........................Legend with Font Size.........................#

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
    label="Sales"
)

plt.plot(
    months,
    expenses,
    label="Expenses"
)

plt.legend(
    fontsize=10
)

plt.title("Sales and Expenses")

plt.show()


# .........................Legend with Title.........................#

x = [1, 2, 3, 4, 5]

sales = [20, 30, 25, 40, 35]

expenses = [15, 20, 18, 25, 22]

plt.plot(
    x,
    sales,
    label="Sales"
)

plt.plot(
    x,
    expenses,
    label="Expenses"
)

plt.legend(
    title="Data Type"
)

plt.title("Business Data")

plt.show()


# .........................Legend Outside Plot.........................#

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
    label="Sales"
)

plt.plot(
    months,
    expenses,
    label="Expenses"
)

plt.legend(
    loc="upper left",
    bbox_to_anchor=(1, 1)
)

plt.title("Sales and Expenses")

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

attendance = [
    80,
    85,
    95,
    75,
    90
]

plt.plot(
    students,
    marks,
    marker="o",
    label="Marks"
)

plt.plot(
    students,
    attendance,
    marker="o",
    label="Attendance"
)

plt.title("Student Performance")

plt.xlabel("Students")

plt.ylabel("Value")

plt.legend()

plt.grid()

plt.show()


# .........................Bar Chart with Legend..................
```
