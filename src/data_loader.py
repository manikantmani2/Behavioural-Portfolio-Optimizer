import pandas as pd

def load_data(path):
    data = pd.read_csv(path)

    if 'Date' in data.columns:
        data['Date'] = pd.to_datetime(data['Date'])

    # If input is incident-level data, aggregate to daily counts per crime type.
    if {'Date', 'Crime_Type'}.issubset(data.columns):
        daily_counts = (
            data.groupby(['Date', 'Crime_Type'])
            .size()
            .unstack(fill_value=0)
            .reset_index()
            .sort_values('Date')
        )
        return daily_counts

    return data