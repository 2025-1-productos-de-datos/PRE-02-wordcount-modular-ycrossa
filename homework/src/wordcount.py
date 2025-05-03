# obtain a list of files in the input directory

from homework.src._internals.read_all_lines import read_all_lines
from homework.src._internals.write_count_words import write_count_words


def main():

    ## mover a la funcion "read_all_lines"
    all_lines = read_all_lines()

    ## mover a "preprocess_lines"
    all_lines = preprocess_lines(all_lines)

    ## mover "split_in_words"
    words = []
    for line in all_lines:
        words.extend(word.strip(",.!?") for word in line.split())

    ## mover a "count_words"
    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1

    # count the frequency of the words in the files in the input directory
    # counter = {}
    # for filename in input_file_list:
    #     with open("data/input/" + filename) as f:
    #         for l in f:
    #             for w in l.split():
    #                 w = w.lower().strip(",.!?")
    #                 counter[w] = counter.get(w, 0) + 1

    ##
    write_count_words(counter)


def preprocess_lines(all_lines):
    all_lines = [line.lower().strip() for line in all_lines]
    return all_lines


if __name__ == "__main__":
    main()
