from collections import Counter

def read_input(file_path):
    left_list = []
    right_list = []
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.strip().split())
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list

def calculate_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    return total_distance


def calculate_similarity_score(left_list, right_list):
    right_count = Counter(right_list)
    
    similarity_score = 0
    
    for num in left_list:
        if num in right_count:
            similarity_score += num * right_count[num]
    
    return similarity_score

left_list, right_list = read_input("input.txt")

# Part One:
total_distance = calculate_total_distance(left_list, right_list)
print("Total distance:", total_distance)

# Part Two:
similarity_score = calculate_similarity_score(left_list, right_list)
print("Similarity score:", similarity_score)