```python
# ===================== 22_MATPLOTLIB_SAVEFIG.py =====================


import matplotlib.pyplot as plt


# .........................Basic Save Figure.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y,
    marker="o"
)

plt.title("Basic Plot")

plt.savefig(
    "basic_plot.png"
)

plt.show()


# .........................Save as PNG.........................#

x = [1, 2, 3, 4, 5]

y = [15, 25, 20, 35, 30]

plt.plot(
    x,
    y,
    marker="o"
)

plt.title("PNG Plot")

plt.savefig(
    "sales_plot.png"
)

plt.show()


# .........................Save as JPG.........................#

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

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.savefig(
    "monthly_sales.jpg"
)

plt.show()


# .........................Save as PDF.........................#

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

plt.savefig(
    "product_sales.pdf"
)

plt.show()


# .........................Custom File Name.........................#

x = [1, 2, 3, 4, 5]

y = [20, 30, 25, 40, 35]

plt.plot(
    x,
    y,
    marker="o"
)

plt.title("Custom File Name")

plt.savefig(
    "my_matplotlib_chart.png"
)

plt.show()


# .........................Custom Figure Size.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.figure(
    figsize=(10, 6)
)

plt.plot(
    x,
    y,
    marker="o"
)

plt.title("Large Saved Figure")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.savefig(
    "large_chart.png"
)

plt.show()


# .........................High Resolution Image.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 25, 30, 40]

plt.plot(
    x,
    y,
    marker="o"
)

plt.title("High Resolution Chart")

plt.savefig(
    "high_resolution_chart.png",
    dpi=300
)

plt.show()


# .........................Transparent Background.........................#

x = [1, 2, 3, 4, 5]

y = [15, 20, 30, 25, 35]

plt.plot(
    x,
    y,
    marker="o"
)

plt.title("Transparent Background")

plt.savefig(
    "transparent_chart.png",
    transparent=True
)

plt.show()


# .........................Save with Tight Layout.........................#

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
    30000,
    35000,
    40000
]

plt.figure(
    figsize=(10, 5)
)

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.tight_layout()

plt.savefig(
    "monthly_sales_tight.png"
)

plt.show()


# .........................Save Bar Chart.........................#

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

plt.bar(
    students,
    marks
)

plt.title("Student Performance")

plt.xlabel("Students")

plt.ylabel("Marks")

plt.ylim(
    0,
    100
)

plt.savefig(
    "student_performance.png"
)

plt.show()


# .........................Save Pie Chart.........................#

subjects = [
    "Python",
    "SQL",
    "Excel",
    "Power BI"
]

study_hours = [
    30,
    25,
    20,
    25
]

plt.figure(
    figsize=(7, 7)
)

plt.pie(
    study_hours,
    labels=subjects,
    autopct="%1.1f%%"
)

plt.title("Study Time Distribution")

plt.savefig(
    "study_distribution.png"
)

plt.show()


# .........................Save Scatter Plot.........................#

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
    marks
)

plt.title("Study Hours and Marks")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.grid()

plt.savefig(
    "study_marks.png"
)

plt.show()


# .........................Save Histogram.........................#

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

plt.ylabel("Students")

plt.savefig(
    "marks_distribution.png"
)

plt.show()


# .........................Save Multiple Lines.........................#

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

plt.grid()

plt.savefig(
    "sales_expenses.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# .........................Important Function.........................#

# plt.savefig()
#       -> Saves the current figure as an image or file


# .........................Common File Formats.........................#

# PNG
#       -> .png
#
# JPG
#       -> .jpg
#
# PDF
#       -> .pdf
#
# SVG
#       -> .svg


# .........................DPI.........................#

# dpi
#       -> Controls image resolution
#
# Example:
#
# plt.savefig(
#     "chart.png",
#     dpi=300
# )
#
# Higher DPI
#       -> Better image quality


# .........................Transparent Background.........................#

# transparent=True
#       -> Saves the figure with a transparent background
#
# Example:
#
# plt.savefig(
#     "chart.png",
#     transparent=True
# )


# .........................Tight Bounding Box.........................#

# bbox_inches="tight"
#       -> Removes unnecessary extra space around the figure
#
# Example:
#
# plt.savefig(
#     "chart.png",
#     bbox_inches="tight"
# )


# .........................Important Syntax.........................#

# plt.plot(
#     x,
#     y
# )
#
# plt.title("My Chart")
#
# plt.savefig(
#     "my_chart.png"
# )
#
# plt.show()


# .........................Best Practice.........................#

# plt.tight_layout()
#
# plt.savefig(
#     "chart.png",
#     dpi=300,
#     bbox_inches="tight"
# )
#
# plt.show()
```
