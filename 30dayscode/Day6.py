# Enter your code here. Read input from STDIN. Print output to STDOUT
def main():
    n = int(input())
    for i in range(0,n):
        lst = input()
        for j in range (0,len(lst)):
            if (j % 2 == 0):
                print(lst[j], end='')
        print(" ", end='')
        for j in range(0, len(lst)):
            if(j % 2 != 0):
                print(lst[j], end='')


main()