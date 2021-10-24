from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def print_attrs(self, attrs):
        for attr in attrs:
            print("->", attr[0], ">", attr[1])

    def handle_starttag(self, tag, attrs):
        print(tag)
        self.print_attrs(attrs)

    def handle_startendtag(self, tag, attrs):
        print(tag)
        self.print_attrs(attrs)


lines = int(input())
parser = MyHTMLParser()
text = ""
for line in range(lines):
    text += input() + "\n"
parser.feed(text)
parser.close()
