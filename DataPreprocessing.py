import pandas as pd
import numpy as np


class DataProcess:
    def del_duplicates(self, df):
        df_without_duplicates = df.drop_duplicates(keep=False)
        df_without_duplicates = pd.DataFrame(df_without_duplicates,
                                             columns=['Colour', 'Radius (cm)', 'Weight (grams)', 'Fruit (class)'])
        df_without_duplicates.to_csv('del_duplicates.csv', index=False)
        return df_without_duplicates

    def fill_values(self, df):
        # df['Radius (cm)'] = df['Radius (cm)'].replace(0, df.groupby('Fruit (class)')['Radius (cm)'].mean())
        df_fill = df.copy()
        df_fill.iloc[:,1] = df_fill.iloc[:,1].replace(0, np.nan)
        df_fill.iloc[:,1] = df_fill.iloc[:,1].fillna(df.groupby('Fruit (class)')['Radius (cm)'].transform('mean'))
        df_fill.iloc[:,2] = df_fill.iloc[:,2].replace(0, np.nan)
        df_fill.iloc[:,2] = df_fill.iloc[:,2].fillna(df.groupby('Fruit (class)')['Weight (grams)'].transform('mean'))
        df_fill.to_csv('mean.csv', index = False, float_format= '%.2f')
        return df_fill

    def transform_nominal(self, df):
        df_transformnominal = df.copy()
        df_transformnominal['Green'] = df_transformnominal.iloc[:,0].replace({'Green': 1, 'Yellow': 0, 'Red': 0})
        df_transformnominal['Yellow'] = df_transformnominal.iloc[:,0].replace({'Yellow': 1, 'Green': 0, 'Red': 0})
        df_transformnominal['Red'] = df_transformnominal.iloc[:,0].replace({'Red': 1, 'Yellow': 0, 'Green': 0})
        df_transformnominal = df_transformnominal.drop(columns='Colour')
        df_transformnominal = df_transformnominal[['Green', 'Red', 'Yellow', 'Radius (cm)', 'Weight (grams)']]
        df_transformnominal.to_csv('transform_nominal.csv', index = False)
        return df_transformnominal

    def normalise_minmax(self, df):
                df_minmax = df.copy()
                radiusmin_value = df_minmax.iloc[:,1].min()
                radiusmax_value = df_minmax.iloc[:,1].max()
                df_minmax.iloc[:,1] = (df_minmax.iloc[:,1] - radiusmin_value)/(radiusmax_value - radiusmin_value)
                weightmin_value = df_minmax.iloc[:,2].min()
                weightmax_value = df_minmax.iloc[:,2].max()
                df_minmax.iloc[:,2] = (df_minmax.iloc[:,2] - weightmin_value) / (weightmax_value - weightmin_value)
                df_minmax.to_csv('normalise.csv', index = False, float_format= '%.2f')
                return df_minmax




dp = DataProcess()
df = pd.read_csv("C:\\Users\\algat\\OneDrive\\Desktop\\Vaishnavi\\Web and Data Science\\Machine Learning and Data Mining\\ML_assignment02_dataset_2021.csv")
pd.options.display.float_format = "{:,.2f}".format
df_without_duplicates = dp.del_duplicates(df)
print(df_without_duplicates)
df_mean = dp.fill_values(df)
print(df_mean)
df_transform = dp.transform_nominal(df)
print(df_transform)
df_normalise = dp.normalise_minmax(df)
print(df_normalise)
