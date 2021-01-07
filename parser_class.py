class Parser:
    def __init__(self, parse_file):
        self.lines = open(parse_file, "r").readlines()

    def parser_func(self):
        sentences_number = len(self.lines)
        characters = 0

        for lines in self.lines:
            characters += len(lines)

        dic = {"sentences": self.lines, "stats": {"total_sentences": sentences_number, "total_chars": characters}}
        return dic
