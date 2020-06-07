from sys import argv


def salary_calc(worked_hours, hourly_rate, bonus):
    return (worked_hours * hourly_rate) + bonus


scr_name, worked, rate, bns = argv
try:
    print(salary_calc(float(worked), float(rate), float(bns)))
except ValueError:
    print("One of the parameters is not a number!")
