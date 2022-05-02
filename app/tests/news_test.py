from models import news
import unittest


News= news.News

class NewsTest(unittest.TestCase):
    '''Testace to test the Source Class'''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = News()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, News))


if __name__ == '__main__':
    unittest.main()