'''
---------------------------------------------
|   Author  :   Mason Moreland              |
|   Created :   September 07, 2018          |
|   Program :   I/O File Sorting Parser     |
---------------------------------------------
'''

import argparse

'''
---------------------------------------------------------------------------------------------
|   [FUNCTION] create_sorting_parser:                                                       |
|   -return type    : ArgumentParser                                                        |
|   -description    : initializes a parser with three arguments (input, output, reversed)   |
---------------------------------------------------------------------------------------------
'''
def create_sorting_parser():
    # initialize the parser
    parser = argparse.ArgumentParser(description='Order strings from an input file.')

    # required file - input file
    parser.add_argument('input', type=argparse.FileType('r'),
                        help='[REQUIRED] input file of choice', default="example_file")

    # optional file - output file
    parser.add_argument('-o', '--output', action='store', nargs='?', dest='output',
                        help='[OPTIONAL] output file of choice (default: output.txt)',
                        type=argparse.FileType('wb'), default="output.txt")

    # optional boolean - order the lines of file normally or reversed
    parser.add_argument('-r', '--reversed',  action='store_true', dest='reversed',
                        help='[OPTIONAL] normal alphabetical or reverse alphabetical order')
                        
    return parser