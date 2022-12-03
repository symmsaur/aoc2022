#!/usr/bin/env python3

def score(move):
    shape_scores = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    beats = {
        "X": "C",
        "Y": "A",
        "Z": "B",
    }
    loses = {
        "X": "B",
        "Y": "C",
        "Z": "A",
    }
    score = shape_scores[move[1]]
    if beats[move[1]] == move[0]:
        score += 6
    elif loses[move[1]] == move[0]:
        pass
    else:
        score += 3
    return score


def corrected_score(move):
    shape_scores = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    if move[1] == "X":
        if move[0] == "A":
            return shape_scores["Z"]
        elif move[0] == "B":
            return shape_scores["X"]
        else:  # move[0] == "C":
            return shape_scores["Y"]
    elif move[1] == "Y":
        if move[0] == "A":
            return 3 + shape_scores["X"]
        elif move[0] == "B":
            return 3 + shape_scores["Y"]
        else:  # move[0] == "C":
            return 3 + shape_scores["Z"]
    else:  # move[1] == "Z":
        if move[0] == "A":
            return 6 + shape_scores["Y"]
        elif move[0] == "B":
            return 6 + shape_scores["Z"]
        else:  # move[0] == "C":
            return 6 + shape_scores["X"]


def main():
    with open("input") as data:
        moves = [line.split() for line in data.readlines()]
    scores = [score(move) for move in moves]
    total = sum(scores)
    print(f"Part One: {total}")
    corrected_scores = [corrected_score(move) for move in moves]
    corrected_total = sum(corrected_scores)
    print(f"Part Two: {corrected_total}")


if __name__ == "__main__":
    main()
