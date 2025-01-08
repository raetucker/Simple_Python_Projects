#quadratic1.py
import math

def main():
    print("Let's find the solutions to a quadratic\n")
    try:
        a = float(input("Enter the coefficient a: "))
        b = float(input("Enter the coefficient b: "))
        c = float(input("Enter the coefficient c: "))
        
        # Calculate the discriminant
        discriminant = b * b - 4 * a * c
        
        # Check if the discriminant is negative, zero, or positive
        if discriminant > 0:
            discRoot = math.sqrt(discriminant)
            root1 = (-b + discRoot) / (2 * a)
            root2 = (-b - discRoot) / (2 * a)
            print("\nThe solutions are:", root1, " and ", root2)
        elif discriminant == 0:
            root = -b / (2 * a)
            print("\nThere is one real solution:", root)
        else:
            print("\nNo Real Roots (the solutions are complex).")
        
    except ValueError as excObj:
        print("You didn't give me the right number of coefficients.")
    except Exception as excObj:
        print(f"Something went wrong: {excObj}")

main()