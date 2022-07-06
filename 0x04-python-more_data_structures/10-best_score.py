#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        max_score = max(a_dictionary.values())
        for name, score in a_dictionary.items():
            if score == max_score:
                return name
    else:
        return None
