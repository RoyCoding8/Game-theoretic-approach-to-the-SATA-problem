from classes import *
import pandas as pd

# Each group is a task, and each user is a worker

# Tag_id and tag name mapping (skills)
df = pd.read_csv(r'.\Data\Meetup_tag\tag_text.csv')
tag_text = dict(zip(df['id'],df['text']))

# User and interested tag_ids (skills of user)
df = pd.read_csv(r'.\Data\Meetup_tag\user_tag.csv')
user_tag = dict()
for _,row in df.iterrows():
    key=row['user']
    value=row['tag_id']
    if key not in user_tag:
        user_tag[key]=[]
    user_tag[key].append(value)

# Group and tag_ids (skills required in a group)
df = pd.read_csv(r'.\Data\Meetup_tag\group_tag.csv')
group_tag = dict()
for _,row in df.iterrows():
    key=row['group']
    value=row['tag_id']
    if key not in group_tag:
        group_tag[key]=[]
    group_tag[key].append(value)

# User and group participated mapping (tasks done by worker online before)
df = pd.read_csv(r'.\Data\Meetup_network\user_group.csv')
user_group = dict()
for _,row in df.iterrows():
    key=row['user']
    value=row['group']
    if key not in user_group:
        user_group[key]=[]
    user_group[key].append(value)

# User and event participated mapping and each event is in turn mapped to a group (tasks done by worker offline)
df = pd.read_csv(r'.\Data\Meetup_network\user_event.csv')
user_event = dict()
for _,row in df.iterrows():
    key=row['user']
    value=row['event']
    if key not in user_event:
        user_event[key]=[]
    user_event[key].append(value)

df = pd.read_csv(r'.\Data\Meetup_network\event_group.csv')
event_group = dict(zip(df['event'],df['host_group']))

# Location
df = pd.read_csv(r'.\Data\Meetup_geo\user_lon_lat.csv')
user_location=dict[int,list[float]]()
for _,row in df.iterrows():
    key=row['user']
    values=[row['lon'],row['lat']]
    user_location[key]=values

df = pd.read_csv(r'.\Data\Meetup_geo\event_lon_lat.csv')
event_location=dict[int,list[float]]()
for _,row in df.iterrows():
    key=row['event']
    values=[row['lon'],row['lat']]
    event_location[key]=values

print(event_location)