import requests

# https://jsonplaceholder.typicode.com/users

def get_users ():
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    print(r)
    return r.json()

def create_post (title, content, user_id):
    r = requests.post('https://jsonplaceholder.typicode.com/posts',
                      data={'title': title, 'body': content, 'userId': user_id})
    return r.json()

new_post = create_post('Hello World', 'This is my new post', 1)
# print(new_post)

def get_post_by_id (post_id):
    r = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    return r.json()

def get_all_posts ():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    return r.json()

# print(len(get_all_posts()))

# our_post = get_post_by_id(101)
# print(our_post)

def get_comments_by_post_id (post_id):
    r = requests.get('https://jsonplaceholder.typicode.com/comments', params={'postId': post_id})
    return r.json()

print(len(get_comments_by_post_id(1)))