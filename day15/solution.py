def main():
    # Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
    # Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
    # Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
    # Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8
    ingredients = [{'cap': 2, 'dur': 0, 'fla': -2, 'tex': 0, 'cal': 3},
                   {'cap': 0, 'dur': 5, 'fla': -3, 'tex': 0, 'cal': 3},
                   {'cap': 0, 'dur': 0, 'fla': 5, 'tex': -1, 'cal': 8},
                   {'cap': 0, 'dur': -1, 'fla': 0, 'tex': 5, 'cal': 8}]

    def prop_score(prop, s, b, c, a):
        return max(0, sum([ingredients[i][prop] * ingr for (i, ingr) in [(0, s),(1, b),(2, c),(3, a)]]))

    score = 0
    score_cal = 0
    for s in xrange(1, 100):
        for b in xrange(1, 100 - s):
            for c in xrange(1, 100 - s - b):
                a = 100 - s - b - c
                props = []
                for prop in ['cap', 'dur', 'fla', 'tex']:
                    props.append(prop_score(prop, s, b, c, a))
                new_score = reduce(lambda x, y: x * y, props, 1)
                score = max(score, new_score)
                if prop_score('cal', s, b, c, a) == 500:
                    score_cal = max(score_cal, new_score)
    print(score)
    print(score_cal)


if __name__ == "__main__":
    main()
