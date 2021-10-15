#!/usr/bin/env python
# nevl 2021

def print_info(first_name, second_name, year_of_birth, city, email, phone_number):
    """
    Print user info
    
    :param first_name: String: First name
    :param second_name: String: Second name
    :param year_of_birth: String: Year of birthday
    :param city: String: City
    :param email: String: E-mail
    :param phone_number: String: Phone number in international format
    :return: None
    """
    print(f'{first_name} {second_name}, {year_of_birth}, {city}, {email}, {phone_number}')


if __name__ == '__main__':
    first_name = input('First name: ')
    second_name = input('Second name: ')
    year_of_birth = input('Year of birthday: ')
    city = input('City: ')
    email = input('E-mail: ')
    phone_number = input('Phone number in international format: ')

    print_info(phone_number=phone_number, email=email, city=city, year_of_birth=year_of_birth,
               second_name=second_name, first_name=first_name)
