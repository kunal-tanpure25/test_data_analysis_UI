import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


def parse_time_string(time_str):
  parts = time_str.split(' Hr ')
  hours = int(parts[0])
  minutes = int(parts[1].replace(' Min', ''))
  # return pd.Timedelta(hours=hours, minutes=minutes)
  return f"{hours}:{minutes}:00"


def filter_program_data(filepath):

  try:


    if filepath.endswith('.xlsx'):
      d = pd.read_excel(filepath)
    else:
      d = pd.read_csv(filepath)

    expected_columns = ["date", "time", "program", "selected_rpm", "selected_temp",
              "operation", "program_time", "rpm", "k", "freq", "ipm_temp"]

    if len(d.columns) < len(expected_columns):
      print(f"Warning: The file has {len(d.columns)} columns, expected {len(expected_columns)} columns.")
      d.columns = expected_columns[:len(d.columns)]
    elif len(d.columns) > len(expected_columns):
      print(f"Warning: The file has {len(d.columns)} columns, more than the expected {len(expected_columns)} columns. Extra columns will be ignored.")
      d.columns = expected_columns
    else:
      d.columns = expected_columns

    #d["operation"] = d["operation"].astype("string")

    if d["rpm"].dtype != 'int64':
      d = d.dropna(subset=['rpm'])

    if d['operation'].dtype == 'object':
      d_filtered = d[d['operation'] != 'IDEAL']
    else:
      print("The data type of 'column_name' is not object")

    start_index = d_filtered[d_filtered['operation'] == "START"].index.tolist()
    if start_index:
      start_index = start_index[0]
    else:
      print("WARNING: 'START' not found in the 'operation' column.")
      start_index = None

    end_index = d_filtered[d_filtered['operation'] == "END"].index.tolist()
    if end_index:
      end_index = end_index[0]
    else:
      print("WARNING: 'END' not found in the 'operation' column.")
      end_index = None

    if start_index is not None and end_index is not None:
      filtered_df = d_filtered.iloc[start_index:end_index + 1]
    else:
      print("No valid range found between 'START' and 'END'.")

    filter = filtered_df[filtered_df["rpm"]>1000]
    filtered_df = filtered_df.drop(filter.index)

    filtered_df['program_time'] = filtered_df['program_time'].apply(parse_time_string)
    filtered_df["program_time"] = pd.to_datetime(filtered_df["program_time"],format='%H:%M:%S')
    return filtered_df

  except FileNotFoundError:
    print("Error: File not found at", filepath)
    return None