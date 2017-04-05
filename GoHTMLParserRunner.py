import sys
from GoHTMLParser import GoHTMLParser

input_file = str(sys.argv[1])
output_file = str(sys.argv[2])
file = open(output_file, 'w+')
parser = GoHTMLParser()
parser.feed(open(input_file, 'r').read())

for r in parser.recordList:
    with open(output_file, 'a+') as file:
        file.write(r.a+";"+r.p+"\n")

