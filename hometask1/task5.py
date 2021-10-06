#!/usr/bin/env python
# nevl 2021

def is_number(str):
    try:
        tmp = float(str)
        if tmp <= 0:
            print('Input positive number.')
        return True
    except:
        print('Input not a number')
    return False

if __name__ == '__main__':
    # fetch proceeds
    while True:
        proceeds = input('Input proceeds: ')
        if is_number(proceeds):
            break

    # fetch costs
    while True:
        costs = input('Input costs: ')
        if is_number(costs):
            break

    # check financial results
    profit = float(proceeds) - float(costs)
    financial_results = 'profit' if profit > 0 else 'loss'
    print(f'Financial results are {financial_results}')

    # profitability of proceeds
    if profit > 0:
        profitability_of_proceeds = profit / float(proceeds)
        print(f'Profitability of proceeds = {profitability_of_proceeds}')

    # number of employees
    while True:
        number_of_employees = input('Input number of employees: ')
        if is_number(number_of_employees):
            break

    # profit per employee
    profit_per_employee = profit / float(number_of_employees)
    print(f'Profit {profit_per_employee} per employee.')
