'''
---------------------------------------------
|   Author  :   Mason Moreland              |
|   Created :   September 07, 2018          |
|   Program :   I/O File Sorting Parser     |
---------------------------------------------
'''

from cl_parser import create_sorting_parser

# initialize and assign sorting parser
parser = create_sorting_parser()

# access arguments from input
args = parser.parse_args()

# assign input from file to a string
lines = args.input.read()
# convert string of input from input file to array
arr = lines.split("\n")

# bool - check for ordered or reversed alphabetical sorting
isReverse = args.reversed

# sort the array in alphabetical order ignoring case sensitivity
arr.sort(key=str.casefold)

# reverse the array alphabetically reverse
if isReverse:
    arr.reverse()

# output to the file
args.output.write('\n'.join(arr).encode())

# close I/O files
args.input.close()
args.output.close()

# DEBUG - uncomment lines below to test parser
# print(arr)
# print(isReverse)
# print(lines)