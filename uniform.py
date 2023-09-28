import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


a = [0.1, 0.2, 0.3, 0.4]
b = [1, 2, 3, 4]

uniform_list = []

for i in range(len(a)):
    for i in range(len(b)):
        normal_data = np.random.uniform(low=a[i], high=b[i], size=25)
        uniform_list.append(normal_data)


#print(norm_list)


unidf = {'uni1': uniform_list[0],
            'uni2': uniform_list[1],
            'uni3': uniform_list[2],
            'uni4': uniform_list[3],
            'uni5': uniform_list[4],
            'uni6': uniform_list[5],
            'uni7': uniform_list[6],
            'uni8': uniform_list[7],
            'uni9': uniform_list[8],
            'uni10': uniform_list[9],
            'uni11': uniform_list[10],
            'uni12': uniform_list[11],
            'uni13': uniform_list[12],
            'uni14': uniform_list[13],
            'uni15': uniform_list[14],
            'uni16': uniform_list[15],

            }
df = pd.DataFrame(unidf)

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

