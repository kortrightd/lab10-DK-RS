import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(0,0),0)
        self.assertEqual(add(1,3),4)
        self.assertEqual(add(1345,2948),4293)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(2,3),-1)
        self.assertEqual(sub(10,4),6)
        self.assertEqual(sub(200,200),0)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(2,3),6)
        self.assertEqual(multiply(10,4),0)
        self.assertEqual(multiply(-1,-2),2)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(6,3),2)
        self.assertAlmostEqual(div(10,4),2.5)



    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(10,1000),3)
        self.assertEqual(log(2,16),4)
        self.assertEqual(log(2,1),0)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero\
        with self.assertRaises(ValueError):
            log(1,23)
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)
        self.assertEqual(logarithm(2,1),0)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4),5)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
           square_root(-3)
        self.assertEqual(square_root(1),1)
        self.assertEqual(square_root(4),2)

    #########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()