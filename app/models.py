
class Articles:
  

    def __init__(self,id,name,author, title, description, url, urlToImage,publishedAt):
    
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt




class Source:
    """
    Source class to define news source object
    """

    def __init__(self, id, name, author, title, url, urlToImage, publishedAt):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
    
       
