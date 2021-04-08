import requests

from plotly.graph_objs import bar       ### import Bar and offline modules from  plotly
from plotly import offline

# Make an API call and store the response.      ### print status of API call to be aware of problem
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process results.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []      ### three empty lists are created to store data of initial chart and name updated to repo_links
for repo_dict in repo_dicts:        ### loops through all the dictionaries in repo_dicts
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']        ### pulls URL for project from repo_dict and assign to temp variable repo_url
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']     ### the loop that processes data, we pull owner and project descriptions
    description = repo_dict['description']
    label = f"{owner}<br />{description}"       ### Plotly allows use of HTML code withing text elements and here a line break is used between project names and description
    labels.append(label)

# Make visualization.
data = [{
	'type': 'bar',
	'x': repo_links,       ### creates links to projects on Github from bar chart directly
	'y': stars,
    'hovertext': labels,        ### this key allows for displaying of data when hovering over a certain bar
    'marker': {
        'color': 'rgb(60, 100, 150)',        ### sets colors of bars on chart
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}      ### applies a dark gray outline to chart bars
    },
    'opacity': 0.6,      ### opacity softens appearance of chart a bit
}]

my_layout = {       ### instead of building this chart with a Layout class, a dictionary defines the layout specifications
	'title': 'Most-Starred Python Projects on Github',
    'titlefont': {'size': 28},
	'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
	'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')