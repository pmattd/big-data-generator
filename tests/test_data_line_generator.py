from data_generator.data_line_generator import EnumeratedFieldGenerator, DataLineGenerator


def test_generate():
    generator1 = EnumeratedFieldGenerator("greeting", ["hello"])
    generator2 = EnumeratedFieldGenerator("greeting", ["goodbye"])
    line_generator = DataLineGenerator([generator1, generator2], ",")
    assert line_generator.generate() == "hello,goodbye"


def test_enumerated_field_generator():
    generator = EnumeratedFieldGenerator("greeting", ["hello"])
    assert generator.get_val() == "hello"
