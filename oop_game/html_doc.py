class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = f'<{name}>'
        self.end_tag = f'</{name}>'
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = ''  # DOCTYPE doesn't have end tag


class ContentsTag(Tag):

    def __init__(self, name, contents):
        super().__init__(name, contents)
        self._contents = []

    def _add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._contents.append(new_tag)

    def display(self, file=None):
        for tag in self._contents:
            self.contents += str(tag)

        super().display(file=file)


class Head(ContentsTag):

    def __init__(self, title=None):
        super().__init__('head', '')
        if title:
            super()._add_tag("title", title)


class Body(ContentsTag):

    def __init__(self):
        super().__init__('body', '')  # body contents will be built up separately

    def add_tag(self, name, contents):
        super()._add_tag(name, contents)


class HtmlDoc(object):

    def __init__(self, title=None):
        self._doc_type = DocType()
        self._head = Head(title=title)
        self._body = Body()

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


if __name__ == "__main__":
    my_page = HtmlDoc(title='Document title')  #
    my_page.add_tag('h1', 'Main heading')
    my_page.add_tag('h2', 'sub-heading')
    my_page.add_tag('p', 'This is a paragraph that will appear on the page')
    # my_page.display()
    with open('test.html', 'w') as test_doc:
        my_page.display(file=test_doc)
