proceeds = float(input("Enter proceeds: "))
costs = float(input("Enter costs: "))

if proceeds == costs:
    print("The company worked without profit and without loss.")
elif proceeds < costs:
    print("The company worked with loss.")
else:
    profit = proceeds - costs
    profitability = profit / proceeds
    print(f"The company worked with profit {profit:.2f} and profitability {profitability:.2f}.")
    num_of_workers = int(input("Enter the number of employers in the company: "))
    profit_per_employeer = profit / num_of_workers;
    print(f"Profit per employeer: {profit_per_employeer:.2f}")