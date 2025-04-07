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
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as file_obj:
        data = json.load(file_obj)
        if field in data:
            data = data[field]
        else:
            return None

    return data

def linear_search(unordered_nums, key):
    list_idx = [] #+1
    count = 0 # +1
    values_dict = dict() # +1
    for index, number in enumerate(unordered_nums): # +n
        if number == key: # +n
            list_idx.append(index) # +n
            count = count + 1 #+n
        else:
            continue
    values_dict["positions"] = list_idx # +1
    values_dict["count"] = count # +1    - SLOZITOST 4n + 4 == O(n) - JEDEN CYKLUS, CO JDE PRES CELY SEZNAM
    return values_dict

def pattern_search(dna_sequence, key):
    i = 0
    triplets = len(key)
    idx_set = set()
    dna_sequence = "ATGACGGAATATAAGCTAGGTGGTGGCTGGGCAGTCCGCGCTGATAGGGCAAGAGTGCGCGTACCATACCACGCTAAGCCATATAGGGCATCAGTCAGCCTGGCA"
    for i in range(len(dna_sequence) - (triplets - 1)):
        if dna_sequence[i:triplets] == key:
            idx_set.add(i)
            i = i + 1
            triplets = triplets + 1
        else:
            i = i + 1
            triplets = triplets + 1
    return idx_set

def main():
    sequential_data = read_data("sequential.json", "dna_sequence")
    print(sequential_data)
    print(linear_search(sequential_data, 9))
    print(pattern_search(sequential_data, "ATA"))

if __name__ == '__main__':
    main()