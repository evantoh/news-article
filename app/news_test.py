import unittest
from .models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the news class
    '''
    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_news = News('Herbex Health slated for ')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))
if __name__ =='__main__':
    unittest.main()