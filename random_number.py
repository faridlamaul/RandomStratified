import random
import json
import csv


def csv_to_txt(csv_file, txt_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        data = list(reader)

    with open(txt_file, 'w') as file:
        for row in data:
            # if row is not empty
            if row:
                file.write('\n'.join(row) + '\n')

    print(f"Data from '{csv_file}' has been successfully written to '{txt_file}'.")


strata = [
    ("class 1", 862), ("class 2", 31), ("class 3", 14), ("class 4", 6),
    ("class 5", 10), ("class 6", 8), ("class 7", 4), ("class 8", 1),
    ("class 9", 1), ("class 10", 1), ("class 11", 2), ("class 12", 10),
    ("class 13", 0), ("class 14", 1), ("class 15", 1), ("class 16", 2),
    ("class 17", 1), ("class 18", 1), ("class 19", 1), ("class 20", 3),
    ("class 21", 1), ("class 22", 1), ("class 23", 2), ("class 24", 1),
    ("class 25", 1), ("class 26", 0), ("class 27", 0), ("class 28", 0),
    ("class 29", 1), ("class 30", 3), ("class 31", 1), ("class 32", 2),
    ("class 33", 2), ("class 34", 3), ("class 35", 2), ("class 36", 0),
    ("class 37", 1), ("class 38", 1), ("class 39", 1), ("class 40", 1),
    ("class 41", 0), ("class 42", 1), ("class 43", 0), ("class 44", 0),
    ("class 45", 1), ("class 46", 0), ("class 47", 2), ("class 48", 0),
    ("class 49", 0), ("class 50", 0), ("class 51", 0), ("class 52", 0),
    ("class 53", 0), ("class 54", 0), ("class 55", 0), ("class 56", 1),
    ("class 57", 1), ("class 58", 0), ("class 59", 0), ("class 60", 0),
    ("class 61", 1), ("class 62", 0), ("class 63", 0), ("class 64", 1),
    ("class 65", 0), ("class 66", 0), ("class 67", 1), ("class 68", 1),
    ("class 69", 1), ("class 70", 0), ("class 71", 0), ("class 72", 0),
    ("class 73", 0), ("class 74", 0), ("class 75", 1), ("class 76", 0),
    ("class 77", 0), ("class 78", 0), ("class 79", 1), ("class 80", 0),
    ("class 81", 0), ("class 82", 0), ("class 83", 0), ("class 84", 0),
    ("class 85", 0), ("class 86", 0), ("class 87", 0), ("class 88", 0),
    ("class 89", 0), ("class 90", 0), ("class 91", 0), ("class 92", 0),
    ("class 93", 0), ("class 94", 1), ("class 95", 1), ("class 96", 0),
    ("class 97", 0), ("class 98", 0), ("class 99", 0), ("class 100", 1),
]

for a in range(1, 11):
    start = 0
    end = 88000
    for i, total_data in strata:
        total = int(a * total_data)
        data = [random.randint(start, end) for _ in range(0, total)]
        result = json.dumps({"data": data})
        with open(f'data/RandStratified{a * 1000}/{i.replace(" ", "_")}.json', "w") as f:
            f.write(result)
        start = end
        end += 88000

    data = []
    for i in range(1, 101):
        data.append(json.load(open(f"data/RandStratified{a * 1000}/class_{i}.json"))["data"])

    with open(f'data/RandStratified{a * 1000}/RandStratified{a * 1000}.csv', "w") as f:
        write = csv.writer(f)
        write.writerows(data)

    csv_to_txt(f'data/RandStratified{a * 1000}/RandStratified{a * 1000}.csv', f'data/RandStratified{a * 1000}/RandStratified{a * 1000}.txt')
