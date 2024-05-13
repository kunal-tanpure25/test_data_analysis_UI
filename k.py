import os
from filter_data import filter_program_data
import plot_data

M = filter_program_data("PRG-7 (5_30_16 pm).csv")

plot_data.plotting(M)