# importing sys
import sys
import unittest

# adding sample_data to the system path
sys.path.insert(0, '/Desktop/Supermarket-Starter-Pack/sample_data')
sys.path.insert(0, '/Desktop/Supermarket-Starter-Pack/scripts')

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(16, checkout_counter.total_cost_before_tax (9))  # add assertion here


if __name__ == '__main__':
    unittest.main()
