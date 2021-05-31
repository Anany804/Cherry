'''
This is a Simple Physics all in one calculator for simple Physics numericals
--------------------
'''
import math 

while True:
    print("See your results ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("---------------------------------------------------------------------------")
    print("What do you want to calculate.")
    print("Press 'v' to calculate velocity.")
    print("Press 'a' to calculate acceleration.")
    print("Press '1' to calculate 'v' with Newton's first law.")
    print("Press 2 to calculate 's' with Newton's second law of motion.")
    print("To calculate the value of 'v^2' with Newton's third law motion press '3'.")
    print("To find the value of force Enter 'f'.")
    print("To find momentum press 'm'...")
    print("To find Kinetic Energy, Enter 'ke' (in small case only)")
    print("To find Potential Energy, Enter 'pe' (in small case only)")
    print("To quit the program press 'q'.... ")
    print("Made by Anany...")
    a = input("Enter here: ")
    
    if (a == "a"):
        b = float(input("Enter final velocity in m/s (Enter numbers only)- "))
        c = float(input("Enter initial velocity in m/s (Enter numbers only)- "))
        d = float(input("Enter time in seconds (Enter numbers only) - "))
        acc = (b - c)/d
        print(f'Acceleration of the body is {round(acc, 3)} m/s')
        
    elif (a == "v"):
        b = float(input("Enter displacement in metres (Enter numbers only) - "))
        c = float(input("Enter time in seconds (Enter numbers only) - "))
        v = b / c
        print(f'Velocity of the body is {round(v, 3)} m/s')
    
    elif (a == "1"):
        b = float(input("Enter the value of 'u' (Enter numbers only): "))
        c = float(input("Enter value of 'a' (Enter numbers only): "))
        d = float(input("Enter time in seconds (Enter numbers only): "))
        v = b + (c*d)
        print(f'Velocity of the body is {round(v, 3)} m/s')
    
    elif (a == "2"):
        b = float(input("Enter the value of 'u' : "))
        c = float(input("Enter the value of 't' : "))
        d = float(input("Enter the value of 'a' : "))
        D = (b*c) + 0.5*(d * (c**2))
        print(f'Displace of the body is {round(D, 3)} meters')
    
    elif (a == "3"):
        b = float(input("Enter the value of 'u' : "))
        c = float(input("Enter the value of 'a' : "))
        d = float(input("Enter the value of 's' : "))
        v2 = (b**2) + (2 * c * d)
        print(f'v^2 = {round(v2, 3)} m/s')
    
    elif (a == "f"):
        b = float(input("Enter mass in kg's : "))
        c = float(input("Enter the value of acceleration : "))
        f = b * c
        print(f'Force = {round(f, 3)} N')
        
    elif (a == "m"):
        b = float(input("Enter mass in Kgs: "))
        c = float(input("Enter body's velocity (m/s): "))
        m = b*c
        print(f'Momentum of the body is {round(m, 3)} Kgm/s')
    
    elif a == "ke":
        b = float(input("Enter mass (Kg): "))
        c = float(input("Enter velocity (m/s): "))
        ke = (1/2)*(b)*(c**2)
        print(f'Kinetic Energy of the body is {round(ke, 3)} Joules...')
    
    elif a == "pe":
        b = float(input("Enter mass (Kg): "))
        c = float(input("Enter height in metres: "))
        g = 9.8
        pe = b * c * g
        print(f'Potential Energy of the object on earth = {round(pe, 3)} Joules...')
    
    elif (a == "q"):
        print("Thank you for using this calculator.. See you soon...")
        quit()   
    else:
        print('Wrong Input...')
        quit()
