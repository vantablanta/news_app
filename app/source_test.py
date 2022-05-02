from models import source
import unittest


Source = source.Source

class SourceTest(unittest.TestCase):
    '''Testace to test the Source Class'''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source("name","description","url" )
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))


if __name__ == '__main__':
    unittest.main()