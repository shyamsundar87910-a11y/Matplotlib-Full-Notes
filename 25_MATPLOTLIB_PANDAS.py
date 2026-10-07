```python
# ===================== 25_MATPLOTLIB_PANDAS.py =====================


import pandas as pd

import matplotlib.pyplot as plt


# .........................Create DataFrame.........................#

data = {
    "Month": [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May"
    ],

    "Sales": [
        20000,
        25000,
        30000,
        35000,
        40000
    ]
}

df = pd.DataFrame(
    data
)

print(df)


# .........................Pandas DataFrame Line Plot.........................#

plt.plot(
    df["Month"],
    df["Sales"],
    marker="o"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()


# .........................DataFrame with Multiple Columns.........................#

data = {
    "Month": [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May"
    ],

    "Sales": [
        20000,
        25000,
        30000,
        35000,
        40000
    ],

    "Expenses": [
        15000,
        18000,
        22000,
        25000,
        28000
    ]
}

df = pd.DataFrame(
    data
)

plt.plot(
    df["Month"],
    df["Sales"],
    marker="o",
    label="Sales"
)

plt.plot(
    df["Month"],
    df["Expenses"],
    marker="s",
    label="Expenses"
)

plt.title("Sales and Expenses")

plt.xlabel("Month")

plt.ylabel("Amount")

plt.legend()

plt.grid()

plt.show()


# .........................Pandas Bar Chart.........................#

data = {
    "Product": [
        "Laptop",
        "Mobile",
        "Tablet",
        "Monitor"
    ],

    "Sales": [
        50000,
        35000,
        20000,
        15000
    ]
}

df = pd.DataFrame(
    data
)

plt.bar(
    df["Product"],
    df["Sales"]
)

plt.title("Product Sales")

plt.xlabel("Product")

plt.ylabel("Sales")

plt.show()


# .........................Pandas Horizontal Bar Chart.........................#

plt.barh(
    df["Product"],
    df["Sales"]
)

plt.title("Product Sales")

plt.xlabel("Sales")

plt.ylabel("Product")

plt.show()


# .........................Pandas Scatter Plot.........................#

data = {
    "Study_Hours": [
        1,
        2,
        3,
        4,
        5,
        6
    ],

    "Marks": [
        45,
        50,
        60,
        65,
        75,
        85
    ]
}

df = pd.DataFrame(
    data
)

plt.scatter(
    df["Study_Hours"],
    df["Marks"],
    s=100
)

plt.title("Study Hours and Marks")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.grid()

plt.show()


# .........................Pandas Histogram.........................#

data = {
    "Marks": [
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
}

df = pd.DataFrame(
    data
)

plt.hist(
    df["Marks"],
    bins=5,
    edgecolor="black"
)

plt.title("Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Students")

plt.show()


# .........................Pandas Pie Chart.........................#

data = {
    "Subject": [
        "Python",
        "SQL",
        "Excel",
        "Power BI"
    ],

    "Hours": [
        30,
        25,
        20,
        25
    ]
}

df = pd.DataFrame(
    data
)

plt.pie(
    df["Hours"],
    labels=df["Subject"],
    autopct="%1.1f%%"
)

plt.title("Study Time Distribution")

plt.show()


# .........................DataFrame with GroupBy.........................#

data = {
    "Department": [
        "IT",
        "HR",
        "IT",
        "Sales",
        "HR",
        "Sales"
    ],

    "Employee": [
        "Aman",
        "Rahul",
        "Priya",
        "Sneha",
        "Rohit",
        "Neha"
    ],

    "Salary": [
        50000,
        40000,
        55000,
        45000,
        42000,
        48000
    ]
}

df = pd.DataFrame(
    data
)

department_salary = df.groupby(
    "Department"
)["Salary"].mean()

print(department_salary)

plt.bar(
    department_salary.index,
    department_salary.values
)

plt.title("Average Salary by Department")

plt.xlabel("Department")

plt.ylabel("Average Salary")

plt.show()


# .........................Pandas Data Analysis Chart.........................#

data = {
    "Product": [
        "Laptop",
        "Mobile",
        "Tablet",
        "Monitor",
        "Keyboard"
    ],

    "Sales": [
        50000,
        35000,
        20000,
        15000,
        10000
    ]
}

df = pd.DataFrame(
    data
)

highest_product = df.loc[
    df["Sales"].idxmax()
]

print("Highest Sales Product:")

print(highest_product)

plt.bar(
    df["Product"],
    df["Sales"]
)

plt.title("Product Sales Analysis")

plt.xlabel("Product")

plt.ylabel("Sales")

plt.xticks(
    rotation=45
)

plt.show()


# .........................Add Values to Bar Chart.........................#

data = {
    "Product": [
        "Laptop",
        "Mobile",
        "Tablet",
        "Monitor"
    ],

    "Sales": [
        50000,
        35000,
        20000,
        15000
    ]
}

df = pd.DataFrame(
    data
)

plt.bar(
    df["Product"],
    df["Sales"]
)

for i in range(len(df)):
    plt.text(
        i,
        df["Sales"][i],
        str(df["Sales"][i]),
        ha="center",
        va="bottom"
    )

plt.title("Product Sales")

plt.xlabel("Product")

plt.ylabel("Sales")

plt.show()


# .........................Pandas Filtering and Plotting.........................#

data = {
    "Product": [
        "Laptop",
        "Mobile",
        "Tablet",
        "Monitor",
        "Keyboard"
    ],

    "Sales": [
        50000,
        3
```
