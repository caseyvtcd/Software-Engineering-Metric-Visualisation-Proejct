import requests
import json
import matplotlib.pyplot as plt
import numpy as np

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


data = [project_sum("caseyvtcd")]
X = np.arange(4)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(X + 0.00, data[0], color = 'b', width = 0.25)

plt.show()