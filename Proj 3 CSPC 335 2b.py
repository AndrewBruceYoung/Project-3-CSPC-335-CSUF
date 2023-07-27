import math

def fibonacci_equation3(n):
    final_num = ((((1 + math.sqrt(5))**n) -
                  ((1 - math.sqrt(5))**n))/((2**n)*math.sqrt(5)))
    return final_num

def fibonacci_equation4():
    number_checker = False
    while number_checker == False:
        try:
            p = int(input("Enter a positive integer 'p': "))
            if p <= 0:
                print("Please enter a positive integer.")
            else:
                number_checker = True
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    p_fibonacci = fibonacci_equation3(p)
    n = int(input("Enter n: "))
    n_fibonacci = (p_fibonacci)*(((1 + math.sqrt(5))/(2))**(n - p))
    return n_fibonacci
    
def fibonacci_equation5():
    n = int(input("Enter the number corresponding to the position desired Fibonacci number: "))
    n_minus_one_fibonacci = fibonacci_equation3(n - 1)
    n_fibonacci = ((n_minus_one_fibonacci)*((1 + math.sqrt(5))/(2)))
    return n_fibonacci


def no_user_input_fibonacci_equation4(p,n):
    p_fibonacci = fibonacci_equation3(p)
    n_fibonacci = (p_fibonacci)*(((1 + math.sqrt(5))/(2))**(n - p))
    return n_fibonacci

def no_user_input_fibonacci_equation5(n):
    n_minus_one_fibonacci = fibonacci_equation3(n - 1)
    n_fibonacci = ((n_minus_one_fibonacci)*((1 + math.sqrt(5))/(2)))
    return n_fibonacci

def first_20_numbers():
    list_of_equation4 = []
    list_of_equation5 = []
    for i in range(20):
        p = 5
        if i == 0:
            p = 0
        q = i
        if i == 0:
            q = 1
        list_of_equation4.append(no_user_input_fibonacci_equation4(p,i))
        list_of_equation5.append(no_user_input_fibonacci_equation5(q))
    print("First 20 results of equation 4: ")
    print(list_of_equation4)
    print("First 20 results of equation 5: ")
    print(list_of_equation5)
    return
    
