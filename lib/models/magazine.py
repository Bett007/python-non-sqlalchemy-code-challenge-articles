from lib.models.article import Article
class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) is not str:
            raise TypeError("name must be a string")
        if len(value) < 2 or len(value) > 16:
            raise ValueError("name must be 2-16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if type(value) is not str:
            raise TypeError("category must be a string")
        if len(value) == 0:
            raise ValueError("category must be longer than 0 characters")
        self._category = value
        
    def articles(self):
        return [a for a in Article.all if a.magazine == self]