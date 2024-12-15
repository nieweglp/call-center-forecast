import pandas as pd
import numpy as np
from datetime import datetime
import holidays
from requests import get


def _utils_dates(df: pd.DataFrame) -> pd.DataFrame:
    df["Date"] = df["EmitDate"].dt.date
    df["CallTime"] = (df["EmitEndDate"] - df["EmitDate"]).dt.total_seconds()
    return df


def _extract_info_from_dates(dates: pd.Series) -> pd.DataFrame:
    df = pd.DataFrame(dates)
    df["Year"] = dates.dt.year
    df["Month"] = dates.dt.month
    df["Day"] = dates.dt.day
    df["Day_of_week"] = dates.dt.dayofweek
    df["Week_of_year"] = dates.dt.isocalendar().week
    df["Day_of_year"] = dates.dt.dayofyear
    df["Is_weekend"] = dates.isin([5, 6]).astype(int)
    df["Day_of_week_sin"] = np.sin(2 * np.pi * df["day_of_week"] / 7)
    df["Day_of_week_cos"] = np.cos(2 * np.pi * df["day_of_week"] / 7)
    df["Month_sin"] = np.sin(2 * np.pi * df["month"] / 12)
    df["Month_cos"] = np.cos(2 * np.pi * df["month"] / 12)

    day_of_year = dates.dt.dayofyear
    days_in_year = dates.dt.is_leap_year.apply(lambda x: 366 if x else 365)

    df["Year_sin"] = np.sin(2 * np.pi * day_of_year / days_in_year)
    df["Year_cos"] = np.cos(2 * np.pi * day_of_year / days_in_year)

    return df


def _generate_holidays_dates(parameters: dict) -> pd.DataFrame:
    date_range = pd.date_range(start=parameters["start_date"], end=parameters["end_date"])
    denmark_holidays = holidays.Denmark(years=[2022, 2023])

    data = {
        "Date": date_range,
        "Is_holiday": [1 if date in denmark_holidays else 0 for date in date_range]
    }
    return pd.DataFrame(data)

def _get_weather_data(location, parameters: dict) -> pd.DataFrame:
    url = (
        f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
        f"{location}/{parameters['start_date']}/{parameters['end_date']}"
    )
    params = {
        "unitGroup": "metric",
        "key": parameters["WEATHER_API_KEY"],
        "contentType": "json",
        "include": "days"
    }

    response = get(url, params=params)
    data_historical = response.json()

    historical_days = data_historical["days"]
    df_weather = pd.DataFrame(historical_days)
    df_weather["Date"] = pd.to_datetime(df_weather["datetime"])
    df_conditions_one_hot_encoding = pd.get_dummies(df_weather['conditions'], drop_first=True) * 1
    weather_cols = ['tempmax', 'tempmin', 'temp', 'dew', 'humidity',
       'precip', 'windspeed', 'pressure']

    df_weather = pd.concat([df_weather[weather_cols], df_conditions_one_hot_encoding], axis=1)
    new_cop_cols = [location + "_" + col for col in df_weather.columns]
    df_weather.columns = [col.replace(" ", "_").replace(",","") for col in new_cop_cols]
    return df_weather


def concat_files(
    assistance_train_dataset_1: pd.DataFrame,
    assistance_train_dataset_2: pd.DataFrame,
    assistance_train_dataset_3: pd.DataFrame,
) -> pd.DataFrame:
    """ """
    assistance_train_dataset = pd.concat(
        [
            assistance_train_dataset_1,
            assistance_train_dataset_2,
            assistance_train_dataset_3,
        ],
        ignore_index=True,
    )
    return assistance_train_dataset


def extract_from_dates(assistance_train_dataset: pd.DataFrame) -> pd.DataFrame:
    """ """
    assistance_train_dataset_dates = _utils_dates(assistance_train_dataset)
    return assistance_train_dataset_dates


def aggregate_per_day(assistance_train_dataset_dates: pd.DataFrame) -> pd.DataFrame:
    """ """
    df_agg_calls = (
        assistance_train_dataset_dates.groupby("Date")["EmitDate"]
        .count()
        .reset_index()
        .rename(columns={"EmitDate": "Calls"})
    )
    df_agg_call_time = assistance_train_dataset_dates.groupby("Date")["CallTime"].sum().reset_index()
    df_agg_call_type = pd.crosstab(assistance_train_dataset_dates["Date"], assistance_train_dataset_dates["CallType"]).reset_index()
    df_agg_call_direction = pd.crosstab(assistance_train_dataset_dates["Date"], assistance_train_dataset_dates["CallDirection"]).reset_index()

    df_agg_numerical = df_agg_calls.merge(df_agg_call_time, on="Date")
    df_agg_categories = df_agg_call_type.merge(df_agg_call_direction, on="Date")
    df_agg = df_agg_numerical.merge(df_agg_categories, on="Date")
    df_agg.columns = [col.capitalize() for col in df_agg.columns]
    return df_agg


def enhance_dates(df: pd.DataFrame) -> pd.DataFrame:
    """ """
    df_enhanced_dates = _extract_info_from_dates(df["Date"])
    return df_enhanced_dates


def create_model_input_table(df_enhanced_dates: pd.DataFrame, parameters: dict) -> pd.DataFrame:
    """

    """
    df_holidays = _generate_holidays_dates(parameters)
    # df_weather_copenhagen = _get_weather_data("Copenhagen, Denmark")
    # df_weather_aarhus = _get_weather_data("Aarhus, Denmark")

    model_input_table = df_enhanced_dates.merge(df_holidays, on="Date")
    return model_input_table
