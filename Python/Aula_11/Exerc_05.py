def num_primo(num):
    if num == 0 or num == 1:
        print(f'não é numero primo.')
    elif num == 2 or num == 3:
        print('É numero primo')
    else:
        if num % 2 != 0 and num % 3 != 0:
            print('É numero primo')
        else:
            print(f'não é numero primo.')


num_primo(89)
num_primo(71)
num_primo(84)