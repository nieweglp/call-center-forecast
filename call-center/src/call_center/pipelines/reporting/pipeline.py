from kedro.pipeline import Pipeline, node, pipeline


def create_pipeline(**kwargs) -> Pipeline:
    """This is a simple pipeline which generates a pair of plots"""
    return pipeline(
        [
            # node(
            #     func=generate plot,
            #     inputs="preprocessed_shuttles",
            #     outputs="shuttle_passenger_capacity_plot_exp",
            # ),
        ]
    )
