@kfp.dsl.graph_component
def train_until_low_error(starting_model, training_data, true_values):
    # Training
    model = xgboost_train_on_csv_op(
        training_data=training_data,
        starting_model=starting_model,
        label_column=0,
        objective='reg:squarederror',
        num_iterations=50,
    ).outputs['model']

    # Predicting
    predictions = xgboost_predict_on_csv_op(
        data=training_data,
        model=model,
        label_column=0,
    ).output