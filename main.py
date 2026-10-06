import pandas as pd
from src.reporter import DataFrameReporter

def main():
    reporter = DataFrameReporter()
    df = pd.read_csv('data/payments.csv')
    reporter.show_report(df, title='Информация о ДатаФрейме')
if __name__ == '__main__':
    main()