import requests
import json
import matplotlib.pyplot as plt
import numpy as np

def get_repos(username):
  res = requests.get('https://api.github.com/users/' + username + '/repos')
  return res.json()


#
#Repository size finder
#

def project_sum(username):
  data = get_repos(username)
  total_data_size = 0

  for j in data:
    if j['size']:
      total_data_size += j['size']
  return total_data_size


data=(json.dumps(get_repos('caseyvtcd'), indent = 5))
#print(project_sum("caseyvtcd"))

data=(json.dumps(get_repos('keaneyjo'), indent = 5))
#print(project_sum("keaneyjo"))


#
# single bar chart
#

# data = [project_sum("caseyvtcd")]
# X = np.arange(2)
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# ax.bar(X + 0.00, data[0], color = 'b', width = 0.25)

#
#bar chart 2
#

# N = 5
# menMeans = (20, 35, 30, 35, 27)
# womenMeans = (25, 32, 34, 20, 25)
# menStd = (2, 3, 4, 1, 2)
# womenStd = (3, 5, 2, 3, 3)
# ind = np.arange(N)    # the x locations for the groups
# width = 0.35       # the width of the bars: can also be len(x) sequence

# p1 = plt.bar(ind, menMeans, width, yerr=menStd)
# p2 = plt.bar(ind, womenMeans, width,
#              bottom=menMeans, yerr=womenStd)

# plt.ylabel('Scores')
# plt.title('Scores by group and gender')
# plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
# plt.yticks(np.arange(0, 81, 10))
# plt.legend((p1[0], p2[0]), ('Men', 'Women'))


#
#bar chart 3
#

# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ('caseyvtcd', 'keaneyjo')
y_pos = np.arange(len(people))
#performance = 3 + 10 * np.random.rand(len(people))
users = [project_sum("caseyvtcd"), project_sum("keaneyjo")]
error = np.random.rand(len(people))

ax.barh(y_pos, users, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Size (kb)')
ax.set_title('What is the combined size of your repositories?')

#
#display
#

plt.show()