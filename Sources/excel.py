#data frame을 엑셀로 출력하는 코드

# import modules
import pandas as pd
import numpy as np

# index_format(index) & columns_format(columns)정의
index_format = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
columns_format = ['AccountNum', 'User','Item','Compnay','Card','Qunt','ResDate','PayTime']

# DataFrame 초기화
values = pd.DataFrame(index=index_format, columns=columns_format)

# x & y 값 정의
x = index_format
y = np.sin(x)

for ii in range(values.shape[0]):
    # fill in x values into column index zero of values
    values.iloc[ii, 0] = x[ii] #AccountNum
    values.iloc[ii, 1] = y[ii] #User
    values.iloc[ii, 2] = y[ii] #Item
    values.iloc[ii, 3] = y[ii] #Compnay
    values.iloc[ii, 4] = y[ii] #Card
    values.iloc[ii, 5] = y[ii] #Qunt
    values.iloc[ii, 6] = y[ii] #ResDate
    values.iloc[ii, 7] = y[ii] #PayTime

# saves DataFrame(values) into an Excel file
values.to_excel('./test.xlsx',
                sheet_name='Sheet1',
                columns=columns_format,
                header=True,
                index=index_format,
                index_label="y = sin(x)",
                startrow=1,
                startcol=0,
                engine=None,
                merge_cells=True,
                encoding=None,
                inf_rep='inf',
                verbose=True,
                freeze_panes=None)
