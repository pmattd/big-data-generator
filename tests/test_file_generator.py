from data_generator.file_generator import WriteState


def test_add_string():
    ws = WriteState(10)
    ws.add_string("hello")
    assert ws.current_data_size == 5
    assert ws.stop_writing() is False


def test_add_data():
    ws = WriteState(10)
    ws.add_data(9)
    assert ws.current_data_size == 9
    assert ws.stop_writing() is False


def test_add_data_limit_surpassed():
    ws = WriteState(10)
    assert ws.current_data_size == 0
    ws.add_data(9)
    ws.add_data(10)
    assert ws.current_data_size == 19
    assert ws.stop_writing() is True


def test_stop_writing():
    ws = WriteState(10)
    ws.add_data(15)
    assert ws.stop_writing() is True
