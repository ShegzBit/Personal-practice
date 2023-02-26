import time
q = 3
v = 1
n = 0
#using a while loop 
while (True):
# ask for user input
    num = input("enter number:")
#take operator
    operator = input("operator: ")
#take user input 
    if("." in num):
        if (operator == "+"):
            n += float(num)
            print (n)
        elif (operator == "-"):
            n -= float(num)
            print (n)
        elif (operator == "*"):
            v *= float(num)
            print (n)
        elif (operator == "/"):
            divisor = float(input ("Enter dividend: "))
            n = num / divisor
            print(n)
    if (not ("." in num)):
        if (operator == "+"):
            n += int(num)
            print (n)
        elif (operator == "-"):
            n -= int(num)
            print (n)
        elif (operator == "*"):
            v *= int(num)
            print (n)
        elif (operator == "/"):
            divisor = int(input ("Enter dividend: "))
            n = num / divisor
        elif (operator == "="):
            print ("final result is " + str(n))
            break
    elif (num.isalnum() or num.isspace() or num.isalpha()):
        print ("SORRY INVALID OPERAND")
        time.sleep(3)
        print ("TERMINATING OPERATION IN")
        while (q > 0):
            print (q)
            q -= 1
            time.sleep(1)
        break


#take operator