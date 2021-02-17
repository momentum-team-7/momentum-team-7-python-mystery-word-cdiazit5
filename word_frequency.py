STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    # """Read in `file` and print out the frequency of words in that file."""
    text_counter = {}
    with open(file) as open_file:
        text = open_file.read()
        text = text.lower()
        text_list = text.split()
        text_list_dup = text_list.copy()

        # read_file = open_file.read() 

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for element in text:
            if element in punctuations:
                text = text.replace(element,"")
                text = text.replace("\n"," ")
            
        for word in text_list:
            if word in STOP_WORDS:
                text_list_dup.remove(word)
            elif word not in text_counter:
                unsorted_counter = text_list_dup.count(word)
                text_counter[word] = unsorted_counter

        sorted_counter = sorted(text_counter.values(), reverse =True)
        # print(sorted_counter)
        sorted_dictionary = {}
        for index in sorted_counter:
            for key in text_counter.keys():
                if sorted_dictionary[key] == index:
                    sorted_dictionary[key] = text_counter[key]
        
        for key in sorted_dictionary:
            print(key," | ", sorted_dictionary[key])
        
        print(sorted_dictionary)
        print(text_list_dup)







    # print('read file', read_file)

    # -remove puncuation (jupt note 7)
    # -normalize all words to lowercase
    # -remove stop words -- words used so frequently they are ignored
        # check each word and see if it is equal to one of the stop words/if its in the list
        # conditional with if
    # -go through the file word by word and keep a count of how often each word is used
    # probably use a dictionry to store this, for counting purposes: keys -> words, values -> # of occurerences
    # pass


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
