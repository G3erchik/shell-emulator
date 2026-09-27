import os
import getpass
import socket
import sys
import argparse

from parser import Parser
from shell import Shell
from script_runner import ScriptRunner


def main():
    cli_parser = argparse.ArgumentParser(description="Эмулятор оболочки ОС")


    cli_parser.add_argument(
        "--vfs",
        type=str,
        default="./vfs_root",
        help="Путь к физическому расположению VFS"
    )


    cli_parser.add_argument(
        "--script",
        type=str,
        default=None,
        help="Путь к стартовому скрипту"
    )

    args = cli_parser.parse_args()


    emulator = Emulator(vfs_path=args.vfs, script_path=args.script)
    emulator.run()


class Emulator:
    def __init__(self, vfs_path: str, script_path: str = None):
        self.vfs_path = vfs_path
        self.script_path = script_path

        self.parser = Parser()
        self.shell = Shell()


        if hasattr(self.shell, 'set_vfs_path'):
            self.shell.set_vfs_path(vfs_path)

        self._print_debug_info()

    def _print_debug_info(self):

        print("--- Конфигурация эмулятора ---")
        print(f"Путь к VFS: {os.path.abspath(self.vfs_path)}")
        if self.script_path:
            print(f"Стартовый скрипт: {os.path.abspath(self.script_path)}")
        else:
            print("Стартовый скрипт: не задан")
        print("-----------------------------")

    def get_prompt(self):
        """
        Приглашение к вводу в стиле username@hostname:cwd$
        """
        try:
            username = getpass.getuser()
            hostname = socket.gethostname()
            return f"{username}@{hostname}$ "
        except (OSError, KeyError):
            return "user@host:~$ "

    def run(self):
        if self.script_path:
            runner = ScriptRunner(self.shell, self.parser)
            success = runner.execute_script(self.script_path)
            if not success:
                print("Ошибка: Не удалось выполнить стартовый скрипт.", file=sys.stderr)

        print("--- Эмулятор оболочки ОС (Этап 2) ---")
        print("Введите 'exit' для выхода.")

        while True:
            try:
                prompt = self.get_prompt()
                user_input = input(prompt)

                # Пропускаем пустые строки
                if not user_input.strip():
                    continue

                elements = list(self.parser.parse(user_input))

                if not elements:
                    continue

                command = elements[0]
                args = elements[1:]

                self.shell.execute_command(command, args)

            except KeyboardInterrupt:
                print("\nДля выхода введите 'exit'")
            except Exception as e:
                print(f"Непредвиденная ошибка: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()