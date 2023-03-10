import pandas as pd
import random
data20 = random.sample(range(0,6000), 20)
data100 = random.sample(range(0,6000), 100)
data1000 = random.sample(range(0,6000), 1000)
data4000 = random.sample(range(0,6000), 4000)

print(data20)
print(data100)
print(data100)
print(data4000)
df_20 = pd.DataFrame(data20)
df_100 = pd.DataFrame(data100)
df_1000 = pd.DataFrame(data1000)
df_4000 = pd.DataFrame(data4000)

# saving these in 4 files: arr20.txt, arr100.txt, arr1000.txt and arr4000.txt
df_20.to_csv('ar20.txt', index=False)
df_100.to_csv('ar100.txt', index=False)
df_1000.to_csv('ar1000.txt', index=False)
df_4000.to_csv('ar4000.txt', index=False)

