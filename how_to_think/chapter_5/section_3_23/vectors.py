def add_vectors(vector1, vector2):
    if len(vector1) != len(vector2):
        return None
    vector3 = []
    for v1, v2 in zip(vector1, vector2):  # zip combines multiple lists into one list of tuples
        vector3.append(v1 + v2)
    return vector3


if __name__ == "__main__":
    print(add_vectors([1, 1], [1, 1]))
    print(add_vectors([1, 2], [1, 4]))
    print(add_vectors([1, 2, 1], [1, 4, 3]))
