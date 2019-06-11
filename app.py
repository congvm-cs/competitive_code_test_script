def main():
    n = int(input(""))
    for _ in range(n):
        x, y = input("").strip().split(" ")
        # ...
        z = int(x) + int(y)
        # ...
        print("{}".format(z))
    
    
    
if __name__ == '__main__':
    main()