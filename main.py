'''
    Author: Jason Tran
    Date: 10/31/23
    Class: COP3502C
'''


def print_menu():
    print('Menu\n'
          '-------------\n'
          '1. Encode\n'
          '2. Decode\n'
          '3. Quit\n')


def main():
    while True:
        print_menu()
        option = int(input("Please enter an option: "))

        if option == 1:
            encoded_pw = encode(input("Please enter your password to encode: "))
            print("Your password as been encoded and stored!\n")
        elif option == 2:
            pass
            #Implement decode here
        elif option == 3:
            break


def encode(password):
    encoded_pw = "".join(str((int(item)+3)) for item in password)
    return encoded_pw


if __name__ == "__main__":
    main()