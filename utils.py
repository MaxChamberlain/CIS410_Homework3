import pandas as pd
import matplotlib.pyplot as plt

def read_data(FILENAME):
    data = pd.read_csv(FILENAME)
    return data

def display_info(data):
    print("FILE INFO\n")
    data.info()

def display_unique_values(data):
    print("UNIQUE VALUES\n")
    unique_values = data.nunique()
    print(unique_values)

def display_all_rows(data):
    pd.set_option('display.max_rows', None)
    print("ALL ROWS\n")
    print(data)
    pd.reset_option('display.max_rows')

def display_first_last_rows_columns(data):
    print("FIRST AND LAST FIVE ROWS AND COLUMNS\n")
    first_rows = data.head(5)
    last_rows = data.tail(5)
    selected_columns = pd.concat([data.iloc[:, :4], data.iloc[:, -4:]], axis=1)
    print("First 5 rows of selected columns:\n", selected_columns.head(5))
    print("\nLast 5 rows of selected columns:\n", selected_columns.tail(5))

def access_three_columns(data):
    print("FIRST FIVE ROWS OF THREE COLUMNS\n")
    selected_columns = data[['Total Volume', 'AveragePrice', 'Total Bags']]
    print(selected_columns.head(5))

def access_one_column_dot_notation(data):
    print("ONE COLUMN USING DOT NOTATION\n")
    print(data.Total_Volume.head(5))  # Ensure column name matches CSV

def multiply_columns(data):
    print("MULTIPLY Total Volume AND AveragePrice, ADD COLUMN EstimatedRevenue\n")
    data['EstimatedRevenue'] = data['Total Volume'] * data['AveragePrice']
    print(data[['Total Volume', 'AveragePrice', 'EstimatedRevenue']].head(5))

def group_by_region_type(data):
    print("GROUP BY region AND type, SHOW AVERAGE PRICE\n")
    grouped_data = data.groupby(['region', 'type'])['AveragePrice'].mean().reset_index()
    print(grouped_data.head(5))

def plot_volume_statistics_by_year(data):
    print("PLOT Mean, Median, and Std Dev OF Total Volume BY YEAR\n")
    grouped_year = data.groupby('year')['Total Volume'].agg(['mean', 'median', 'std']).reset_index()
    grouped_year.plot(x='year', y=['mean', 'median', 'std'], kind='bar')
    plt.title('Total Volume Statistics by Year')
    plt.ylabel('Total Volume')
    plt.show()

def group_by_type_bags(data):
    print("GROUP BY type, SUM OF Small Bags, Large Bags, XLarge Bags\n")
    bags_data = data.groupby('type')[['Small Bags', 'Large Bags', 'XLarge Bags']].sum().reset_index()
    print(bags_data)

def plot_bags_by_type(data):
    print("PLOT Bags by type\n")
    bags_data = data.groupby('type')[['Small Bags', 'Large Bags', 'XLarge Bags']].sum().reset_index()
    bags_data.plot(x='type', y=['Small Bags', 'Large Bags', 'XLarge Bags'], kind='bar')
    plt.title('Number of Small, Large, and XLarge Bags by Type')
    plt.ylabel('Bags Count')
    plt.show()

def scatter_plot_volume_vs_price(data):
    print("SCATTER PLOT OF Total Volume AND AveragePrice\n")
    data.plot(kind='scatter', x='Total Volume', y='AveragePrice')
    plt.title('Total Volume vs Average Price')
    plt.show()