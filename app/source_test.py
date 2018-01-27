import unittest
from models import source
Source = source.Source

class SourceTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the news class
    '''
    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_source =Source('abc-news','ABC News','general','en','us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


if __name__ == '__main__':
    unittest.main()