import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    with open(file_name, "r") as file_obj:
        data = json.load(file_obj)
        if field in data:
            data = data[field]
        else:
            return None

    return data
    #file_path = os.path.join(cwd_path, file_name)

def linear_search(unordered_nums, key):
    list_idx = []
    count = 0
    values_dict = dict()
    for index, number in enumerate(unordered_nums):
        if number == key:
            list_idx.append(index)
            count = count + 1
        else:
            continue
    values_dict["positions"] = list_idx
    values_dict["count"] = count
    return values_dict

def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    print(linear_search(sequential_data, 9))

if __name__ == '__main__':
    main()