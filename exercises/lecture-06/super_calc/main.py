from menu import menu
from calculator import run_calculator
from helpers import calc_help

def main():
    while True:
        choice = menu()
        if choice == 'q':
            print('Thank you for using Super Calc!')
            break
        elif choice == 'h':
            calc_help()
        elif choice == 'c':
            run_calculator()

if __name__ == '__main__':
    main()
