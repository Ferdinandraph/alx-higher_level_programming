#!/usr/bin/python3
if __name__ == "__main__":
    """printing all names defined"""
    import hidden_4

    namesOfh = dir(hidden_4)
    for name in namesOfh:
        if name[:2] != "__":
            print(name)
