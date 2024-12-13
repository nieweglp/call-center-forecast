import pandas as pd
import numpy as np


def _utils_dates(df: pd.DataFrame) -> pd.DataFrame:
    df["Date"] = df["EmitDate"].dt.date
    df["CallTime"] = (df["EmitEndDate"] - df["EmitDate"]).dt.total_seconds()
    return df


def _extract_info_from_dates(dates: pd.Series) -> pd.DataFrame:
    df = pd.DataFrame(dates)
    df["year"] = dates.dt.year
    df["month"] = dates.dt.month
    df["day"] = dates.dt.day
    df["day_of_week"] = dates.dt.dayofweek
    df["week_of_year"] = dates.dt.isocalendar().week
    df["day_of_year"] = dates.dt.dayofyear
    df["is_weekend"] = dates.isin([5, 6]).astype(int)
    df["day_of_week_sin"] = np.sin(2 * np.pi * df["day_of_week"] / 7)
    df["day_of_week_cos"] = np.cos(2 * np.pi * df["day_of_week"] / 7)
    df["month_sin"] = np.sin(2 * np.pi * df["month"] / 12)
    df["month_cos"] = np.cos(2 * np.pi * df["month"] / 12)

    day_of_year = dates.dt.dayofyear
    days_in_year = dates.dt.is_leap_year.apply(lambda x: 366 if x else 365)

    df["year_sin"] = np.sin(2 * np.pi * day_of_year / days_in_year)
    df["year_cos"] = np.cos(2 * np.pi * day_of_year / days_in_year)

    return df


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
    assistance_train_dataset = _utils_dates(assistance_train_dataset)
    return assistance_train_dataset


def aggregate_per_day(df: pd.DataFrame) -> pd.DataFrame:
    """ """
    df_agg_calls = (
        df.groupby("Date")["EmitDate"]
        .count()
        .reset_index()
        .rename(columns={"EmitDate": "Calls"})
    )
    df_agg_call_time = df.groupby("Date")["CallTime"].sum().reset_index()
    df_agg_call_type = pd.crosstab(df["Date"], df["CallType"]).reset_index()
    df_agg_call_direction = pd.crosstab(df["Date"], df["CallDirection"]).reset_index()

    df_agg_numerical = df_agg_calls.merge(df_agg_call_time, on="Date")
    df_agg_categories = df_agg_call_type.merge(df_agg_call_direction, on="Date")
    df_agg = df_agg_numerical.merge(df_agg_categories, on="Date")
    df_agg.columns = [col.capitalize() for col in df_agg.columns]
    return df_agg


def enhance_dates(df: pd.DataFrame) -> pd.DataFrame:
    _extract_info_from_dates(df["Date"])


def preprocess_companies(companies: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """Preprocesses the data for companies.

    Args:
        companies: Raw data.
    Returns:
        Preprocessed data, with `company_rating` converted to a float and
        `iata_approved` converted to boolean.
    """
    companies["iata_approved"] = _is_true(companies["iata_approved"])
    companies["company_rating"] = _parse_percentage(companies["company_rating"])
    return companies, {"columns": companies.columns.tolist(), "data_type": "companies"}


def preprocess_shuttles(shuttles: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data for shuttles.

    Args:
        shuttles: Raw data.
    Returns:
        Preprocessed data, with `price` converted to a float and `d_check_complete`,
        `moon_clearance_complete` converted to boolean.
    """
    shuttles["d_check_complete"] = _is_true(shuttles["d_check_complete"])
    shuttles["moon_clearance_complete"] = _is_true(shuttles["moon_clearance_complete"])
    shuttles["price"] = _parse_money(shuttles["price"])
    return shuttles


def create_model_input_table(
    shuttles: pd.DataFrame, companies: pd.DataFrame, reviews: pd.DataFrame
) -> pd.DataFrame:
    """Combines all data to create a model input table.

    Args:
        shuttles: Preprocessed data for shuttles.
        companies: Preprocessed data for companies.
        reviews: Raw data for reviews.
    Returns:
        Model input table.

    """
    rated_shuttles = shuttles.merge(reviews, left_on="id", right_on="shuttle_id")
    rated_shuttles = rated_shuttles.drop("id", axis=1)
    model_input_table = rated_shuttles.merge(
        companies, left_on="company_id", right_on="id"
    )
    model_input_table = model_input_table.dropna()
    return model_input_table
