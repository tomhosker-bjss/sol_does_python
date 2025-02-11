from src.validate_origin import validate_origin, ORIGIN_NOT_FOUND

from utils import get_test_dataframe

def test_validate_origin():
    data = get_test_dataframe("validate_origin_in.csv")
    reference_data = get_test_dataframe("validate_origin_reference_data.csv")
    result = validate_origin(data, reference_data)
    lithuanian_rows = result.loc[result["origin"] == "Lithuania"]
    lithuanian_reason = lithuanian_rows.iloc[0]["reason"]
    assert ORIGIN_NOT_FOUND not in lithuanian_reason
    livonian_rows = result.loc[result["origin"] == "Livonia"]
    livonian_reason = livonian_rows.iloc[0]["reason"]
    assert ORIGIN_NOT_FOUND in livonian_reason