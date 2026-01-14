from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

import ipdb

a1 = Author("Brian")
a2 = Author("Anne")

m1 = Magazine("TechDaily", "Tech")
m2 = Magazine("HealthNow", "Health")

Article(a1, m1, "Python is really cool")
Article(a1, m1, "Learning SQL basics")
Article(a1, m1, "More practice today")  # a1 now has 3 in m1

Article(a2, m1, "Tech trends in Africa")
Article(a2, m2, "Healthy habits guide")

# Try in ipdb:
# a1.articles()
# a1.magazines()
# a1.topic_areas()
# m1.article_titles()
# m1.contributors()
# m1.contributing_authors()
# Magazine.top_publisher()

ipdb.set_trace()
