# Design a class that represents a StackOverflow Post
# It should take two parameters via it's constructor
# a title and a description.
# And make sure to provide a public API that will allow
# the consumer of this class to increase and decrease the votes
# count number without overriding the total votes count directly.

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
