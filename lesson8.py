enter_login = input('Enter login ')
enter_password = input('Enter password ')

if enter_login.isalpha() and enter_password.isalnum():
    enter_password_again = input('Enter password again ')
    if enter_password == enter_password_again:
        print('Congratulations! You are registered\n\n')
    else:
        print('Passwords do not match')

    print('You are blocked. We need to know that You have a good memory)')

    enter_re_login = input('Enter Your login again ')
    enter_re_password = input('And enter Your password again ')

    if enter_re_login.isalpha() and enter_re_password.isalnum():
        if enter_re_login == enter_login and enter_re_password == enter_password:
            print('Congratulations! You are registered')
        else:
            print('You have bad memory)')
    else:
        print('Use only letters in your login and only letters and numbers in your password')

else:
    print('Use only letters in your login and only letters and numbers in your password')
