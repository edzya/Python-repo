# Task 1

def get_min_avg_max(sequence):
    print(min(sequence), sum(sequence)/len(sequence), max(sequence))
    return min(sequence), sum(sequence)/len(sequence), max(sequence)


def get_min_med_max(seq):
    sort_seq = sorted(seq)
    print(sort_seq)
    median = 2

    if len(sort_seq) % 2 == 1:
        median = int((len(sort_seq))/2)
        median = sort_seq[median]
    else:
        median_1 = int((len(sort_seq))/2)
        median_2 = median_1 - 1
        if type(seq) == str:
            median = (sort_seq[median_2] + sort_seq[median_1])
        else:
            median = (sort_seq[median_1] + sort_seq[median_2])/2

    return min(seq), median, max(seq)


print(get_min_med_max((0, 10, 1, 9, 5, 7)))
print(get_min_med_max([0, 10, 1, 9]))
print(get_min_med_max("baac"))

print(get_min_med_max([2, 2, 9, 9, 4, 3]))
print(get_min_med_max([2, 2, 9, 4, 3]))

# Task 2
# get_min_avg_max([0, 10, 1, 9])
