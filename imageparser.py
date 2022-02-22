from html.parser import HTMLParser


class ImageLinkHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.__linklist = []

    def handle_starttag(self, tag, attrs):
        if len(attrs) > 4:
            imginfo = attrs[3]
            if "data-src" in imginfo:
                self.__linklist.append(imginfo[1])

    @property
    def linklist(self):
        self.__linklist.pop(0)
        i = 0
        while i < 5:
            self.__linklist.pop()
            i += 1
        return self.__linklist
