def longest_word(s):


    words = s.split()
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest



print(longest_word("Hello darkness my old friend."))
