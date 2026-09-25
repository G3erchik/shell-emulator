import shlex


class Parser:
    def parse(self, line: str) -> list[str]:
        return shlex.split(line)