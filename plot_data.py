import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import filter_data

# def plotting(dataframe):
#   plt.figure(figsize=(16, 8))
#   plt.plot(dataframe["program_time"], dataframe["rpm"])
#   plt.gca().invert_xaxis()
#   plt.figure(figsize=(16, 8))
#   plt.plot(dataframe["program_time"], dataframe["operation"],color = 'r')
#   plt.gca().invert_xaxis()
#   plt.ylabel('Operation', labelpad=10)
#   plt.tick_params(axis='y', which='both', labelleft=False, labelright=True)
#   plt.figure(figsize=(16, 8))
#   plt.plot(dataframe["program_time"], dataframe["ipm_temp"])
#   plt.gca().invert_xaxis()
#   plt.figure(figsize=(16, 8))
#   plt.plot(dataframe["program_time"], dataframe["freq"])
#   plt.gca().invert_xaxis()
#   plt.show()

import matplotlib.pyplot as plt

def plotting(dataframe):
    plt.figure(figsize=(16, 8))
    plt.plot(dataframe["program_time"], dataframe["rpm"])
    plt.gca().invert_xaxis()
    plt.savefig('static/images/rpm_chart.png')  # Save the plot as an image
    plt.close()

    plt.figure(figsize=(16, 8))
    plt.plot(dataframe["program_time"], dataframe["operation"], color='r')
    plt.gca().invert_xaxis()
    plt.ylabel('Operation', labelpad=10)
    plt.tick_params(axis='y', which='both', labelleft=False, labelright=True)
    plt.savefig('static/images/operation_chart.png')  # Save the plot as an image
    plt.close()

    plt.figure(figsize=(16, 8))
    plt.plot(dataframe["program_time"], dataframe["ipm_temp"])
    plt.gca().invert_xaxis()
    plt.savefig('static/images/temp_chart.png')  # Save the plot as an image
    plt.close()

    plt.figure(figsize=(16, 8))
    plt.plot(dataframe["program_time"], dataframe["freq"])
    plt.gca().invert_xaxis()
    plt.savefig('static/images/freq_chart.png')  # Save the plot as an image
    plt.close()
