
from media import media_elements_list

mock_list = [1, 2, 3, 4, 5]

print(media_elements_list(mock_list))


def test_if_return_a_media_of_values_in_list():
    result_list = media_elements_list(mock_list)
    media = 3.0

    assert isinstance(result_list, float) is True
    assert result_list == media


def test_if_return_a_string_message_if_not_insert_a_list():

    assert media_elements_list('string') == "Enter a list of numbers"
