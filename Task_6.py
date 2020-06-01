goods = []
num = 0
command = ""

while command != 'q':
    command = input("Enter a command:\n 'g' - get analitics;\n 'n' - new item;\n 'q' - quit.\n")
    if command == 'n':
        title = input("Enter the title: ")
        price = input("Enter price: ")
        amount = input("Enter amount: ")
        units = input("Enter units: ")
        num = num + 1
        goods.append((num, {"Title": title, "Price": price, "Amount": amount, "Units": units}))
        print(f"\n{goods}\n")
    elif command == 'g':
        title_list = []
        price_list = []
        amount_list = []
        units_list = []
        for i in range(num):
            title_list.append(goods[i][1]["Title"])
            price_list.append(goods[i][1]["Price"])
            amount_list.append(goods[i][1]["Amount"])
            units_list.append(goods[i][1]["Units"])

        stat_dict = {"Titles": title_list, "Prices": price_list, "Amount": amount_list, "Units": units_list}
        print(f"\n{stat_dict}\n")

