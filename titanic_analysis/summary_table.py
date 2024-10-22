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
        data_type = df[column].dtype
        has_missing = df[column].isnull().any()
        num_unique = df[column].nunique()

        summary_data.append({
                'Feature Name': column,
                'Data Type': str(data_type),
                'Has Missing Values?': has_missing,
                'Number of Unique Values': num_unique
            })
        
    summary_df = pd.DataFrame(summary_data)
        
    return summary_df