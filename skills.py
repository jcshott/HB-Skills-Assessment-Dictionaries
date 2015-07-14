# To work on the advanced problems, set to True
ADVANCED = True


def count_unique(input_string):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """
    #loop over string differentiating each word by a space. 

    word_list = input_string.split() #pull out words in string by differentiating on space

    dictionary = {}

    for word in word_list:          #if word not in dictionary, create the value at 1.
        dictionary[word] = dictionary.get(word, 0) + 1 #using heather's suggestion

#my first method
        # if word not in dictionary:
        #     dictionary[word] = 1
        # else:
        #     dictionary[word] = dictionary[word] + 1 #if it is in dictionary, add one to value


    return dictionary


def find_common_items(list1, list2):
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between
    the lists.

    IMPORTANT: you may not use 'if ___ in ___' or the method 'index'.


    For example:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in both lists, return it each
    time:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(find_common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """
    #TODO: turn this into list comprehension (nested loops)

    common = []

    for item1 in list1:         #loop through every value in list 1
        for item2 in list2:     #each iteration, loop through each item in list 2
            if item1 == item2:  #comparing current in list1 to each item in list2
                common.append(item1) #if they match, add to list
    
    return common


def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `find_common_items`, this should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """
    #iterate through list1, if there is a match in list2, add it to the "common" list.
    common = [item for item in list1 if item == item in list2]

    # for item in list1:
    #     if item == item in list2:
    #         common.append(item)

    return common


def get_sum_zero_pairs(input_list):
    """Given a list of numbers,
    return list of x,y number pair lists where x + y == 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """

    sum_zero_pair_list = []
    input_set = set(input_list)

    #iterate through each number in the input list.  
    for number in input_set:
    #heather's suggested approach with sets but when i run outside this assignment as test, its fine, here i get 2 copies
        if number > 0 and -number in input_set
        
            sum_zero_pair_list.append((-number, number))


#my way
    #     for n in range(len(input_list) - input_list.index(number)): 
    #         #create a tuple of each number plus every other number in the list, including itself, using index.
    #         #the range is set up so that you won't get an index out of range error 
    #         sum_pair_tuple = (number, input_list[input_list.index(number) + n]) 
        
    #         #evaluate the current pair and if the first and last equal 0, put it in the dictionary as a key-value pair
    #         if sum_pair_tuple[0] + sum_pair_tuple[1] == 0:
    #             sum_zero_pair_dictionary[sum_pair_tuple[0]] = sum_pair_tuple[1]

    # #to weed duplicate pairs (i.e. 1, -1 and -1,1), if a key is also a value, delete it. 
    # #only exception is zero because it is the only number that you can add to itself to get zero
    # for key in sum_zero_pair_dictionary.keys():
    #     if key in sum_zero_pair_dictionary.values() and key != 0:
    #         del sum_zero_pair_dictionary[key]

    return sum_zero_pair_list


def remove_duplicates(words):
    """Given a list of words, return the list with duplicates removed
    without using a Python set.

    For example:

        >>> sorted(remove_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(remove_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """

    dictionary = {}

    #assign each word in the input "words" list as a dictionary key (no need for a value)
    #this automatically takes out duplicates because dict. keys must be unique
    for word in words:
        dictionary[word] = None

    return dictionary.keys()


def encode(phrase):
    """Given a phrase, replace all "e" characters with "p",
    replace "a" characters with "d", replace "t" characters with "o",
    and "i" characters with "u". Return the encoded string.

    For example:

        >>> encode("You are a beautiful, talented, brilliant, powerful musk ox.")
        'You drp d bpduouful, odlpnopd, brulludno, powprful musk ox.'
    """

    phrase = phrase.replace("e", "p")
    phrase = phrase.replace("a", "d")
    phrase = phrase.replace("t", "o")
    phrase = phrase.replace("i", "u")
    
    return phrase


def sort_by_word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """

    dictionary_word_lengths = {}
    word_length_list = []

    # iterate through words in the input list and set key to length of word, value to a list of the word.
    # if the word length is already in, add to the list

    for item in words:
        dictionary_word_lengths.setdefault(len(item), [])
        dictionary_word_lengths[len(item)].append(item)

    # for values in dictionary_word_lengths.values():
    #     # print dictionary_word_lengths.values()
    #     # sorted_values = dictionary_word_lengths.get(values.sort)
    #     print values.sort()


        # if len(item) not in dictionary_word_lengths:
        #     dictionary_word_lengths[len(item)] = [item]
        # else:
        #     dictionary_word_lengths[len(item)].append(item)

    print sorted(dictionary_word_lengths.items())



def get_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> get_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> get_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """

    word_list = phrase.split()

    dictionary_pirate = {
        "sir": "matey",
        "hotel": "fleabag inn", 
        "student": "swabbie",
        "boy": "matey",
        "madam": "proud beauty",
        "professor": "foul blaggart",
        "restaurant": "galley",
        "your ": "yer",
        "excuse": "arr",
        "students": "swabbies",
        "are": "be",
        "lawyer": "foul blaggart",
        "the": "th'",
        "restroom": "head",
        "my": "me",
        "hello": "avast",
        "is": "be",
        "man": "matey"}

    for word in word_list:
        if word in dictionary_pirate.keys():
            new_word = dictionary_pirate.get(word)
            word_list[word_list.index(word)] = new_word
    
    return " ".join(word_list) 

# End of skills. See below for advanced problems.
# To work on them, set ADVANCED=True at the top of this file.
############################################################################


def adv_get_top_letter(input_string):
    """Given an input string, return a list of letter(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the letters in the returned
    list should be alphabetical.

    For example:
        >>> adv_get_top_letter("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:
        >>> adv_get_top_letter("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Spaces do not count as letters.

    """
    input_letters = list(input_string.replace(" ", ""))

    dict_letters = {}

    for letter in input_letters:
        if letter not in dict_letters:
            dict_letters[letter] = 1
        else:
            dict_letters[letter] = dict_letters[letter] + 1

    items = dict_letters.items()
    sorted_list = sorted(items, key=lambda letter: letter[1])

    long_word_list = [sorted_list[-1][0]]

    for tuple_words in sorted_list[: -1]:
        if tuple_words[1] == sorted_list[-1][1]:
            long_word_list.append(tuple_words[0])
    
    sorted_list = sorted(long_word_list)
    return sorted_list

def adv_alpha_sort_by_word_length(words):
    """    
    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.
    Now try doing it with only one call to .sort() or sorted(). What does the
    optional "key" argument for .sort() and sorted() do?

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """
 #I couldn't get this one to work.... :(

    dictionary_word_lengths = {}
    word_length_list = []

    # iterate through words in the input list and set key to length of word, value to a list of the word.
    # if the word length is already in, add to the list

    for item in words:
        dictionary_word_lengths.setdefault(len(item), [])
        dictionary_word_lengths[len(item)].append(item).sort

    return sorted(dictionary_word_lengths.items())


##############################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)

if __name__ == "__main__":
    print
    import doctest
    for k, v in globals().items():
        if k[0].isalpha():
            if k.startswith('adv_') and not ADVANCED:
                continue
            a = doctest.run_docstring_examples(v, globals(), name=k)
    print "** END OF TEST OUTPUT"
    print
