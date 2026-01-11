'''
#Question No.1
import numpy as np  # library imported for arrays

#Creating two 2D Arrays
arr1 = np.array([[4, 15, 33],[44, 15, 36]])
arr2 = np.array([[61, 53, 42],[32, 22, 11]])

#Operations
add = np.add(arr1, arr2)
subtract = np.subtract(arr1, arr2)
multiply = np.multiply(arr1, arr2)
divide = np.divide(arr1, arr2)

#Output
print("Array No.1:\n", arr1)
print("\nArray No.2:\n", arr2)
print ("\nOperations Elementwise:")
print("\nAddition:\n", add)
print("\nSubtraction:\n", subtract)
print("\nMultiplication:\n", multiply)
print("\nDivision:\n", divide)

'''

'''
#Question No.2
import numpy as np  # library imported for numerical operations

#Creating a NumPy array
numbers = np.array([10, 20, 30, 40, 50, 60])

#Calculations
avg = np.mean(numbers)
mid = np.median(numbers)
std = np.std(numbers)
var = np.var(numbers)
percentile50 = np.percentile(numbers, 50)

#Output
print("\nNumbers:", numbers)
print("\nMean (average):", avg)
print("\nMedian (middle value):", mid)
print("\nStandard Deviation:", std)
print("\nVariance:", var)
print("\n50th Percentile:", percentile50)

'''

'''
#Question No.3
import pandas as pd  # library imported for tables

#Creating a DataFrame
employees = {
    'Employee': ['Abdullah', 'Hamza', 'Ahmed', 'Bilal'],
    'AgeYears': [15, 35, 28, 43],
    'MonthlySalary': [50000, 60000, 55000, 70000]
}
employee_df = pd.DataFrame(employees)
#Main table
print("\nOriginal Employee Table:\n")
print(employee_df)

#Column Addition for bonus
employee_df['Bonus10Percent'] = employee_df['MonthlySalary'] * 0.10
print("\nEmployee Table After Adding Bonus:\n")
print(employee_df)

#Removing Age column
employee_df = employee_df.drop(columns=['AgeYears'])
print("\nEmployee Table After Removing Age Column:\n")
print(employee_df)
print("\n")

'''

'''
Question No.4
import pandas as pd # library imported for tables
import numpy as np # library imported for arrays

# Series data
s1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
s2 = pd.Series([11, 8, 7, 5, 6, 5, 3, 4, 7, 1])

# Compute Euclidean distance
euclidean_distance = np.sqrt(((s1 - s2) ** 2).sum())

#Output
print("\nEuclidean Distance between Series-1 and Series-2:", euclidean_distance)
print("\n")
'''

'''
import os
import pandas as pd  # library imported for tables
import matplotlib.pyplot as plt  # library imported for plotting

print("Looking for file in:", os.getcwd())

# --- Step 1: Load the dataset ---
csv_file = "onlineretail.csv"
excel_file = "Online Retail.xlsx"

if os.path.exists(csv_file):
    print(f"✅ Found {csv_file}, loading CSV...")
    retail_df = pd.read_csv(csv_file, encoding="ISO-8859-1")

elif os.path.exists(excel_file):
    print(f"⚠️ {csv_file} not found. Found {excel_file}, converting to CSV...")
    retail_df = pd.read_excel(excel_file, sheet_name="Online Retail")
    retail_df.to_csv(csv_file, index=False, encoding="utf-8")
    print(f"✅ Saved as {csv_file}, now loading CSV...")
    retail_df = pd.read_csv(csv_file, encoding="ISO-8859-1")

else:
    raise FileNotFoundError("❌ Neither 'onlineretail.csv' nor 'Online Retail.xlsx' found!")

# --- Step 2: Show first 5 rows of data ---
print("\nFirst 5 rows of the dataset:\n")
print(retail_df.head())

# --- Step 3: Show summary statistics of numerical columns ---
print("\nSummary Statistics of Numerical Fields:\n")
print(retail_df.describe())

# --- Step 4: Show first and last column separately ---
first_col = retail_df.iloc[:, 0]    # first column
last_col = retail_df.iloc[:, -1]    # last column

print("\nFirst Column (e.g., InvoiceNo):\n")
print(first_col.head())

print("\nLast Column (e.g., Country):\n")
print(last_col.head())

# --- Step 5: Plot a histogram of Quantity ---
plt.figure(figsize=(8, 5))
plt.hist(retail_df['Quantity'].dropna(), bins=50, edgecolor='black')
plt.title("Histogram of Quantity")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.tight_layout()   # better spacing
plt.show()

'''

'''
#Question No.5
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Import the dataset
# (Make sure 'onlineretail.csv' is in the same folder as this script)
df = pd.read_csv("onlineretail.csv", encoding="ISO-8859-1")

# Step 2: Display data
print(" First 5 rows of dataset:\n", df.head())

# Step 3: Display summary of numerical fields
print("\n Summary of Numerical Fields:\n", df.describe())

# Step 4: Display first and last column
print("\n First Column (InvoiceNo):\n", df.iloc[:, 0].head())
print("\n Last Column (Country):\n", df.iloc[:, -1].head())

# Step 5: Analyze data by plotting histogram
plt.figure(figsize=(8, 5))
plt.hist(df['Quantity'].dropna(), bins=50, edgecolor='black')
plt.title("Histogram of Quantity")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.show()

'''
