from operator import itemgetter

import requests

# Make an API call and store the respoonse.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'       ### make an API call and print status of response
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()       ### convert the response object to a Python list and store in submission_ids
submission_dicts = []       ### set up an empty list to store these dictionaries
for submission_id in submission_ids[:30]:
    # Make a seperate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"        ### make a new API call generating a URL that includes current value of submission_id
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    try:
        submission_dict = {     ### create a dictionary to store title, links, and comment of articles received
            'title': response_dict['title'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
    except KeyError:
        # This is a special YC post with comments disabled.
        continue

    else:
        submission_dicts.append(submission_dict)        ### resulting list is appended to submission_dicts

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
