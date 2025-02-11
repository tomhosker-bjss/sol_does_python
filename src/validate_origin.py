from typing import Any
from pandas import DataFrame

REASON_SEPARATOR = " | "
ORIGIN_NOT_FOUND = "Origin Not Found."

def lower_if_possible(value: Any) -> Any:
    pass

def validate_origin(data: DataFrame, reference_data: DataFrame) -> DataFrame:
    origins_lowered = data["origin"].apply(lower_if_possible)
    countries_lowered = reference_data["COUNTRY"].apply(lambda x: x.lower())
    country_not_found = ~origins_lowered.isin(countries_lowered)
    data.loc[country_not_found, "reason"] += \
        f"{ORIGIN_NOT_FOUND}{REASON_SEPARATOR}"
    return data