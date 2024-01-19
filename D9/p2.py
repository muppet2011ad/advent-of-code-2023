from itertools import pairwise

def differences(seq: list[int]) -> list[int]:
    return list(map(lambda x: x[1] - x[0], pairwise(seq)))

def all_differences(seq: list[int]) -> list[list[int]]:
    difference_lists = [seq]
    while not all(map(lambda x: x == 0, difference_lists[-1])):
        difference_lists.append(differences(difference_lists[-1]))
    return difference_lists

def predict_forwards(seq: list[int]) -> int:
    difference_lists = all_differences(seq)
    for lower_level, higher_level in pairwise(difference_lists[::-1]):
        higher_level.append(higher_level[-1] + lower_level[-1])
    return difference_lists[0][-1]

def predict_backwards(seq: list[int]) -> int:
    difference_lists = all_differences(seq)
    for lower_level, higher_level in pairwise(difference_lists[::-1]):
        higher_level.insert(0, higher_level[0] - lower_level[0])
    return difference_lists[0][0]

with open("D9/data") as f:
    lines = f.readlines()

    sequences = map(lambda x: list(map(int, x)), map(lambda line: line.strip(" \r\n").split(), lines))

    predictions = map(predict_backwards, sequences)

    print(sum(predictions))