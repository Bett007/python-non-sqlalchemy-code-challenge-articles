class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(self, "_title"):
            return

        if type(value) is not str:
            raise TypeError("title must be a string")
        if len(value) < 5 or len(value) > 50:
            raise ValueError("title must be 5-50 characters")

        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        from lib.models.author import Author  # import here to avoid circular issues

        if not isinstance(value, Author):
            raise TypeError("author must be an Author instance")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        from lib.models.magazine import Magazine  # import here to avoid circular issues

        if not isinstance(value, Magazine):
            raise TypeError("magazine must be a Magazine instance")
        self._magazine = value
