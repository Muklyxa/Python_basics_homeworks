number = int(input("Enter a number greater than zero: "))

greatest_is_found = False
current_greatest = 0
new_greatest = 0
divider = 10

while not(greatest_is_found):
    new_greatest = number % divider
    new_greatest = new_greatest // (divider//10)
    if new_greatest > current_greatest:
        current_greatest = new_greatest
        if current_greatest == 9:
            greatest_is_found = True
            break
    number = number - (new_greatest * (divider // 10))

    if number == 0:
        greatest_is_found = True
        break
    else:
        divider = divider * 10

print(f"Greatest digit is: {current_greatest}")
