min_profit = 20000.0
with open("text_3.txt", "r", encoding="utf-8") as f_obj:
    content = f_obj.readlines()
    total_profit = 0
    length = len(content)
    for i in range(length):
        [name, profit] = content[i].split()
        profit = float(profit)
        total_profit += profit
        if profit < min_profit:
            print(f"{name} has profit less than {min_profit}.")
print(f"Average profit is {total_profit/length}.")