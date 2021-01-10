from bokeh.models.tickers import YearsTicker
import numpy as np
from bokeh.plotting import figure, output_file, show
from math import pi
import pandas as pd
from bokeh.palettes import Category20c
from bokeh.transform import cumsum
from github import Github
import datetime

from bokeh.models import DatetimeTickFormatter
from bokeh.layouts import gridplot



output_file("layout.html")

#
#Language Pie Chart
#


def display(x, picture, username, df):
  
  data = pd.Series(x).reset_index(name='value').rename(columns={'index':'country'})
  data['angle'] = data['value']/data['value'].sum() * 2*pi
  if len(x) > 2:
    data['color'] = Category20c[len(x)]
  elif (len(x) > 0 and len(x) < 2):  
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
        

  s2 = figure(plot_width=400, plot_height=400, title="Commit Timeline")
  s2.line(df.index, df['score'])
  s2.xaxis.formatter=DatetimeTickFormatter(
          hours=["%d %B %Y"],
          days=["%d %B %Y"],
          months=["%d %B %Y"],
          years=["%d %B %Y"],
      )
  s2.xaxis.major_label_orientation = pi/4

  s3 = figure(title=username, toolbar_location=None, tools="")
  s3.image_url( url=[picture],
             x=1, y=1, w=400, h=400, anchor="bottom_left")
  
  #graph = row(s3, s2, s1)
  grid = gridplot([[s3, s2], [None, s1]], plot_width=350, plot_height=400)
  show(grid)




#
#Main - Using PyGithub
#

f = open("token.txt", "r")
g = Github(f.read())

u = open("user.txt", "r")
r = open("repo.txt", "r")

repo = g.get_repo(r.read())
lang = repo.get_languages()
user = g.get_user(u.read())
picture = user.avatar_url
username = user.login


#
#Commit Extraction
#

commits = repo.get_commits()

commitDateList = []
sizeList = []
id = []
commitNo = 0
i = 0
j = 0
tempDate = []
tempMonth = []
tempYear = []
numTemp = 0

for commit in commits:
      
  day = commit.commit.committer.date.strftime("%d")
  month = commit.commit.committer.date.strftime("%m")
  year = commit.commit.committer.date.strftime("%y")
  
  
  if (day != tempDate or month != tempMonth or year != tempYear):
        commitDateList.append(commit.commit.committer.date)
  #print(commitDateList)
  id.append(commit.sha)
  commitNo += 1
  
  if j == 0:
    sizeList.append(1)

  #print (day, tempDate)
  #print (month, tempMonth)
  #print (year, tempYear)
  
  if(j > 0):
        
        if (day == tempDate and month and tempMonth and year == tempYear):
              numTemp= numTemp + 1
              sizeList[j-numTemp] += 1
        else:
              sizeList.append(1)


  tempDate = day
  tempMonth = month
  tempYear = year
  j= j+1



#print(sizeList)
#converting data into a form bokeh can use
 
 
#
# Converting Datetime data to be processed by the graph
#
 
# Create a datetime variable for today
base = datetime.datetime.today()
# Create a list variable that creates 365 days of rows of datetime values
date_list = commitDateList

score_list = sizeList
#score_list = list(np.random.randint(low=1, high=1000, size=len(commitDateList)))

df = pd.DataFrame()

# Create a column from the datetime variable
df['datetime'] = date_list
# Convert that column into a datetime datatype
df['datetime'] = pd.to_datetime(df['datetime'])
# Set the datetime column as the index
df.index = df['datetime'] 
# Create a column from the numeric score variable
df['score'] = score_list

df.resample('D').mean()


#
#Graph Output
#

display(lang, picture, username, df)
