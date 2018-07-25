import unittest
class AAA(unittest.TestCase):
    def test_A(self):
        print("hello1")

    def test_a(self):
        print("hello2")

if __name__=="__main__":
        # unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(AAA('test_A'))
    runner = unittest.TextTestRunner()
    runner.run(suit)