import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
dice_result=[]
for i in range (0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)
mean = sum(dice_result)/len(dice_result)
standardDeviation = statistics.stdev(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)
print("mean of the data is" , mean)
print("standard deviation is", standardDeviation)
print("mode:", mode)
print("median", median)
fstdevstart,fstdevend=mean-standardDeviation, mean + standardDeviation
sstdevstart,sstdevend=mean-(2*standardDeviation), mean + (2*standardDeviation)
tstdevstart,tstdevend=mean-(3*standardDeviation), mean + (3*standardDeviation)
fig=ff.create_distplot([dice_result],["result"],show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[fstdevstart,fstdevend], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[fstdevstart, fstdevend], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[sstdevstart, sstdevend], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[sstdevstart, sstdevend], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
list_of_data_within_1_std_deviation = [result for result in dice_result if result > fstdevstart and result < fstdevend]
list_of_data_within_2_std_deviation = [result for result in dice_result if result > sstdevstart and result < sstdevend]
list_of_data_within_3_std_deviation = [result for result in dice_result if result > tstdevstart and result < tstdevend]
print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("Standard Deviation of this data is {}".format(standardDeviation))

print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(dice_result)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(dice_result)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(dice_result)))

fig.show()