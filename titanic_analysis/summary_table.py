import pandas as pd


def create_summary_table(df):
    """
    Creates a summary DataFrame with feature name, data type, number of unique values, and if it has missing values.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        pd.DataFrame: A summary DataFrame.
    """
    pass  # Implement the logic here
    summary_data = []
    for column in df.columns:
        feature_name = column
        data_type = df[column].dtype
        number_of_unique_values = df[column].nunique()
        missing_values = df[column].isnull().any()

        summary_df.append({
            'Feature name': feature_name,
            'Data type': data_type,
            'Number of unique values': number_of_unique_values,
            'Missing values':missing_values
        })
    summary_df = pd.DataFrame(summary_data)

    return(summary_df)
