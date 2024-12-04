from typing import Tuple, List

file_name = "data.txt"

def prepare_data(file_name:str) -> list[int]:
    # Read the dataset from the file
    with open(file_name, "r") as file:
        # Read the content and split it into individual numbers
        data = file.read().replace(",", " ").split()
        data = [int(num) for num in data]
        return data

def prepare_arrays(data: list[int]) -> tuple[list[int], list[int]]:
    array_coords_1 = sorted(data[::2])
    array_coords_2 = sorted(data[1::2])
    return array_coords_1, array_coords_2

def get_diffs(array_coords_1: list[int], array_coords_2: list[int]) -> list[int]:
    diff_array = []
    for number in array_coords_1:
        diff = abs(number - array_coords_2[array_coords_1.index(number)])
        diff_array.append(diff)

    return diff_array


data = prepare_data(file_name)
array_coords_1, array_coords_2 = prepare_arrays(data)
diffs = get_diffs(array_coords_1, array_coords_2)

result = sum(diffs)
print(result)