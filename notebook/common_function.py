
def dataset_summary(df):
    import pandas as pd 
    pd.set_option('max_columns', 50)
    """
    Return the following information from dataset:
    variable name, number of unique value, pandas dtype, 
    number of missing values, percentage of missing values, 
    and list of unique values.
    
    Args:
    * df, pd.DataFrame: the dataset
    
    Output:
    * table, pd.DataFrame
    """
    table = pd.DataFrame(
                columns=['variable',
                         'no_unique',
                         'pandas_dtype',
                         'missing_value',
                         '%_missing_values',
                         'unique_value'
                ]
    )

    for i, var in enumerate(df.columns):
        table.loc[i] = [var,
                        df[var].nunique(),
                        df[var].dtypes,
                        df[var].isnull().sum(),
                        df[var].isnull().sum() * 100 / df.shape[0],
                        df[var].unique().tolist()
        ]
    return table