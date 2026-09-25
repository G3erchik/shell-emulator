import sys


class Shell:
    def execute_command(self, command: str, args):
        if command == "exit":
            print("Выход из эмулятора...")
            sys.exit(0)

        elif command == "ls":
            print(f"Выполнена команда: ls")
            print(f"Аргументы: {args}")

        elif command == "cd":
            print(f"Выполнена команда: cd")
            print(f"Аргументы: {args}")

        else:
            print(f"Ошибка: команда '{command}' не найдена.", file=sys.stderr)
            if args:
                print(f"Полученные аргументы: {args}", file=sys.stderr)