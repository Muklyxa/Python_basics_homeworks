def print_usr_info(name, surname, year_of_birth, locality, email, phone_number):
    """
    Function for one string user information printing
    :param name:
    :param surname:
    :param year_of_birth:
    :param locality:
    :param email:
    :param phone_number:
    :return:
    """
    print(f"{name} {surname} {year_of_birth:4} {locality} {email} {phone_number:14} ")
    return


print_usr_info(name=input("Enter your name: "),
               surname=input("Enter your surname: "),
               phone_number=input("Enter your phone number: "),
               email=input("Enter your email: "),
               locality=input("Enter your locality: "),
               year_of_birth=input("Enter your year of birth: "))
