import os
from filter_data import filter_program_data
import plot_data

k = filter_program_data("PRG-5 (10_34_01 am).csv")

rpm_above_200 = []
for index, rpm in k.iloc[:200].iterrows():
  if rpm[7] > 200:
    rpm_above_200.append(rpm[7])
  else:
    "Load Sensing skipped"

print(rpm_above_200)

if rpm_above_200[0] < 230:
    print(f"load sensing rpm is {rpm_above_200} and load size is 10kg")
elif rpm_above_200[0] < 260:
    print(f"load sensing rpm is {rpm_above_200} and load size is 8kg")
elif rpm_above_200[0] < 290:
    print(f"load sensing rpm is {rpm_above_200} and load size is 5kg")
else:
    "Load Sensing skipped"