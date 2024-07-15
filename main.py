from collections import Counter

# Function to sort the strings with 2 or 3 same characters


def contains_same_chars(string, n):
    count = Counter(string)
    return any(value == n for value in count.values())


def sort_string_with_2_same_chars(strings):
    return [string for string in strings if contains_same_chars(string, 2)]


def sort_string_with_3_same_chars(strings):
    return [string for string in strings if contains_same_chars(string, 3)]

# Function to compare the strings


def one_different_char(string1, string2):
    differ = 0
    for c1, c2 in zip(string1, string2):
        if c1 != c2:
            differ += 1
            if differ > 1:
                return False
    return differ == 1


def find_strings_with_one_different_char(strings):
    pairs = []
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if one_different_char(strings[i], strings[j]):
                pairs.append((strings[i], strings[j]))
    return pairs


def keep_commons_chars(string1, string2):
    result = []
    for c1, c2 in zip(string1, string2):
        if c1 == c2:
            result.append(c1)
    return "".join(result)

# Main function to find the boxes which contains robot parts


def main_function(li):
    two_chars = sort_string_with_2_same_chars(li)
    two_chars = list(set(two_chars))
    three_chars = sort_string_with_3_same_chars(li)
    three_chars = list(set(three_chars))
    boxes_with_2_same_chars = len(two_chars)
    boxes_with_3_same_chars = len(three_chars)
    bender_boxes = find_strings_with_one_different_char(li)
    print(f"Number of boxes with ID which contains 2 same chars: {boxes_with_2_same_chars}")
    print(f"Number of boxes with ID which contains 3 same chars: {boxes_with_3_same_chars}")
    print(f"Checksum: 247 * 39 = {boxes_with_2_same_chars * boxes_with_3_same_chars}")
    for bender_box in bender_boxes:
        print(f"Boxes which contains robot parts are: \n {bender_box[0]} and \n {bender_box[1]}")
        string1, string2 = bender_box
        commons = keep_commons_chars(string1, string2)
        print(f"Commons letter between the boxes are: \n {commons}")
        break

# The id boxes list


id_collection1 = []
with open("input.txt") as file:
    for line in file:
        id_collection1.append(line.strip())


# Call the main function


main_function(id_collection1)