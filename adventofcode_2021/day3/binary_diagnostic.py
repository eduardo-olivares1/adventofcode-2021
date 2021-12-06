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


def get_common_bit(arr, most_common=True, on_even=None):
    unique_elements = set(arr)
    count_cache = {}
    for element in unique_elements:
        count_cache[element] = 0

    for element in arr:
        if element in count_cache:
            count_cache[element] += 1

    if most_common == True:
        if len(count_cache) == 1 or count_cache["0"] == count_cache["1"]:
            return on_even
        else:
            common_bit = max(count_cache, key=count_cache.get)
        
    elif most_common == False:
        if len(count_cache) == 1 or count_cache["0"] == count_cache["1"]:
            return on_even
        else:
            common_bit = min(count_cache, key=count_cache.get)
        

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

# WARNING: HORRIFIC CODE BELOW
def get_rating(matrix, rating):
    for i in range(0, len(matrix[0])):
        tranposed_matrix = tranpose(matrix)
        if rating == "generator":
            common_bit = get_common_bit(tranposed_matrix[i], on_even="1")
        elif rating == "scrubber":
            common_bit = get_common_bit(tranposed_matrix[i], on_even="0", most_common=False)
        matrix = [el for el in matrix if el[i] == common_bit]
        if len(matrix) == 1:
            break

    binary_string = ""
    for bit in matrix[0]:
        binary_string += bit

    return int(binary_string, 2)


def get_life_support_rating(scrubber_rating, generator_rating):
    return scrubber_rating * generator_rating