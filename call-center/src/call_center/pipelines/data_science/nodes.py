import logging

import pandas as pd
from xgboost import XGBRegressor
from sklearn.metrics import (
    max_error,
    mean_absolute_error,
    r2_score,
    mean_absolute_percentage_error,
    root_mean_squared_error,
)
from sklearn.model_selection import train_test_split
from kedro.framework.context import KedroContext


logger = logging.getLogger(__name__)


def _compute_asses_metrics(y_test: pd.Series, y_pred: pd.Series) -> dict:
    score = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    mse = root_mean_squared_error(y_test, y_pred, squared=False)
    me = max_error(y_test, y_pred)
    mape = mean_absolute_percentage_error(y_test, y_pred)
    logger.info("Model has a coefficient R^2 of %.3f on test data.", score)
    return {"r2_score": score, "mae": mae, "mse": mse, "max_error": me, "mape": mape}


def _save_predictions(predictions: pd.Series) -> None:
    """ """
    context = KedroContext()
    catalog = context.catalog
    predictions_dict = {"predictions": predictions.tolist()}
    catalog.save("predictions_json", predictions_dict)


def split_data(data: pd.DataFrame, parameters: dict) -> tuple:
    """Splits data into features and targets training and test sets.

    Args:
        data: Data containing features and target.
        parameters: Parameters defined in parameters/data_science.yml.
    Returns:
        Split data.
    """
    X = data[parameters["features"]]
    y = data[parameters["target"]]
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=parameters["test_size"],
        random_state=parameters["random_state"],
        shuffle=False,
    )
    return X_train, X_test, y_train, y_test


def train_model(
    X_train: pd.DataFrame, y_train: pd.Series, parameters: dict
) -> XGBRegressor:
    """Trains the linear regression model.

    Args:
        X_train: Training data of independent features.
        y_train: Training data for price.

    Returns:
        Trained model.
    """
    regressor = XGBRegressor(
        n_estimators=100,
        max_depth=3,
        learning_rate=0.1,
        objective="reg:squarederror",
        andom_state=parameters["random_state"],
    )
    regressor.fit(X_train, y_train)
    return regressor


def evaluate_model(
    regressor: XGBRegressor, X_test: pd.DataFrame, y_test: pd.Series
) -> dict[str, float]:
    """Calculates and logs the coefficient of determination.

    Args:
        regressor: Trained model.
        X_test: Testing data of independent features.
        y_test: Testing data for price.
    """
    y_pred = regressor.predict(X_test)
    metrics_dict = _compute_asses_metrics(y_test, y_pred)
    logger.info("Saving predictions to json file")
    _save_predictions(y_pred)
    return metrics_dict
