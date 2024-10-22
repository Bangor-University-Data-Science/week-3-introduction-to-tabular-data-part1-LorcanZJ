def get_numerical_df(df, numerical_features):
    """
    Creates a DataFrame containing only numerical features.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        numerical_features (list): List of numerical feature names.
    
    Returns:
        pd.DataFrame: DataFrame containing only numerical features.
    """
    pass  # Implement the logic here
    valid_numerical_features = [col for col in numerical_features if col in df.columns]
    return df[valid_numerical_features]