def arb_lex_sort(strings, letter_precedence):

    max_string_len = 0
    for string in strings:
        string_len = len(string)
        if string_len > max_string_len:
            max_string_len = string_len

    ordered_strings = strings[:]
    new_ordered_strings = strings[:]

    for i in range(max_string_len - 1, -1, -1):

        next_string_index = 0

        for string in ordered_strings:
            if i >= len(string):
                new_ordered_strings[next_string_index] = string
                next_string_index += 1

        for letter in letter_precedence:
            for string in ordered_strings:
                if i < len(string) and string[i] == letter:
                    new_ordered_strings[next_string_index] = string
                    next_string_index += 1

        ordered_strings, new_ordered_strings = new_ordered_strings, ordered_strings

    return ordered_strings


if __name__ == "__main__":
    example_inputs = [(["acb", "abc", "bca"], "abc"),
                      (["acb", "abc", "bca"], "cba"),
                      (["aaa","aa",""], "a")]
    for i, example_input in enumerate(example_inputs):
        print("Example input #{}: {}".format(i + 1, example_input))
        print("Example output #{}: {}\n".format(i + 1, arb_lex_sort(*example_input)))
