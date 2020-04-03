def set_password(length):
    password = input("Please enter your password: ")
    while len(password) < length:
        print("Your password should be {} characters".format(length))
        password = input("Please enter your password: ")
    print("Your password is:")
    for char in password:
        print("*", end='')


def main():
    set_password(12)


if __name__ == '__main__':
    main()
