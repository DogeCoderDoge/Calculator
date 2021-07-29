print("Welcome to CALCULATOR TESTING!")
session_live = True

while session_live:
    print("Type in A for add, S for subtract, M for multiplication, D for divison and EXIT to exit the calculator")
    operation = input();
    
    print("Type in 2 numbers")
    n1 = int(input())
    n2 = int(input())

    if operation == "A":
            sum = n1 + n2
            print("Sum: ", sum) 

    elif operation == "S" :
            diff = n1 - n2
            print("Difference: ", diff)

    elif operation == "M":
            product = n1 * n2
            print("Product: ", product)  

    elif operation == "D":
            quotient = n1/n2
            print("Quotient: ", quotient)

    elif operation == "EXIT":
        print("Thank you for using the calculator")
        session_live = False

    
        