import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
'''
data1 = np.random.normal(100, 10, 250)  # parameters here are loc=mean, scale = sd, and size
data2 = np.random.normal(200, 15, 250)
data3 = np.random.normal(300, 17, 250)
data4 = np.random.normal(400, 16, 250)
'''

loc = [1, 2, 3, 4]
scale = [10, 20, 30, 40]

norm_list = []

for i in range(len(loc)):
    for i in range(len(scale)):
        normal_data = np.random.normal(loc=loc[i], scale=scale[i], size=25)
        norm_list.append(normal_data)


#print(norm_list)


normdf = {'norm1': norm_list[0],
            'norm2': norm_list[1],
            'norm3': norm_list[2],
            'norm4': norm_list[3],
            'norm5': norm_list[4],
            'norm6': norm_list[5],
            'norm7': norm_list[6],
            'norm8': norm_list[7],
            'norm9': norm_list[8],
            'norm10': norm_list[9],
            'norm11': norm_list[10],
            'norm12': norm_list[11],
            'norm13': norm_list[12],
            'norm14': norm_list[13],
            'norm15': norm_list[14],
            'norm16': norm_list[15],

            }
df = pd.DataFrame(normdf)

def draw_histograms1(df, variables, n_rows, n_cols):
    fig=plt.figure(figsize=(10,10))
    for i, var_name in enumerate(variables):
        ax=fig.add_subplot(n_rows,n_cols,i+1)
        df[var_name].hist(ax=ax)
        ax.set_title(var_name)
        plt.xlim(0,10)
    fig.tight_layout()
    # Improves appearance a bit.
    plt.show()

draw_histograms1(df, df.columns, 4,4)

