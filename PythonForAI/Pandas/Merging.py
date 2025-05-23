import numpy as np
import pandas as pd

#create 3 data frames
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])
print(df1)

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7]) 
print(df2)

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])
print(df3)

#Row concatination 
concat_df = pd.concat([df1, df2, df3])
print(concat_df)

#Column concatination
concat_df_col = pd.concat([df1, df2, df3], axis=1)
print(concat_df_col) #it will create NaN values for the empty space

#Merge function 
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
   
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})    

merge_df = pd.merge(left, right, how="inner", on="key") #inner join, meaning only rows with matching values in both DataFrames are included.
print(merge_df)

#merge 2 keys
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
print(left)
    
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                               'key2': ['K0', 'K0', 'K0', 'K0'],
                                  'C': ['C0', 'C1', 'C2', 'C3'],
                                  'D': ['D0', 'D1', 'D2', 'D3']})
print(right)

merge_df_v2 = pd.merge(left, right, on=['key1', 'key2'])
print(merge_df_v2)

merge_df_v3 = pd.merge(left, right, how='outer', on=['key1', 'key2'])
print(merge_df_v3)

merge_df_v4 = pd.merge(left, right, how='right', on=['key1', 'key2'])
print(merge_df_v4)

merge_df_v5 = pd.merge(left, right, how='left', on=['key1', 'key2'])
print(merge_df_v5)

#Joining function for combining the columns of two potentially differently-indexed DataFrames into a single
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])

left_df1 = left.join(right)
print(left_df1)

left_df2 = left.join(right, how='outer')
print(left_df2)
