import requests
import json
import matplotlib.pyplot as plt
import numpy as np
from bokeh.plotting import figure, output_file, show

from math import pi

import pandas as pd

from bokeh.io import output_file, show
from bokeh.palettes import Category20c
from bokeh.transform import cumsum
from github import Github

from datetime import datetime as dt
from bokeh.io import output_file
#from bokeh.charts import show
from bokeh.models import DatetimeTickFormatter
from bokeh.plotting import figure

#
#Language Pie Chart
#



def piechart(x):

  output_file("pie.html")
  
  data = pd.Series(x).reset_index(name='value').rename(columns={'index':'country'})
  data['angle'] = data['value']/data['value'].sum() * 2*pi
  if len(x) > 2:
    data['color'] = Category20c[len(x)]
  else:  
    data['color'] = ('#3182bd', '#6baed6')

  p = figure(plot_height=350, title="Pie Chart", toolbar_location=None,
            tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

  p.wedge(x=0, y=1, radius=0.4,
          start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
          line_color="white", fill_color='color', legend_field='country', source=data)

  p.axis.axis_label=None
  p.axis.visible=False
  p.grid.grid_line_color = None

  show(p)


#
# Commit Graph
#
def commitGraph():
  df = pd.DataFrame(data=[1,2,3],
                    index=[dt(2015, 1, 1), dt(2015, 1, 2), dt(2015, 1, 3)],
                    columns=['foo'])
  p = figure(plot_width=400, plot_height=400)
  p.line(df.index, df['foo'])
  p.xaxis.formatter=DatetimeTickFormatter(
          hours=["%d %B %Y"],
          days=["%d %B %Y"],
          months=["%d %B %Y"],
          years=["%d %B %Y"],
      )
  p.xaxis.major_label_orientation = pi/4
  output_file('myplot.html')
  show(p)




#
#Main - Using PyGithub
#
f = open("token.txt", "r")
g = Github(f.read())

repo = g.get_repo("caseyvtcd/Software-Engineering-Metric-Visualisation-Project")
lang = repo.get_languages()


#
#Commit Extraction
#

commits = repo.get_commits()

commitDateList = []
id = []
commitNo = 0


for commit in commits:
  commitDateList.append(commit.commit.committer.date)
  #print(commitDateList)
  id.append(commit.sha)
  commitNo += 1


 #converting data into a form bokeh can use
 
 

# commitList = []
# commitDates = []
# for i in commitDateList:
# 	if i not in commitDates:
# 		commitDates.append(i)
	
#     #converting data into a form bokeh can use

	# cnt = 0

	# for commit in commits:
	# 	for i in authors:
	# 		if commit.author.login == authors[cnt].name:
	# 			authors[cnt].commits += 1
	# 		cnt += 1
	# 	cnt = 0



#
#Graph Output
#

piechart(lang)
commitGraph()




#
#Bokeh Graph Testing
#

# # prepare some data
# x = [1, 2, 3, 4, 5]
# y = [6, 7, 2, 4, 5]

# # output to static HTML file
# output_file("lines.html")

# # create a new plot with a title and axis labels
# p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# # add a line renderer with legend and line thickness
# p.line(x, y, legend_label="Temp.", line_width=2)

# # show the results
# show(p)

# output_file('vbar.html')

# p = figure(plot_width=400, plot_height=400)
# p.vbar(x=[1, 2, 3], width=0.5, bottom=0,
#        top=[1.2, 2.5, 3.7], color="firebrick")

# show(p)





# def get_repos(username):
#   res = requests.get('https://api.github.com/users/' + username + '/repos')
#   return res.json()



# def project_sum(username):
#   data = get_repos(username)
#   total_data_size = 0

#   for j in data:
#     if j['size']:
#       total_data_size += j['size']
#   return total_data_size


# data=(json.dumps(get_repos('caseyvtcd'), indent = 5))
# print(project_sum("caseyvtcd"))


# data = [project_sum("caseyvtcd")]
# X = np.arange(4)
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# ax.bar(X + 0.00, data[0], color = 'b', width = 0.25)

# plt.show()