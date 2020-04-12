import unittest

from data_generator.data_generator import EnumeratedFieldGenerator, DataLineGenerator


class DataFileTest(unittest.TestCase):

    def testEnumeratedFieldGenerator(self):
        generator = EnumeratedFieldGenerator(["hello"])
        self.assertEqual(generator.getVal(), "hello")

    def testGenerate(self):
        generator1 = EnumeratedFieldGenerator(["hello"])
        generator2 = EnumeratedFieldGenerator(["goodbye"])
        line_generator = DataLineGenerator([generator1, generator2], ",")
        self.assertEqual(line_generator.generate(), "hello,goodbye")
