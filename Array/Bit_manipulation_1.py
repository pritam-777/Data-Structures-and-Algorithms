def main():
    a = 60
    b = 70
    size = abs(b - a) + 1
    array = [0] * size
 
    for i in range(a, b + 1):
        if i % 2 == 0 or i % 5 == 0:
            array[i - a] = 1
 
    for i in range(a, b + 1):
        if array[i - a] == 1:
            print(i, end=' ')
 
if __name__ == '__main__':
    main()