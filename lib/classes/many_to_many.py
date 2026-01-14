class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # immutable after first set
        if hasattr(self, "_name"):
            return
        if type(value) is not str:
            return
        if len(value) == 0:
            return
        self._name = value

    def articles(self):
        return [a for a in Article.all if a.author == self]

    def magazines(self):
        mags = []
        for article in self.articles():
            if article.magazine not in mags:
                mags.append(article.magazine)
        return mags

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if len(self.articles()) == 0:
            return None
        areas = []
        for mag in self.magazines():
            if mag.category not in areas:
                areas.append(mag.category)
        return areas


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) is not str:
            return
        if len(value) < 2 or len(value) > 16:
            return
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if type(value) is not str:
            return
        if len(value) == 0:
            return
        self._category = value

    def articles(self):
        return [a for a in Article.all if a.magazine == self]

    def contributors(self):
        authors = []
        for article in self.articles():
            if article.author not in authors:
                authors.append(article.author)
        return authors

    def article_titles(self):
        arts = self.articles()
        if len(arts) == 0:
            return None
        return [a.title for a in arts]

    def contributing_authors(self):
        arts = self.articles()
        if len(arts) == 0:
            return None

        counts = {}
        for a in arts:
            counts[a.author] = counts.get(a.author, 0) + 1

        result = []
        for author, count in counts.items():
            if count > 2:
                result.append(author)

        if len(result) == 0:
            return None
        return result

    @classmethod
    def top_publisher(cls):
        if len(Article.all) == 0:
            return None

        counts = {}
        for article in Article.all:
            mag = article.magazine
            counts[mag] = counts.get(mag, 0) + 1

        top_mag = None
        top_count = 0
        for mag, count in counts.items():
            if count > top_count:
                top_mag = mag
                top_count = count

        return top_mag


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
        # immutable after first set
        if hasattr(self, "_title"):
            return
        if type(value) is not str:
            return
        if len(value) < 5 or len(value) > 50:
            return
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            return
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            return
        self._magazine = value
