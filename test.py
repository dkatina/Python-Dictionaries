import unittest

from whiteboard import solution

class MatchTestCase(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(solution( "8 j 8   mBliB8g  imjB8B8  jl  B"),"8j8mBliB8gimjB8B8jlB")
    def test_example_two(self):
        self.assertEqual(solution("8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd"),"88Bifk8hB8BB8BBBB888chl8BhBfd")
    def test_example_three(self):
        self.assertEqual(solution("8aaaaa dddd r     "),"8aaaaaddddr")
    def test_empty(self):
        self.assertEqual(solution("        "),"")

if __name__ == '__main__':
    unittest.main()