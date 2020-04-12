from data_generator.DataFile import EnumeratedFieldGenerator, DataLineGenerator


def test_generate():
    generator1 = EnumeratedFieldGenerator(["hello"])
    generator2 = EnumeratedFieldGenerator(["goodbye"])
    line_generator = DataLineGenerator([generator1, generator2], ",")
    assert line_generator.generate() == "hello,goodbye"


def testEnumeratedFieldGenerator():
    generator = EnumeratedFieldGenerator(["hello"])
    assert generator.getVal() == "hello"
