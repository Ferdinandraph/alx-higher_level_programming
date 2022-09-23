#!/usr/bin/python3
if __name__ == "__main__":
    """progam that adds argument to infinite"""
    import sys

    a = sys.argv[1:]
    su = sum(int(i) for i in a)
    print(su)
