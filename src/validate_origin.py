from typing import Any
from pandas import DataFrame

def lower_if_possible(value: Any) -> Any:
    try:
        result = value.lower()
    except:
        return value
    return result

def validate_origin(data: DataFrame, reference_data: DataFrame) -> DataFrame:
    origins_lowered = data.origin.apply(lower_if_possible)
    countries_lowered = reference_data["COUNTRY"].apply(lambda x: x.lower())
    country_not_found = ~origins_lowered.isin(countries_lowered)
    data.loc[country_not_found, "reason"] += "Origin Not Found. | "
    return data