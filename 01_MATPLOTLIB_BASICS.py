```python
# ===================== 01_MATPLOTLIB_BASICS.py =====================


import matplotlib.pyplot as plt


# .........................Introduction.........................#

# Matplotlib is a Python library used for data visualization.
# It helps us create different types of charts and graphs.


# .........................Simple Line Plot.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 30, 40, 50]

plt.plot(x, y)

plt.show()


# .........................Line Plot with Title.........................#

x = [1, 2, 3, 4, 5]

y = [10, 15, 25, 20, 30]

plt.plot(x, y)

plt.title("Simple Line Plot")

plt.show()


# .........................X-axis and Y-axis Labels.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 30, 40, 50]

plt.plot(x, y)

plt.title("Sales Data")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()


# .........................Line Plot with Marker.........................#

x = [1, 2, 3, 4, 5]

y = [20, 35, 30, 45, 50]

plt.plot(
    x,
    y,
    marker="o"
)

plt.title("Sales Growth")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()


# .........................Different X Values.........................#

months = [
    "January",
    "February",
    "March",
    "April",
    "May"
]

sales = [
    20000,
    25000,
    22000,
    30000,
    35000
]

plt.plot(
    months,
    sales
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()


# .........................Simple Bar Chart.........................#

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

plt.xlabel("Product")

plt.ylabel("Sales")

plt.show()


# .........................Simple Pie Chart.........................#

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor"
]

sales = [
    50,
    30,
    15,
    5
]

plt.pie(
    sales,
    labels=products
)

plt.title("Sales Distribution")

plt.show()


# .........................Simple Scatter Plot.........................#

age = [
    18,
    19,
    20,
    21,
    22
]

marks = [
    65,
    70,
    75,
    82,
    90
]

plt.scatter(
    age,
    marks
)

plt.title("Age vs Marks")

plt.xlabel("Age")

plt.ylabel("Marks")

plt.show()


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


# .........................Using Figure.........................#

plt.figure(
    figsize=(8, 5)
)

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y
)

plt.title("Figure Example")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.show()


# .........................Multiple Lines.........................#

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May"
]

sales_2025 = [
    20000,
    25000,
    30000,
    28000,
    35000
]

sales_2026 = [
    25000,
    28000,
    32000,
    35000,
    40000
]

plt.plot(
    months,
    sales_2025
)

plt.plot(
    months,
    sales_2026
)

plt.title("Sales Comparison")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()


# .........................Basic Matplotlib Functions.........................#

# plt.plot()      -> Line chart
# plt.bar()       -> Bar chart
# plt.pie()       -> Pie chart
# plt.scatter()   -> Scatter plot
# plt.hist()      -> Histogram
# plt.title()     -> Chart title
# plt.xlabel()    -> X-axis label
# plt.ylabel()    -> Y-axis label
# plt.show()      -> Display chart
# plt.figure()    -> Create a figure
```
