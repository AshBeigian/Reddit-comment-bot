import praw
import time
import pickle

try:
    with open('commented_posts.pickle', 'rb') as handle:
        commented_posts = pickle.load(handle)
except FileNotFoundError:
    commented_posts = set()

reddit = praw.Reddit(
    client_id="ID",
    client_secret="SECRET",
    user_agent="<console:bot:1.0>",
    username="USERNAME",
    password="PASSWORD"
)


#example phrases, you can change the variable names and the strings but make sure you replace the variable names in the function below.
chiro = "It sounds like this product would do you well:   https://bonepalshop.com/products/magnetotherapy-back-massager-18186?variant=44138851467560   It gives instant back relief and helps your posture long terms. Not to mention it loosens up your spine and gives your back a nice stretch so you can get rid of your back pain down the line. hope this helps."
neck = "It sounds this product would do you well: https://bonepalshop.com/products/hammock-stretcher-soothes-the-neck  It gives an instant neck pain and headache relief as it reduces the nerve pressure that gets built up in your neck. It also gives a relieving stretch to your neck and upper spine to fix your posture and significantly reduce neck pain and headaches overtime. I use it for instant headache relief. Hope this helps ! "

subreddit = reddit.subreddit('all')


def comment_on_posts(keywords, message):
    for keyword in keywords:
        search = subreddit.search(keyword, sort='new', limit=10) 
        for post in search:
            if post.id not in commented_posts:
                post.reply(message)
                commented_posts.add(post.id)
                with open('commented_posts.pickle', 'wb') as handle:
                    pickle.dump(commented_posts, handle, protocol=pickle.HIGHEST_PROTOCOL)
                time.sleep(10)

#example keywords, you can change the variable names and the strings in the array but make sure you replace the variable names when calling the function below.
keywords_backpain = ["backpain", "back hurts", "lower backpain", "kyphosis", "posture"]
keywords_neckpain = ["neckpain", "heafache", "posture"]

while True:
    comment_on_posts(keywords_backpain, chiro)
    comment_on_posts(keywords_neckpain, neck)
    time.sleep(3600) 
