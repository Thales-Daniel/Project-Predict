from predict import predict


def test_predict_return_a_list():
    result_predict = predict(3)
    assert isinstance(result_predict, list) is True


def test_values_in_predict_is_a_string():
    result_predict = predict(3)

    assert isinstance(result_predict[0], str) is True
    assert isinstance(result_predict[1], str) is True
    assert isinstance(result_predict[2], str) is True


def test_if_lenght_of_predict_is_correct():
    result_predict = predict(3)

    assert len(result_predict) == 3
