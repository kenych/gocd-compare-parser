import unittest

from GoHTMLParser import GoHTMLParser


class GoHTMLParserTest(unittest.TestCase):
    def test_init_time(self):
        parser = GoHTMLParser()
        parser.feed(open('gooutput.html', 'r').read())

        for r in parser.recordList:
            print 'a: ' + r.a
            print 'p: ' + r.p

# add test cases


if __name__ == '__main__':
    unittest.main()
