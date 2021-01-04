import requests
import json
import matplotlib.pyplot as plt

def get_repos(username):
  res = requests.get('https://api.github.com/users/' + username + '/repos')
  return res.json()



def project_sum(username):
  data = get_repos(username)
  total_data_size = 0

  for j in data:
    if j['size']:
      total_data_size += j['size']
  return total_data_size


data=(json.dumps(get_repos('caseyvtcd'), indent = 5))
print(project_sum("caseyvtcd"))


labels = ['G1', 'G2', 'G3', 'G4', 'G5']
third_means = [20, 35, 30, 35, 27]
fourth_means = [25, 32, 34, 20, 25]
third_std = [2, 3, 4, 1, 2]
fourth_std = [3, 5, 2, 3, 3]
width = 0.35       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

ax.bar(labels, third_means, width, yerr=third_std, label='3rd')
ax.bar(labels, third_means, width, yerr=third_std, bottom=third_means,
       label='4th')

ax.set_ylabel('Scores')
ax.set_title('Scores by group and year')
ax.legend()

plt.show()