# import os
# print(os.name)



# datetime

# from datetime import datetime
# now = datetime.now()
# print(now)



# os: Interacting with the Operating System

# import os
# current_dir = os.getcwd()
# print(current_dir)


# import sys
# print(sys.version)



# 3. Popular Third-party Python Libraries
# a. NumPy: Numerical Computation

# import numpy as np
# arr = np.array([1, 2, 3])
# print(arr) 

# b. Pandas: Data Manipulation


# import pandas as pd

# data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
# df = pd.DataFrame(data)
# print(df)


# c. Matplotlib and Seaborn: Data Visualization


# import matplotlib.pyplot as plt


# x = [1, 2, 3, 4]
# y = [10, 20, 25, 40]
# plt.plot(x, y)
# plt.show()


# d. Requests: HTTP Requests

import requests

response = requests.get('https://api.github.com')
print(response.status_code)