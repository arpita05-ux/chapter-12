try:
    a = int(input("Hey Enter a number : " ))
    print(a)  


except Exception as e:   #using try, except, as, and the exception = Python doesn't make your program invalid, even when an error happens. It helps your program handle the error gracefully instead of crashing.
     print(e) 

print("Thank you")      