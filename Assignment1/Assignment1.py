'''Print Triangle
Create lower triangular, upper triangular and pyramid containing the "*" character.'''
def lower_triangular(n):
    print("Lower Triangular:")
    for i in range(1, n + 1):
        print('* ' * i)
    print()
def upper_triangular(n):
    print("Upper Triangular:")
    for i in range(n):
        print('  ' * i + '* ' * (n - i))
    print() 
def pyramid(n):
    print("Pyramid:")
    for i in range(n):
        print(' ' * (n - i - 1) + '* ' * (i + 1))
    print()
#n=int(input("Enter n."))
n=5
lower_triangular(n)
upper_triangular(n)
pyramid(n)
