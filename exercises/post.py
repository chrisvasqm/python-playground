class Post(object):

    def __init__(self, title, description):
        self.title = title
        self.description = description
        self._votes = 0

    @property
    def votes(self):
        return self._votes

    def upVote(self):
        self._votes += 1

    def downVote(self):
        self._votes -= 1


post = Post(title="Title", description="Description")

print(f'The {post.title} post has {str(post.votes)} votes')

post.upVote()

print(f'The {post.title} post has {str(post.votes)} votes')

post.downVote()

print(f'The {post.title} post has {str(post.votes)} votes')
