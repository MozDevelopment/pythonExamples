#!/usr/bin/python3
# iterators.py


def main():
    fh = open('lines.txt')
    for line in fh.readlines():
        print(line)

if __name__ == "__main__": main()
