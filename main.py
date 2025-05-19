from stats import get_num_words
from stats import character_counts
from stats import sorted_list
from stats import print_report
import sys


def main():
    # text = "books/frankenstein.txt"
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = sys.argv[1]
    print_report(text)

main()  