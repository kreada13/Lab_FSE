n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
ch = input("Введите символ, с помощью которого будет отрисовываться фигура: ")
print(f"ПРЯМОУГОЛЬНИК {n}×{m}:")
def draw_rectangle(n,m,ch):
    for i in range(n):
        for j in range(m):
            print(ch, end="")
        print()
draw_rectangle(n,m,ch)
print()
print("ПРАВЫЙ ТРЕУГОЛЬНИК:")
def draw_triangle(n,m,ch):
    for i in range(1, n + 1):
        for j in range(i):
            print(ch, end="")
        print()
draw_triangle(n,m,ch)
print()
print(f"РАМКА {n}*{m}:")
def draw_frame(n,m,ch):
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                print(ch, end="")
            else:
                print(" ", end="")
        print()
draw_frame(n,m,ch)