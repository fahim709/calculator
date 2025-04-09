while True:
    try:
        a = int(input('type your first number: '))

        b = int(input('type your second number: '))

        c = input("type your operator: ")

        if c == "+":
           print(a + b)

        elif c == "-":
            print(a - b)

        elif c == "*":
            print(a * b)
 
        elif c == "/":
            if b == 0:
              print("Error: Division by zero!")
            else:
              print(a / b)
              break
    except ValueError:
        print("Error: Invalid input. Please enter a number and an operator.")
