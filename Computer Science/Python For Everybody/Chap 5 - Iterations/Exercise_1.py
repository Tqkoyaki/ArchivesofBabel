largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        n = int(num)
    except:
        if num == "done":
            break
        else:
            print("Invalid input")

    if largest == None:
        largest = n
        smallest = n
    elif n > largest:
        largest = n
    elif n < smallest:
        smallest = n

print("Maximum is", largest)
print("Minimum is", smallest)