import pandas as pd

data = pd.read_csv('D:/1.txt', sep=' ')
# print data.shape
data.to_csv('D:/2.txt', sep=',', index=False)
