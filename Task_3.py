test_dict = {1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring", 6: "summer",
             7: "summer", 8: "summer", 9: "autumn", 10: "autumn", 11: "autumn", 12: "winter"}

test_list = ["winter", "winter", "spring", "spring", "spring", "summer",
             "summer", "summer", "autumn", "autumn", "autumn", "winter"]

test = test_dict    #use it for solution with dict
#test = test_list    #use it for solution with list

month_num = input("Enter month num: ")
if month_num.isnumeric():
    month_num = int(month_num)
    if (month_num >= 1) and (month_num <= 12):
        print(f"The season for {month_num} month is {test[month_num]}.")
    else:
        print(f"{month_num} is not a month number!")
else:
    print(f"{month_num} is not a number!")
