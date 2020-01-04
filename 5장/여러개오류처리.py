try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)

try: 
    a=[1.2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("Could not divid 0")
except IndexError:
    print("Could not indexing")

try:
    a=[1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)