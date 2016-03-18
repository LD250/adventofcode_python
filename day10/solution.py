def main():
    input_data = '1113122113'
    def look_and_say(look):
        prev_digit = look[0]
        prev_count = 1
        say = ''
        for digit in look[1:]:
            if digit == prev_digit:
                prev_count += 1
            else:
                say += "%s%s" % (prev_count, prev_digit)
                prev_count = 1
                prev_digit = digit
        say += "%s%s" % (prev_count, prev_digit)
        return say
    new_input_data = input_data
    for _ in xrange(40):
        new_input_data = look_and_say(new_input_data)
    print len(new_input_data)
    for _ in xrange(10):
        new_input_data = look_and_say(new_input_data)
    print len(new_input_data)
if __name__ == "__main__":
    main()
