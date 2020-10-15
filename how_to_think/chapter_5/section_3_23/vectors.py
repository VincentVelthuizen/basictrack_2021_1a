def add_vectors(vector1, vector2):
    if len(vector1) != len(vector2):
        return None
    vector3 = []
    for v1, v2 in zip(vector1, vector2):  # zip combines multiple lists into one list of tuples
        vector3.append(v1 + v2)
    return vector3


def scalar_mult(scalar, vector):
    mult_vector = []
    for element in vector:
        mult_vector.append(scalar * element)
    return mult_vector


def dot_product(vec1, vec2):
    if len(vec1) != len(vec2):
        return None
    products = []
    for v1, v2 in zip(vec1, vec2):
        products.append(v1 * v2)

    sum_product = 0
    for product in products:
        sum_product += product

    return sum_product


if __name__ == "__main__":
    print(add_vectors([1, 1], [1, 1]))
    print(add_vectors([1, 2], [1, 4]))
    print(add_vectors([1, 2, 1], [1, 4, 3]))
    print()

    print(scalar_mult(5, [1, 2]))
    print(scalar_mult(3, [1, 0, -1]))
    print(scalar_mult(7, [3, 0, 5, 11, 2]))
    print()

    print(dot_product([1, 1], [1, 1]))
    print(dot_product([1, 2], [1, 4]))
    print(dot_product([1, 2, 1], [1, 4, 3]))
