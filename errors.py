ZERO = 0
n = "A"
try:
    s = int(ord(n)+"ZERO")
    print("No exception was raised.")
except ValueError:
    print("A ValueError exception was raised.")
except SyntaxError:
    print("A SyntaxError exception was raised.")
except TypeError:
    print("A TypeError exception was raised.")
except:
    print("A general exception was raised.")

