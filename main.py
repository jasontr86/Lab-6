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
            print("Your password has been encoded and stored!\n")
        #Brenden Brahier
        elif option == 2:
            print(f"The encoded password is {encoded_pw} , and the original password is {decode(encoded_pw)}.")
            # Implement decode here
        elif option == 3:
            break


def encode(password):
    encoded_pw = "".join(str((int(item) + 3)) for item in password)
    return encoded_pw

#converts the encoded password back to it's original value -Brenden Brahier
def decode(password):
    decode_pass = "".join(str((int(item) - 3)) for item in password)
    return decode_pass


if __name__ == "__main__":
    main()
