import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json('steamgames.json',encoding='utf-8')
df = df[df['discount']!='No discount for now'].drop(['name','link','time','price'],axis=1)
for i in df.columns:
    df[i] = df[i].str.extract('(\d+)')

df=df.astype(float)
df.plot()
my_y_ticks = [20,40,60,80,100]
plt.yticks(my_y_ticks)
plt.xlabel('Number of games')
plt.ylabel('favorable rate(%)')
plt.title('evaluate & discount')
plt.show()