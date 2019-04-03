import unittest
import xmlrunner
from youtuber import Youtuber

# A nice video on unit testing https://www.youtube.com/watch?v=Knq_3gvB9lU

# Another nice video on unit testing which also talks about mocking https://www.youtube.com/watch?v=6tNS--WetLI

# Jenkins python integration https://www.youtube.com/watch?v=iGtM_OP01FU


class Testyoutuber(unittest.TestCase):

    def test_initialize_class_with_no_args(self):
        with self.assertRaises(TypeError):
            Youtuber()

    def test_initialize_class_with_args(self):
        youtuber = Youtuber('Allthingsautomated', 'http://www.youtube.com')
        self.assertEqual('Allthingsautomated', youtuber.get_name())
        self.assertEqual('http://www.youtube.com', youtuber.get_channel())


# if __name__ == '__main__':
#    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='./test_results'))
