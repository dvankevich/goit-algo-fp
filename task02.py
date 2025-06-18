'''
Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.
https://en.wikipedia.org/wiki/Pythagoras_tree_(fractal)

'''
import turtle

def draw_branch(branch_length, level):
    if level == 0:
        return
    
    # Draw the current branch
    turtle.forward(branch_length)
    
    # Draw the right branch
    turtle.right(30)
    draw_branch(branch_length * 0.7, level - 1)
    
    # Draw the left branch
    turtle.left(60)
    draw_branch(branch_length * 0.7, level - 1)
    
    # Return to the previous state
    turtle.right(30)
    turtle.backward(branch_length)

def main():
    level = int(input("Введіть рівень рекурсії (від 1): "))
    if level < 1:
        print("Неправильний рівень. Будь ласка, введіть число від 1.")
        return

    turtle.speed(0)  # Найшвидший режим
    turtle.left(90)   # Почати з вертикального положення
    turtle.up()
    turtle.backward(100)
    turtle.down()
    turtle.color("green")

    draw_branch(100, level)  # Початкова довжина гілки
    turtle.done()

if __name__ == "__main__":
    main()