def main():
    f = open('input.txt')
    content = f.read()
    lines = [l for l in content.split('\n') if l]
    naughty_strings = ['ab', 'cd', 'pq', 'xy']
    vowels = 'aeiou'
    def is_nice(word):
        for ns in naughty_strings:
            if ns in word:
                return False
        vowels_num = reduce(lambda c, l: c + (1 if l in vowels else 0), word, 0)
        if vowels_num < 3:
            return False
        for i in xrange(len(word) - 1):
            if word[i] == word[i + 1]:
                return True
        return False
    nice_words = reduce(lambda c, l: c + (1 if is_nice(l) else 0), lines, 0)
    print(nice_words)

    def is_nice2(word):
        maybe_nice = False
        for i in xrange(len(word) - 2):
            maybe_nice = word[i:i + 2] in word[i + 2:]
            if maybe_nice:
                break

        if not maybe_nice:
            return False

        for i in xrange(len(word) - 2):
            if word[i] == word[i + 2]:
                return True
        return False

    nice_words = reduce(lambda c, l: c + (1 if is_nice2(l) else 0), lines, 0)
    print(nice_words)


if __name__ == "__main__":
    main()
