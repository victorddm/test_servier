import pytest
import pandas as pd
from src.utils import normalize_date, clean_string, reformat_dict_serialization, concat_json_csv

# Test cases for the normalize_date function
@pytest.mark.parametrize("test_input,expected", [
    ("01/01/2020", "2020-01-01"),
    ("02/01/2020", "2020-01-02"),
    ("2020-01-01", "2020-01-01"),
    ("1 January 2020", "2020-01-01"),
    ("25/05/2020", "2020-05-25"),
])

def test_normalize_date(test_input, expected):
    assert normalize_date(test_input) == expected, f"Failed for {test_input}"


@pytest.mark.parametrize("data_json, data_df, expected", [
    (
        {'Name': ['John', 'Anna'], 'Age': [28, 22]},  # JSON data
        pd.DataFrame({'Name': ['Mike', 'Lilly'], 'Age': [32, 26]}),  # DataFrame data
        pd.DataFrame({'Name': ['John', 'Anna', 'Mike', 'Lilly'], 'Age': [28, 22, 32, 26]})  # Expected result
    ),
    # You can add more test cases here
])
def test_concat_json_csv(data_json, data_df, expected):
    result = concat_json_csv(data_json, data_df)
    pd.testing.assert_frame_equal(result, expected, check_dtype=False)



@pytest.mark.parametrize("test_input, expected", [
    ("   Héllo, Wörld!   ", "hello, world!"),
    ("TEST", "test"),  # Another test case
    # Add more test cases as needed
])
def test_clean_string(test_input, expected):
    assert clean_string(test_input) == expected



@pytest.mark.parametrize("graph_dict, expected", [
    # Test case 1
    (
        {
            'Drug1': pd.DataFrame({
                'title': ['Study 1', None],
                'scientific_title': [None, 'Study 2'],
                'source': ['Source 1', 'Source 2'],
                'date': ['2021-01-01', '2021-02-01'],
                'journal': ['Journal 1', 'Journal 2']
            })
        },
        {
            'Drug1': [
                ('Study 1', 'Source 1', '2021-01-01', 'Source 1', 'Journal 1'),
                ('Study 2', 'Source 2', '2021-02-01', 'Source 2', 'Journal 2')
            ]
        }
    ),
    # You can add more test cases here
])
def test_reformat_dict_serialization(graph_dict, expected):
    result = reformat_dict_serialization(graph_dict)
    assert result == expected