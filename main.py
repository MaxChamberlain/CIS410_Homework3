from utils import read_data, display_info, display_unique_values, display_all_rows, display_first_last_rows_columns, access_three_columns, multiply_columns, group_by_region_type, plot_volume_statistics_by_year, group_by_type_bags, plot_bags_by_type, scatter_plot_volume_vs_price

FILENAME = "hw3_avocado.csv"

def main():
    data = read_data(FILENAME)
    while True:
        print("\nLoaded data from file. What would you like to do?")
        print("1. Display info")
        print("2. Display unique values")
        print("3. Display all rows")
        print("4. Display first and last five rows and columns")
        print("5. Access three columns and display first five rows")
        print("6. Access one column using dot notation")
        print("7. Multiply Total Volume and AveragePrice columns")
        print("8. Group by region and type and display average price")
        print("9. Create bar plot of Total Volume by year")
        print("10. Create new DataFrame with total of bags grouped by type")
        print("11. Create bar plot of bags by type")
        print("12. Create scatter plot of Total Volume and AveragePrice")
        print("13. Exit")
        
        choice = input("Enter choice: ")

        if choice == "1":
            display_info(data)
        elif choice == "2":
            display_unique_values(data)
        elif choice == "3":
            display_all_rows(data)
        elif choice == "4":
            display_first_last_rows_columns(data)
        elif choice == "5":
            access_three_columns(data)
        elif choice == "6":
            columns = data.columns
            print("Pick a column from the following list:")
            for i, column in enumerate(columns):
                print(f"{i+1}. {column}")
            column_choice = input("Enter column number: ")
            print(data[columns[int(column_choice)-1]].head(5))
        elif choice == "7":
            multiply_columns(data)
        elif choice == "8":
            group_by_region_type(data)
        elif choice == "9":
            plot_volume_statistics_by_year(data)
        elif choice == "10":
            group_by_type_bags(data)
        elif choice == "11":
            plot_bags_by_type(data)
        elif choice == "12":
            scatter_plot_volume_vs_price(data)
        elif choice == "13":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
