import os
from filter_data import filter_program_data
import plot_data

k = filter_program_data("PRG-3 (11_32_21 am).xlsx")

#plot_data.plotting(M)



l = []
i = 0

for index, row in k.iterrows():
    if row['operation'] == 'INTERMEDIATE_SPIN' and row['rpm'] == 800:
        l.append(index , row['rpm'])
if len(l) != 0:
    i+=1


print(l)