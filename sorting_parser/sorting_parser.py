import argparse

def create_sorting_parser():
    """
    Initializes a parser with three arguments: input, output, reversed
    Returns ArgumentParser object
    """

    # Initialize the parser
    parser = argparse.ArgumentParser(description='Order strings from an input file.')

    # Required file - input file
    parser.add_argument('input', type=argparse.FileType('r'),
                        help='[REQUIRED] input file of choice', default="example_file")

    # Optional file - output file
    parser.add_argument('-o', '--output', action='store', nargs='?', dest='output',
                        help='[OPTIONAL] output file of choice (default: output.txt)',
                        type=argparse.FileType('wb'), default="output.txt")

    # Optional boolean - order the lines of file normally or reversed
    parser.add_argument('-r', '--reversed',  action='store_true', dest='reversed',
                        help='[OPTIONAL] normal alphabetical or reverse alphabetical order')
                        
    return parser

if __name__ == "__main__":
    # Initialize and assign sorting parser
    parser = create_sorting_parser()

    # Access arguments from input
    args = parser.parse_args()

    # Assign input from file to a string
    lines = args.input.read()

    # Convert string of input from input file to array
    arr = lines.split("\n")

    # Bool - check for ordered or reversed alphabetical sorting
    isReverse = args.reversed

    # Sort the array in alphabetical order ignoring case sensitivity
    arr.sort(key=str.casefold)

    # Reverse the array alphabetically reverse
    if isReverse:
        arr.reverse()

    # Output to the file
    args.output.write('\n'.join(arr).encode())

    # Close I/O files
    args.input.close()
    args.output.close()

