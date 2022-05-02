class News:
    """News Class to create the news object"""

    def __init__(self, urlToImage, title, description, name, publishedAt, url  ):
        self.urlToImage =  urlToImage
        self.title= title
        self.description = description
        self.name = name
        self.publishedAt = publishedAt
        self.url  =url 