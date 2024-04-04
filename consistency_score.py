import pandas as pd
import os
from datetime import timedelta
import numpy as np

STREAM_TIME_MULT = 1

path_pre = './vt-stat-graphs/csv/time'

def delete_rows_by_non_null_frequency(df, min_count):
    reference_column = "Hours"
    column_to_count = "VTuber"
    # Filter the DataFrame to include only rows where reference_column is not null
    filtered_df = df[df[reference_column].notnull()]

    # Calculate frequency of each value in column_to_count in the filtered DataFrame
    value_counts = filtered_df[column_to_count].value_counts()

    # Identify values where their frequency is less than min_count
    values_to_remove = value_counts[value_counts < min_count].index

    # Filter the original DataFrame to keep only rows where the column_to_count value's frequency is above or equal to min_count
    df = df[~df[column_to_count].isin(values_to_remove)]

    return df

# Function to remove the first month with data for each VTuber
def remove_first_month_with_data(df):
    first_non_null_index = df['Hours'].first_valid_index()
    if first_non_null_index is not None:
        return df.drop(first_non_null_index)
    return df

def calculate_consistency_score(data):
    # Calculate average and standard deviation
    avg_data = data.groupby('VTuber')['Hours'].mean().reset_index()
    std_data = data.groupby('VTuber')['Hours'].std().reset_index()

    # Calculate monthly changes and apply the penalty factor
    data['Monthly Change'] = data.groupby('VTuber')['Hours'].diff().fillna(0)

    # Merge average, standard deviation, and penalty factor into one DataFrame
    combined_data = pd.merge(avg_data, std_data, on='VTuber', suffixes=('_Avg', '_Std'))

    combined_data['Consistency Score'] = (combined_data['Hours_Avg'] ** STREAM_TIME_MULT) / combined_data['Hours_Std']
    #combined_data['Consistency Score'] = (combined_data['Hours_Std'] / combined_data['Hours_Avg']) * 100

    return combined_data.sort_values(by='Consistency Score', ascending=False)
    
# Reloading the data files after code execution state reset
file_list = ['hl-ts-gen0.csv', 'hl-ts-gen1.csv', 'hl-ts-gen2.csv', 'hl-ts-gamers.csv', 'hl-ts-gen3.csv', 'hl-ts-gen4.csv', 'hl-ts-gen5.csv', 'hl-ts-gen6.csv', 
	'hl-ts-en.csv', 'hl-ts-en2.csv', 'hl-ts-en3.csv', 'hl-ts-id.csv', 'hl-ts-id3.csv']
file_path_list = []
for fi in file_list:
    file_path_list.append(os.path.join(path_pre, fi))
    
data_list = []
for item in file_path_list:
    data_list.append(pd.read_csv(item))
    
for item in data_list:
    item.rename(columns={'Unnamed: 0': 'VTuber'}, inplace=True)

# Merging the data
combined_data = pd.concat(data_list, ignore_index=True)

# Melting the combined data for easier analysis
melted_combined_data = combined_data.melt(id_vars=['VTuber'], var_name='Month', value_name='Hours')
melted_combined_data['Month'] = pd.to_datetime(melted_combined_data['Month'], format='%b-%y')
melted_combined_data = melted_combined_data.sort_values(by=['VTuber', 'Month'])
end_date = melted_combined_data['Month'].max()
start_date_6_months = end_date - timedelta(days=6*30)
start_date_3_months = end_date - timedelta(days=3*30)
start_date_last_year = end_date - timedelta(days=365)

# Excluding the first available month of data for each VTuber
melted_combined_data_updated = melted_combined_data.groupby('VTuber').apply(remove_first_month_with_data).reset_index(drop=True)
melted_combined_data_updated.to_csv("test.csv")
data_last_3_months = melted_combined_data_updated[melted_combined_data_updated['Month'] >= start_date_3_months]
data_last_6_months = melted_combined_data_updated[melted_combined_data_updated['Month'] >= start_date_6_months]
data_last_year = melted_combined_data_updated[melted_combined_data_updated['Month'] >= start_date_last_year]

data_last_3_months = delete_rows_by_non_null_frequency(data_last_3_months, 3)
data_last_6_months = delete_rows_by_non_null_frequency(data_last_6_months, 6)
data_last_year = delete_rows_by_non_null_frequency(data_last_year, 12)

consistency_last_6_months = calculate_consistency_score(data_last_6_months)
consistency_last_year = calculate_consistency_score(data_last_year)
consistency_last_3_months = calculate_consistency_score(data_last_3_months)

consistency_last_3_months = consistency_last_3_months.round(2)
consistency_last_6_months = consistency_last_6_months.round(2)
consistency_last_year = consistency_last_year.round(2)

consistency_last_3_months = consistency_last_3_months.sort_values(by=["Consistency Score"], ascending=False)
consistency_last_6_months = consistency_last_6_months.sort_values(by=["Consistency Score"], ascending=False)
consistency_last_year = consistency_last_year.sort_values(by=["Consistency Score"], ascending=False)

columns = ['VTuber', 'Consistency Score']
consistency_last_3_months.to_csv('3month.csv', columns=columns, index=False)
consistency_last_6_months.to_csv('6month.csv', columns=columns, index=False)
consistency_last_year.to_csv('1year.csv', columns=columns, index=False)


