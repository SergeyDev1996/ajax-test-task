from main import get_parameters_from_binary
import pytest

@pytest.mark.parametrize(
    "income_payload, error_to_receive",
    [
        pytest.param(
        1,
        TypeError,
        id="Test with integer"
        ),
        pytest.param(
        True,
        TypeError,
        id="Test with boolean"
        ),
        pytest.param(
        "TheString",
        TypeError,
        id="Test with string"
        ),
        pytest.param(
        "10FH0E00",
        TypeError,
        id="Test with incorrect hexadecimal income"
        )
    ]
)
def test_error_with_incorrect_income_data(
    income_payload,
    error_to_receive,
):
    with pytest.raises(error_to_receive):
        get_parameters_from_binary(income_payload)

@pytest.mark.parametrize(
    "income_payload, data_to_receive",
    [
        pytest.param(
        "10FA0E00",
            {'field1': 'Low',
             'field2': '00',
             'field3': '01',
             'field4': '00',
             'field5': '00',
             'field6': '01',
             'field7': '00',
             'field8': 'Very High',
             'field9': '00',
             'field10': '00',
        },
        id="Test with integer"
        ),
        pytest.param(
            "00000000",
            {
                "field1": "Low",
                "field2": "00",
                "field3": "00",
                "field4": "00",
                "field5": "00",
                "field6": "00",
                "field7": "00",
                "field8": "Very Low",
                "field9": "00",
                "field10": "00",
            },
            id="Should return the lowest values for 0 payload",
        )
    ]
)

def test_if_data_is_correct(income_payload, data_to_receive):
    assert get_parameters_from_binary(income_payload) == data_to_receive