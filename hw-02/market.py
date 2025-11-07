import csv

def read_csv():
    data = []
    with open("sales.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                row[1] = float(row[1].strip())
                row[2] = int(row[2].strip())
                data.append(row)
            except Exception:
                pass

    return data

def calculate_total_sale(data:list):
    total_sale = 0.0
    for item in data:
        total_sale += item[1] * item[2]
    
    return total_sale

def calculate_total_transaction(data:list):
    return len(data)

def count_sells_per_product(data:list):
    product_dict = {}
    for item in data:
        if product_dict.get(item[0]) is None:
            product_dict[item[0]] = item[2]
        else:
            product_dict[item[0]] += item[2]
    
    return product_dict

def find_best_selling_product(data:list):
    product_dict = count_sells_per_product(data)
    best_selling_product_name = ""
    best_selling_product_count = 0

    for key, value in product_dict.items():
        if value > best_selling_product_count:
            best_selling_product_count = value
            best_selling_product_name = key

    return best_selling_product_name

def calculate_average_purcahse(data:list):
    total_product = 0
    total_price = 0
    for item in data:
        total_price += (item[1] * item[2])
        total_product += item[2]
    return total_price / total_product

def add_report():
    try:
        product_name = input("Enter a product name: ")
        product_price = float(input("Enter a product price: "))
        product_sale_count = int(input("Enter number of product's sales count: "))
        with open('sales.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([product_name, product_price, product_sale_count])
    except ValueError as e:
        print(e)

def main():
    command = input("Enter sh (to display daily report)\n" \
                    "Enter a (to add new report)\n" \
                    "Enter q (to quit)")
    
    while command != "q":
        if command == "sh":
            print("***Daily Sales Report***")
            data = read_csv()
            print("Total Transactions: ", calculate_total_transaction(data))
            print("Total Daily Sales: ", calculate_total_sale(data))
            print("Best Selling Product: ", find_best_selling_product(data))
            print("Average Purchase: ", calculate_average_purcahse(data))
            print("***************")
        elif command == 'a':
            add_report()
        command = input("Enter sh (to display daily report)\n" \
                    "Enter a (to add new report)\n" \
                    "Enter q (to quit)")
            
main()