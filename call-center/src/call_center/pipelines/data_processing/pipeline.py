from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    aggregate_per_day,
    create_model_input_table,
    concat_files,
    enhance_dates,
    extract_from_dates,
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=concat_files,
                inputs=[
                    "assistance_train_dataset_1",
                    "assistance_train_dataset_2",
                    "assistance_train_dataset_3",
                ],
                outputs="assistance_train_dataset",
                name="assistance_train_dataset_node",
            ),
            node(
                func=extract_from_dates,
                inputs=["assistance_train_dataset"],
                outputs="assistance_train_dataset_dates",
                name="assistance_train_dataset_dates_node",
            ),
            node(
                func=aggregate_per_day,
                inputs=["assistance_train_dataset_dates"],
                outputs="df_agg",
                name="df_agg_node",
            ),
            node(
                func=enhance_dates,
                inputs=["df_agg"],
                outputs="df_enhanced_dates",
                name="df_enhanced_dates_node",
            ),
            node(
                func=create_model_input_table,
                inputs=["df_enhanced_dates", "params"],
                outputs="model_input_table",
                name="create_model_input_table_node",
            ),
        ]
    )
