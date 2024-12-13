from kedro.pipeline import Pipeline, node, pipeline

from .nodes import create_model_input_table, concat_files, preprocess_shuttles


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
                func=create_model_input_table,
                inputs=["preprocessed_shuttles", "preprocessed_companies", "reviews"],
                outputs="model_input_table",
                name="create_model_input_table_node",
            ),
        ]
    )
