from lab_python_oop import circle, rectangle, square
# from colorama import Fore, Back, Style, init
# Back.WHITE
# pyinstaller -F main.py

# def out_red(text):
#     print("\033[31m {}" .format(text))  # красный
# def out_green(text):
#     print("\033[32m {}" .format(text))  # зеленый
# def out_blue(text):
#     print("\033[34m {}" .format(text))  # синий

def main():
    print(circle.Circle(5, "Зелёный"))
    print(rectangle.Rectangle(3, 2, "Синий"))
    print(square.Square(5, "Красный"))

if __name__ == '__main__':
    main()
    
input("Press Enter")