import unittest
from optimal_change import optimal_change

class TestMode(unittest.TestCase):

    def test_for_correct_answer_type(self):
        self.assertIsInstance(optimal_change(50, 100), str)

    def test_for_bad_input(self):
        self.assertEqual(optimal_change('A', 100), 'Both inputs must be a number.')
    
    def test_for_no_change(self):
        self.assertEqual(optimal_change(100, 100), 'No change needed.')
    
    def test_for_insufficient_funds(self):
        self.assertEqual(optimal_change(80, 50), 'Insuffient funds.')

    def test_for_single_deno(self):
        self.assertEqual(optimal_change(90, 100), 'The optimal change for an item that costs $90 with an amount paid of $100 is 1 $10 bill.')

    def test_for_refund(self):
        self.assertEqual(optimal_change(-80, 50), 'Vending machines do not offer refunds at this time.')

    def test_for_primary_function(self):
         self.assertEqual(optimal_change(62.13, 100), "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")

    def test_for_primary_function2(self):
        self.assertEqual(optimal_change(31.51, 50), "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")




if __name__ == '__main__':
    unittest.main()

