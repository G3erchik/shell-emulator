import sys


class Shell:
    def __init__(self):
        self.vfs_path = None

    def set_vfs_path(self, path):
        self.vfs_path = path

    def execute_command(self, command: str, args):
        if command == "exit":
            print("Выход из эмулятора...")
            sys.exit(0)

        elif command == "ls":
            print(f"Выполнена команда: ls")
            if self.vfs_path:
                print(f"(Виртуальная ФС: {self.vfs_path})")
            print(f"Аргументы: {args}")

        elif command == "cd":
            print(f"Выполнена команда: cd")
            print(f"Аргументы: {args}")

        elif command == "echo":
            print(" ".join(args))

        else:
            print(f"Ошибка: команда '{command}' не найдена.", file=sys.stderr)
            if args:
                print(f"Полученные аргументы: {args}", file=sys.stderr)