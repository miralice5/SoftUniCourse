dictionary = {
    1: "а",
    2: "б",
    3: "в",
    4: "г",
    5: "д",
    6: "е",
    7: "ж",
    8: "з",
    9: "и",
    10: "й",
    11: "к",
    12: "л",
    13: "м",
    14: "н",
    15: "о",
    16: "п",
    17: "р",
    18: "с",
    19: "т",
    20: "у",
    21: "ф",
    22: "х",
    23: "ц",
    24: "ч",
    25: "ш",
    26: "щ",
}

message = input().split(', ')

for m in message:
    print(dictionary[int(m)], end='')