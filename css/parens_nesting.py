def check_parens(sentence, open_p_index):
    # start with open nested paren count, set to 0
    open_nested_p = 0
    # starting position is one further than opener
    position = open_nested_p + 1

    while position < len(sentence):
        # if current character is an opener, add to count
        char = sentence[position]
        if (char == "("):
            open_nested_p += 1
        # if char is closing and there is not extra openers
        elif (char ==")"):
            if open_nested_p == 0:
                # return position of closing paren
                return position
            # otherwise minus the count
            else:
                open_nested_p -= 1
        # iterate through the sentence
        position += 1


    # got all the way through and no closing
    return "No closing! Error"