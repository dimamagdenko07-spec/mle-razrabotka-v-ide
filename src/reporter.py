import pandas as pd
class DataFrameReporter:
    def __init__(self, float_format: str = '0.05f', percent_format: str = '0.02%', include_all = False):
        self.float_format = float_format
        self.percent_format = percent_format
        self.include_all = include_all
        def show_report(self, df: pd.DataFrame, title: bool = False):
            if title:
                print(title)
            print("Количество столбцов: ", df.shape[1])
            print("Количество строк: ", df.shape[0])
            print("Количество дубликатов: ", df.duplicated().sum())
            print("Доля дулбикатов: ", format(df.duplicated().sum() / df.shape[0], self.percent_format))


            if self.include_all:
                print(df.describe(include='all'))
            else:
                print(df.describe())
    
            print("Количество пропусков: ", df.isna().sum().sum())
            print("Доля пропусков: ", format(df.isna().sum().sum() / df.shape[0] / df.shape[1], self.float_format))