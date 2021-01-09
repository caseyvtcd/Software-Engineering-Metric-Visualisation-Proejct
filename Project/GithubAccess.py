from bokeh.models.tickers import YearsTicker
import requests
import json
import matplotlib.pyplot as plt
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import row, column
from math import pi
import pandas as pd
from bokeh.palettes import Category20c
from bokeh.transform import cumsum
from github import Github
from datetime import datetime as dt
#from bokeh.charts import show
from bokeh.models import DatetimeTickFormatter
from bokeh.layouts import gridplot



output_file("layout.html")

#
#Language Pie Chart
#


def display(x, picture, username):
  
  data = pd.Series(x).reset_index(name='value').rename(columns={'index':'country'})
  data['angle'] = data['value']/data['value'].sum() * 2*pi
  if len(x) > 2:
    data['color'] = Category20c[len(x)]
  elif len(x) > 0:  
    data['color'] = ('#3182bd')
  else:
    data['color'] = ('#3182bd', '#6baed6')

  s1 = figure(plot_height=300, title="Languages Used", toolbar_location=None,
            tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

  s1.wedge(x=0, y=1, radius=0.4,
          start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
          line_color="white", fill_color='color', legend_field='country', source=data)

  s1.axis.axis_label=None
  s1.axis.visible=False
  s1.grid.grid_line_color = None

  #
  #Commit Graph
  #

  df = pd.DataFrame(data=[1,2,3],
                    index=[dt(2015, 1, 1), dt(2015, 1, 2), dt(2015, 1, 3)],
                    columns=['foo'])
  s2 = figure(plot_width=400, plot_height=400, title="Commit Timeline")
  s2.line(df.index, df['foo'])
  s2.xaxis.formatter=DatetimeTickFormatter(
          hours=["%d %B %Y"],
          days=["%d %B %Y"],
          months=["%d %B %Y"],
          years=["%d %B %Y"],
      )
  s2.xaxis.major_label_orientation = pi/4

  s3 = figure(title=username, toolbar_location=None, tools="")
  s3.image_url( url=[picture],
             x=1, y=1, w=253, h=409, anchor="bottom_left")
  
  #graph = row(s3, s2, s1)
  grid = gridplot([[s3, s1], [s2]], plot_width=500, plot_height=400)
  show(grid)




#
#Main - Using PyGithub
#
f = open("token.txt", "r")
g = Github(f.read())

repo = g.get_repo("caseyvtcd/Software-Engineering-Metric-Visualisation-Project")
lang = repo.get_languages()
user = g.get_user("caseyvtcd")
picture = user.avatar_url
username = user.login


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
#            commitList.append(commitDates(i, 0))
#            commitDates.append(i)
    
	
    #converting data into a form bokeh can use

	# cnt = 0

	# for commit in commits:
	# 	for i in authors:
	# 		if commit.author.login == authors[cnt].name:
	# 			authors[cnt].commits += 1
	# 		cnt += 1
	# 	cnt = 0


class CommitDate:
    	def __init__(self, date, commitNo):
		    self.date = date
		    self.commits = commitNo


#
#Graph Output
#

display(lang, picture, username)
