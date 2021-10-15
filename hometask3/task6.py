#!/usr/bin/env python
# nevl 2021

def int_func2222222(text):
    """
    Capitalize

    :param text: String
    :return: String
    """
    return 0

if __name__ == '__main__':
    int_func = lambda text: str(text).capitalize()

    # task 6
    word = input('Enter word: ')
    print(int_func(word))

    # task 7
    sentence = input('Enter sentence: ')
    for it in sentence.split():
        print(f'{int_func(it)} ', end='')
    print('')
