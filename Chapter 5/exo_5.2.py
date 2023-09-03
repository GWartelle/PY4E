largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        if largest is None or int(num)>largest:
            largest=int(num)
        if smallest is None or int(num)<smallest:
            smallest=int(num)
    except:
        print("Invalid input")
print("Maximum is", largest)
print("Minimum is", smallest)