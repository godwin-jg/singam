import pandas as pd
# df = pd.read_csv('CSE_A.csv')

# print(df.to_string)

mydataset = {
  'cars': ["A", "B", "C"],
  'passings': [10, 20, 30]
}
# a = [1,7,2]
# myvar = pd.Series(a)
myvar = pd.DataFrame(mydataset)

print(myvar)