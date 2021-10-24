from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        newData = data.split("\n")
        numberOfLines = len(newData)
        if numberOfLines == 1:
            print(">>> Single-line Comment")
            print(data)
        else:
            print(">>> Multi-line Comment")
            for row in newData:
                print(row)

    def handle_data(self, data):
        if data != "\n":
            print(">>> Data")
            print(data)


lines = int(input())
parser = MyHTMLParser()
text = ""
for line in range(lines):
    text += input() + "\n"
parser.feed(text)
parser.close()
