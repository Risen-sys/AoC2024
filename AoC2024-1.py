from collections import Counter


def main():
    left, right = [], []
    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f:
            a, b = line.split()
            left.append(int(a))
            right.append(int(b))

    left.sort()
    right.sort()
    sum_of_diffs = sum(abs(a - b) for a, b in zip(left, right))

    print(f"Part 1: {sum_of_diffs}")

    count_right = Counter(right)
    similarity_score = sum(a * count_right[a] for a in left)

    print(f"Part 2: {similarity_score}")


if __name__ == "__main__":
    main()