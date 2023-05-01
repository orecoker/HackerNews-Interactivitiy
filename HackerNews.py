# This project, started on March 9, 2023, was created to explore a data set of posts made on a webpage and create insights. 
# Using a dataset of posts from HackerNews as my source, I will look through the data and specifically look at posts beginning with Ask HN or Show HN.
# I will compare the two types of posts to see what gains the most interaction.

#import packages
import pandas as pd

#request 
path = '/Users/orecoker/Desktop/SPRING 23 COURSEWORK/Python Project/'
file = 'HN_posts_year_to_Sep_26_2016.csv'
df = pd.read_csv(path + file, on_bad_lines='skip')
df

#remove all posts with 0 comments, 0 interactivity
df = df[df['num_comments'] != 0]
df    

#display first 10 rows of data frame
df.head(10)

#print column titles (id, title, url, num_points, num_comments, author, created_at)
df.columns

#take random sample from the data set
df = df.sample(frac=0.10, replace=False)
df
#transforms dataframe to list
hn = df.values.tolist()
hn[0:5]

#iterates through list to check for Ask HN, Show HN, and Other and append to lists
ask_posts = []
show_posts = []
other_posts = []

for i in hn:
    title = i[1]
    if title.lower().startswith('ask hn'):
        ask_posts.append(i)
    elif title.lower().startswith('show hn'):
        show_posts.append(i)
    else:
        other_posts.append(i)

#check length of each list
len(ask_posts)
len(show_posts)
len(other_posts)

#determine how many total and avg comments in ask posts
total_ask_comments = 0

for i in ask_posts:
    total_ask_comments += i[4]
    
total_ask_comments

avg_ask_comm = total_ask_comments / len(ask_posts)
avg_ask_comm

#determine how many total and avg comments in show posts
total_show_comments = 0

for i in show_posts:
    total_show_comments += i[4]
    
total_show_comments

avg_show_comm = total_show_comments / len(show_posts)
avg_show_comm

#ask posts on average recieved approximately 3 more comments than show posts

#determine how many points (total/avg) ask posts recieve
total_ask_points = 0

for i in ask_posts:
    total_ask_points += i[3]
    
total_ask_points

avg_ask_points = total_ask_points / len(ask_posts)
avg_ask_points

#determine how many points (total/avg) show posts recieve
total_show_points = 0

for i in show_posts:
    total_show_points += i[3]
    
total_show_points

avg_show_points = total_show_points / len(show_posts)
avg_show_points

#while ask posts recieved more comments on average, show posts recieved approx 15 more points on average
#this makes logical sense, when people ask questions, others are likely to respond in comments.
#when people make a post showing their work, others will upvote/rate it points so others may see the work.

#This project was completed on March 9, 2023.