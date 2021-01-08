password = 'a123456'
chance = 3
while True:
    user = input('Please enter the password: ')
    if user == password:
        print('Login success!')
        break
    else:
        chance = chance - 1
        if chance < 1:
            print('Fail to login.')
            break
        else:
            print('Wrong password, you get', chance, 'chance to try.')