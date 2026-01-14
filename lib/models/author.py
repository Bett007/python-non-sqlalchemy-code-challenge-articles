from lib.models.article import Article
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