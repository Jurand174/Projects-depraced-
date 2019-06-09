import pandas as pd
import numpy as np
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

import glob

sum1 = []
sum2 = []
sum3 = []
a = glob.glob('./TEL2/*.xlsx')

for i in range(0, len(a)):
    c = pd.read_excel(a[i])
    c.dropna(inplace=True)
    c.set_index('Frequency [Hz]', inplace=True)
    sum3.append(c['Value [W/cm^2]'].loc[2141750000])
    sum2.append(c['Value [W/cm^2]'].loc[1855750000])
    sum1.append(c['Value [W/cm^2]'].loc[959750000])

sum1 = np.array(sum1).astype(np.float64)
sum2 = np.array(sum2).astype(np.float64)
sum3 = np.array(sum3).astype(np.float64)
a1 = np.mean(sum1)
a2 = np.mean(sum2)
a3 = np.mean(sum3)
a = [a1, a2, a3]
print(a)
q1 = 0
q2 = 0
q3 = 0
for i in range(0, len(a)):
    q1 = q1 + (sum1[i] - a[0]) ** 2
    q2 = q2 + (sum2[i] - a[1]) ** 2
    q3 = q3 + (sum3[i] - a[2]) ** 2

print([np.sqrt(q1 / 56), np.sqrt(q2 / 56), np.sqrt(q3 / 56)])

