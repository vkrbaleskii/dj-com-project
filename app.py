from parser_class import Parser

import time

start_time = time.time()


def main():
    new_parser = Parser("example.txt")
    text = new_parser.parser_func()
    print(text.get("stats", {}).get("total_sentences", 0))


if __name__ == '__main__':
    main()

print("%s seconds pass for reading and printing file" % (time.time() - start_time))
