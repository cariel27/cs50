# Multiply each item in a list by 10 and output the mapped values as a tuple assigned to a variable tpl
lst = [1, 2, 3, 4, 5]
tpl = tuple(map(lambda x: x*10, lst))
print(tpl)

# We can apply the map() function on a DataFrame column to create a new column:
import pandas as pd
df = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [0, 0, 0, 0, 0]})
print(df)
df['col3'] = df['col1'].map(lambda x: x * 10)
