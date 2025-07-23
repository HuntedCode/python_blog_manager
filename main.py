#!/usr/bin/env python3
from api import fetch_posts

class Post:
    """Represents a blog post from JSONPlaceholder."""

    def __init__(self, data):
        self._userId = data['userId']
        self._id = data['id']
        self._title = data['title']
        self._body = data['body']

    def __str__(self):
        return f"Post #{self._id}: {self._title} - by user: {self._userId}\n\n{self._body}\n"
    
    def get_userId(self):
        return self._userId
    
    def get_id(self):
        return self._id
    
    def get_title(self):
        return self._title
    
    def get_body(self):
        return self._body

def store_posts():
    """Fetches and returns list of Post objects."""

    fetched_posts = fetch_posts()
    posts_list = []

    for item in fetched_posts:
        post = Post(item)
        posts_list.append(post)
    
    return posts_list

def display_posts(posts_list):
    """Prints all posts in param list."""

    if len(posts_list) > 0:
        for post in posts_list:
            print(post)

def process_command(posts_list):
    """Take user input and calls proper function to handle specific commands."""

    accepted_commands = ["view", "search", "exit"]
    raw = input("What would you like to do? view/search/exit: ")
    command = str(raw).lower()

    if command in accepted_commands:
        match command:
            case "view":
                display_posts(posts_list)
                return False
            case "search":
                search_command(posts_list)
                return False
            case "exit":
                return True

def search_command(posts_list):
    """Searches param Post list titles for user input search term."""

    search_phrase = input("Enter the term you'd like to search for:")
    found_posts = []

    for post in posts_list:
        if str(search_phrase).lower() in post.get_title().lower():
            found_posts.append(post)
    
    display_posts(found_posts)

if __name__ == "__main__":
    posts_feed = []
    posts_feed = store_posts()

    while True:
        is_exit_command = process_command(posts_feed)
        if is_exit_command:
            break
    

