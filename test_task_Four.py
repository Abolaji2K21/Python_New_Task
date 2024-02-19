from unittest import TestCase

import task_Four


class Test(TestCase):
    def test_intersperse_strings(self):
        sample_input1 = 'abc'
        sample_input2 = 'xyz'
        sample_output = 'xyc abz'
        self.assertEqual(sample_output, task_Four.intersperse_strings(sample_input1,sample_input2))
        sample_input1 = 'abcde'
        sample_input2 = 'rstuv'
        sample_output = 'rscde abtuv'
        self.assertEqual(sample_output, task_Four.intersperse_strings(sample_input1,sample_input2))
