import pandas as pd
import seaborn as sns
import copy

data = pd.read_csv('C:\\Users\\olegb\\Downloads\\United States of America-2019.csv')

data = data[::-1] #Reverse order
total_pop = sum(data['M']) + sum(data['F'])
data_for_graph = copy.deepcopy(data)
data_for_graph['M'] = (-1)*data_for_graph['M']
data_for_graph['M %'] = 100*data['M']/total_pop
data_for_graph['F %'] = 100*data['F']/total_pop

bar_plot = sns.barplot(x = 'M', y = 'Age', data = data_for_graph, color = 'lightskyblue')
bar_plot = sns.barplot(x = 'F', y = 'Age', data = data_for_graph, color = 'pink')
bar_plot.set(xlabel="Population (hundreds of millions)", ylabel="Age Group", title = "Population Pyramid")

#There are two spikes on the pyramid peaking ages 55-59 years which shows the baby boomers population and second spike centered at 25-29 years indicates Millenials population

bar_plot = sns.barplot(x = 'M %', y = 'Age', data = data_for_graph, color = 'lightskyblue')
bar_plot = sns.barplot(x = 'F %', y = 'Age', data = data_for_graph, color = 'pink')
bar_plot.set(xlabel="Population (percent)", ylabel="Age Group", title = "Population Pyramid")

#Lets take a closer look at the populations by gender
data2 = pd.melt(data, id_vars = 'Age', var_name='Sex', value_name='Count')
cat_plot = sns.catplot(x = 'Count', y = 'Age', hue = 'Sex', data = data2)
cat_plot.set(xlabel="Population (hundreds of millions)", ylabel="Age Group", title = "Population by Sex", legend = 'Gender')

#From the chart we can conclude that on average there are more males born than females, however females tend to live longer than males
