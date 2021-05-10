import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics
import random
import csv
import pandas as pd 

df =pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()




def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
        mean = statistics.mean(dataset)
        return mean 

        mean_list = []
        for i in range(0,1000):
            set_of_means = random_set_of_mean(100)
            mean_list.append(set_of_means)

std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
first_std_deviation_start,first_std_deviation_end = mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end = mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end = mean-(3*std_deviation),mean+(3*std_deviation)

print("std1",first_std_deviation_start,first_std_deviation_end)
print("std2",second_std_deviation_start,second_std_deviation_end)
print("std3",third_std_deviation_start,third_std_deviation_end)


print("mean of sampling distribution",mean)
fig = ff.create_distplot([data],["student_marks"],show_hist= False)
fig.add_trace(go.Scatter(x=[mean,mean],y = [0,0.20],mode="lines",name= "MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_end],y = [0,0.17],mode="lines",name = "STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_end],y = [0,0.17],mode="lines",name = "STANDARD DEVIATION 1 END"))

fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_end],y = [0,0.17],mode="lines",name = "STANDARD DEVIATION 2 START"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_end],y = [0,0.17],mode="lines",name = "STANDARD DEVIATION 2 END"))

fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_end],y = [0,0.17],mode="lines",name = "STANDARD DEVIATION 3 START"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_end],y = [0,0.17],mode="lines",name = "STANDARD DEVIATION 3 END"))



fig.show()