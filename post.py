class Post:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.votes = 0
    
    def upVote(self):
        self.votes += 1

    def downVote(self):
        self.votes -= 1

post = Post(title="Title", description="Description")

print("The " + post.title + " post has " + str(post.votes) + " votes")

post.upVote()

print("The " + post.title + " post has " + str(post.votes) + " votes")

post.downVote()

print("The " + post.title + " post has " + str(post.votes) + " votes")