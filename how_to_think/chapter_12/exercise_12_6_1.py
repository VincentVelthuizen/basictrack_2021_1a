def readposint() -> int:
    """
    This function asks a user for a positive integer and doesn't let up until it is provided.
    It is a deviation from what is literally asked in the exercise,
        but I hope this shows what can be done using exceptions.
    """

    positive_int = -1
    while positive_int < 0:
        read = input("Please provide a positive integer: ")
        try:
            positive_int = int(read)
            if positive_int < 0:
                raise ValueError
        except ValueError:
            print("\t", read, "is not a positive integer.")

    return positive_int


if __name__ == "__main__":
    print(readposint())
