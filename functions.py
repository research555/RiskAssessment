def DataCleaner(df, initial_dtype, final_dtype):

    # Cleans data from the dataset. all categorical are dtype object so it is easy to change. Could also include
    # Changing several dtypes to a final dtype like float to make it more universal but now thats unnecessary

    df = df.dropna().reset_index(drop=True) # remove NA values

    for i in range(len(df.dtypes)): # converts categorical data to numerical
        if df.dtypes[i] == f'{initial_dtype}':
            df[f'{df.dtypes.index[i]}'] = df[f'{df.dtypes.index[i]}'].astype(f'{final_dtype}') #.cat.codes

    df.drop_duplicates() # removes duplicates

    return df
