import requests
import json
import matplotlib.pyplot as plt
import numpy as np
from bokeh.plotting import figure, output_file, show

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# output to static HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(x, y, legend_label="Temp.", line_width=2)

# show the results
show(p)

output_file('vbar.html')

p = figure(plot_width=400, plot_height=400)
p.vbar(x=[1, 2, 3], width=0.5, bottom=0,
       top=[1.2, 2.5, 3.7], color="firebrick")

show(p)





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