import sys
import os


class ScriptRunner:
    def __init__(self, shell, parser):
        self.shell = shell
        self.parser = parser

    def execute_script(self, filepath: str) -> bool:
        if not os.path.exists(filepath):
            print(f"Ошибка: Файл скрипта '{filepath}' не найден.", file=sys.stderr)
            return False

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            print(f"\n--- Запуск скрипта: {os.path.basename(filepath)} ---")

            for line_num, line in enumerate(lines, 1):

                clean_line = line.strip()



                if not clean_line or clean_line.startswith('#'):
                    continue

                print(f"{clean_line}")

                try:

                    elements = list(self.parser.parse(clean_line))
                    if not elements:
                        continue

                    command = elements[0]
                    args = elements[1:]


                    self.shell.execute_command(command, args)

                except Exception as e:
                    print(f"Ошибка выполнения команды в скрипте (строка {line_num}): {e}", file=sys.stderr)



            print("--- Скрипт завершен ---\n")
            return True

        except Exception as e:
            print(f"Критическая ошибка при чтении скрипта: {e}", file=sys.stderr)
            return False