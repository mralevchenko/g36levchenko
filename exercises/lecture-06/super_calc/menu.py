title = "Super Calc"

def menu():
    print(f"{title}".title().center(40, '='), '\n')
    print("_" * 40)
    print('| Select operation:'.ljust(39) + '|')
    print('|' + "_" * 38 + '|')
    print("| c : Calculate".ljust(39) + '|')
    print("| h : Help".ljust(39) + '|')
    print("| q : Quit".ljust(39) + '|')
    print("=" * 40)

    choice = input("| Enter choice (h|c|q): ".title()).lower()
    return choice if choice in ('h', 'c', 'q') else 'h'
