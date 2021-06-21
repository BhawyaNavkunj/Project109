import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics

df = pd.read_csv("data.csv")
reading_list = df["reading"].to_list()
writing_list = df["writing"].to_list()
math_list = df["math"].to_list()

reading_mean = statistics.mean(reading_list)
reading_median = statistics.median(reading_list)
reading_mode = statistics.mode(reading_list)
print("The mean, median and mode for reading scores are {}, {}, and {} respectively.".format(reading_mean,reading_median,reading_mode))

writing_mean = statistics.mean(writing_list)
writing_median = statistics.median(writing_list)
writing_mode = statistics.mode(writing_list)
print("The mean, median and mode for wrting scores are {}, {}, and {} respectively.".format(reading_mean,reading_median,reading_mode))

math_mean = statistics.mean(math_list)
math_median = statistics.median(math_list)
math_mode = statistics.mode(math_list)
print("The mean, median and mode for math scores are {}, {}, and {} respectively.".format(reading_mean,reading_median,reading_mode))

reading_sd = statistics.stdev(reading_list)
writing_sd = statistics.stdev(writing_list)
math_sd = statistics.stdev(math_list)

reading_first_sd_start, reading_first_sd_end = reading_mean - reading_sd, reading_mean + reading_sd
reading_second_sd_start, reading_second_sd_end = reading_mean - (2*reading_sd),reading_mean + (2*reading_sd)
reading_third_sd_start, reading_third_sd_end = reading_mean - (2*reading_sd), reading_mean + (2*reading_sd)

writing_first_sd_start, writing_first_sd_end = writing_mean - writing_sd, writing_mean + writing_sd
writing_second_sd_start, writing_second_sd_end = writing_mean - (2*writing_sd),writing_mean + (2*writing_sd)
writing_third_sd_start, writing_third_sd_end = writing_mean - (2*writing_sd), writing_mean + (2*writing_sd)

math_first_sd_start, math_first_sd_end = math_mean - math_sd, math_mean + math_sd
math_second_sd_start, math_second_sd_end = math_mean - (2*math_sd),math_mean + (2*math_sd)
math_third_sd_start, math_third_sd_end = math_mean - (2*math_sd), math_mean + (2*math_sd)

reading_first_list = [result for result in reading_list if result > reading_first_sd_start and result < reading_first_sd_end]
reading_second_list = [result for result in reading_list if result > reading_second_sd_start and result < reading_second_sd_end]
reading_third_list = [result for result in reading_list if result > reading_third_sd_start and result < reading_third_sd_end]

writing_first_list = [result for result in writing_list if result > writing_first_sd_start and result < writing_first_sd_end]
writing_second_list = [result for result in writing_list if result > writing_second_sd_start and result < writing_second_sd_end]
writing_third_list = [result for result in writing_list if result > writing_third_sd_start and result < writing_third_sd_end]

math_first_list = [result for result in math_list if result > math_first_sd_start and result < math_first_sd_end]
math_second_list = [result for result in math_list if result > math_second_sd_start and result < math_second_sd_end]
math_third_list = [result for result in math_list if result > math_third_sd_start and result < math_third_sd_end]

print("{} % of data for reading lies within first standard deviation.".format(len(reading_first_list)*100/len(reading_list)))
print("{} % of data for reading lies within second standard deviation.".format(len(reading_second_list)*100/len(reading_list)))
print("{} % of data for reading lies within third standard deviation.".format(len(reading_third_list)*100/len(reading_list)))

print("{} % of data for writing lies within first standard deviation.".format(len(writing_first_list)*100/len(writing_list)))
print("{} % of data for writing lies within second standard deviation.".format(len(writing_second_list)*100/len(writing_list)))
print("{} % of data for writing lies within third standard deviation.".format(len(writing_third_list)*100/len(writing_list)))

print("{} % of data for math lies within first standard deviation.".format(len(math_first_list)*100/len(math_list)))
print("{} % of data for math lies within second standard deviation.".format(len(math_second_list)*100/len(math_list)))
print("{} % of data for math lies within third standard deviation.".format(len(math_third_list)*100/len(math_list)))