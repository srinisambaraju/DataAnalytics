import unittest
from youtuber import Youtuber


class Testyoutuber1(unittest.TestCase):

    def test_initialize_class_with_no_args(self):
        with self.assertRaises(TypeError):
            Youtuber()

    def test_initialize_class_with_args(self):
        youtuber = Youtuber('Allthingsautomated', 'http://www.youtube.com')
        self.assertEqual('Allthingsautomated', youtuber.get_name())
        self.assertEqual('http://www.youtube.com', youtuber.get_channel())

