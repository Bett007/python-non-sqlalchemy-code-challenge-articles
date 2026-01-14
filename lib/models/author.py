from lib.models.article import Article
from lib.models.magazine import Magazine
class Author:
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # can't change after set once
        if hasattr(self, "_name"):
        
            return

        if type(value) is not str:
            raise TypeError("name must be a string")
        if len(value) == 0:
            raise ValueError("name must be longer than 0 characters")

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
        if not isinstance(magazine, Magazine):
         raise TypeError("magazine must be a Magazine instance")
        return Article(self, magazine, title)

    def topic_areas(self):
        if len(self.articles()) == 0:
            return None

        areas = []
        for mag in self.magazines():
            if mag.category not in areas:
             areas.append(mag.category)
        return areas

