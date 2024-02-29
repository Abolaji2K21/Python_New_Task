import unittest
from Task_Seven import Task_Seven

class MyTestCase(unittest.TestCase):

    def test_that_i_can_get_name(self):
        task_seven = Task_Seven("Abolaji")
        self.assertEqual("Abolaji", task_seven.print_name)

    def test_that_i_can_set_name(self):
        task_seven = Task_Seven("Abolaji")
        task_seven.string_name = "Sk"
        self.assertEqual("Sk", task_seven.print_name)




if __name__ == '__main__':
    unittest.main()


