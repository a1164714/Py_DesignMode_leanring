if __name__ == "__main__":
    lst = ["hello Alice", "hello Bob", "hello Eve"]
    lst_iter = iter(lst)
    print(lst_iter.__next__())
    print(lst_iter.__next__())
    print(lst_iter.__next__())
    print(lst_iter.__next__())
