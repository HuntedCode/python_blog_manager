from api import fetch_posts

post_feed = []

class Post:

    def __init__(self, data):
        self.userId = data['userId']
        self.id = data['id']
        self.title = data['title']
        self.body = data['body']

    def __str__(self):
        return f"Post #{self.id}: {self.title} - by user: {self.userId}\n\n{self.body}\n"
    
    def get_userId(self):
        return self.userId
    
    def get_id(self):
        return self.id
    
    def get_title(self):
        return self.title
    
    def get_body(self):
        return self.body


posts_list = fetch_posts()
print(len(posts_list))

if len(posts_list) > 0:
    for item in posts_list:
        post = Post(item)
        print(post)