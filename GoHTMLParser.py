from HTMLParser import HTMLParser


class Record:
    def __init__(self, a, p):
        self.a = a
        self.p = p

    def __str__(self):
        return "a: " + self.a + " p:" + self.p


class GoHTMLParser(HTMLParser):
    tableStarted = False
    dataStarted = False
    recordStarted = False
    recordList = []
    record = None
    tag = ''
    prevTag = ''

    def handle_starttag(self, tag, attrs):
        if (tag == "table"):
            for attr in attrs:
                if (attr == ('class', 'list_table material_modifications')):
                    self.tableStarted = True

        if ((tag == "tr") and self.tableStarted == True):
            for attr in attrs:
                if (attr == ('class', 'change')):
                    self.record = Record('', '')
                    self.recordStarted = True

        if ((tag == "p" or tag == "a") and self.tableStarted == True):
            self.dataStarted = True
            self.prevTag = self.tag
            self.tag = tag
        else:
            self.dataStarted = False

    def handle_endtag(self, tag):
        if ((tag == "p" or tag == "a") and self.tableStarted == True):
            self.tag = self.prevTag

        if (tag == "table" and self.tableStarted == True):
            self.tableStarted = False

        if (tag == "tr" and self.tableStarted == True and self.recordStarted == True):
            if self.record != None:
                self.recordList.append(self.record)

    def handle_data(self, data):
        nonEmptyData = data.strip()
        if self.tableStarted == True and self.dataStarted == True and nonEmptyData and self.record != None:
            if self.tag == 'a':
                self.record.a = nonEmptyData
            if self.tag == 'p':
                if nonEmptyData.startswith("Merge"):
                    self.record = None
                else:
                    self.record.p = nonEmptyData
