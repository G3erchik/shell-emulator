import os
import getpass
import socket
import sys

from parser import Parser
from shell import Shell


def main():
    emulator = Emulator()
    emulator.run()


class Emulator:
    def __init__(self):
        self.parser = Parser()
        self.shell = Shell()

    def get_prompt(self):
        """
         Приглашение к вводу в стиле username@hostname:cwd$
        Требование №2
        """
        try:
            username = getpass.getuser()
            hostname = socket.gethostname()

            return f"{username}@{hostname}$ "
        except (OSError, KeyError):
            return "user@host:~$ "

    def run(self):
        print("--- Эмулятор оболочки ОС (Этап 1) ---")
        print("Введите 'exit' для выхода.")

        while True:
            try:
                prompt = self.get_prompt()
                user_input = input(prompt)

                elements = list(self.parser.parse(user_input))

                command = elements[0]
                args = elements[1:]

                if command is None:
                    continue

                self.shell.execute_command(command, args)

            except KeyboardInterrupt:
                print("\nДля выхода введите 'exit'")
            except Exception as e:
                print(f"Непредвиденная ошибка: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()