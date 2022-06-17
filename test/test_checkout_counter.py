# importing sys
import sys

# adding sample_data to the system path
sys.path.insert(0, '/Desktop/Supermarket-Starter-Pack/sample_data')
sys.path.insert(0, '/Desktop/Supermarket-Starter-Pack/scripts')

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    MyTestCase.main()
