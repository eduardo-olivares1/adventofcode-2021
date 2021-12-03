def tranpose(matrix):
    transposed_matrix = []

    # Create required arrs for transposing (idk if thats a word)
    for element in matrix[0]:
        transposed_matrix.append([])

    # For each arr
    for i in range(0, len(matrix)):
        # For each number in that arr
        for j in range(0, len(matrix[i])):
            transposed_matrix[j].append(matrix[i][j])
    return transposed_matrix


def get_common_bit(arr):
    unique_elements = set(arr)
    count_cache = {}
    for element in unique_elements:
        count_cache[element] = 0

    for element in arr:
        if element in count_cache:
            count_cache[element] += 1

    common_bit = max(count_cache, key=count_cache.get)

    return common_bit


def invert_binary(binary_string):
    inverted_binary = ""
    for i in range(0, len(binary_string)):
        if binary_string[i] == "0":
            inverted_binary += "1"
        elif binary_string[i] == "1":
            inverted_binary += "0"
    return inverted_binary


def get_gamma_binary_string(matrix):
    gamma_rate_binary = ""
    for arr in matrix:
        gamma_rate_binary += get_common_bit(arr)
    return gamma_rate_binary


def get_epsilon_binary_string(gamma_rate_binary):
    epsilon_rate_binary = invert_binary(gamma_rate_binary)
    return epsilon_rate_binary


def get_power_consumption(gamma_rate, epsilon_rate):
    return gamma_rate * epsilon_rate
