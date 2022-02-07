def read_input(msg: str, num1, num2):
    while True:
        try:
            x = int(input(msg))
            if num1 <= x <= num2:
                return x
            else:
                print(f"You must type in an integer between {num1} and {num2}")
        except:
            print(f"You must type in an integer between {num1} and {num2}")


if __name__ == '__main__':
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)
