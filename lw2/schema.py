from graphene_django import DjangoObjectType
import graphene
from django.contrib.auth.models import User
from .models import Post, Comment, Vote
import pdb

class UserType(DjangoObjectType):
    class Meta:
        model = User

class VoteType(DjangoObjectType):
    class Meta:
        model = Vote

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment

class PostType(DjangoObjectType):
    class Meta:
        model = Post
    _id = graphene.String(name="_id")
    user_id = graphene.String()
    page_url = graphene.String(default_value="")
    word_count = graphene.Int(default_value=1)
    all_votes = graphene.List(VoteType, resolver=lambda x,y: [])

    def resolve__id(self,info):
        #TODO: Make sure we actually grab the correct value here
        document_id = info.operation.selection_set.selections[0].arguments[0].value.value
        try:
            document = Post.objects.get(id=document_id)
        except:
            return "error"
        return document_id
    
    def resolve_user_id(self, info):
        #TODO: Make sure we actually grab the correct value here
        document_id = info.operation.selection_set.selections[0].arguments[0].value.value
        try:
            document = Post.objects.get(id=document_id)
        except:
            return "error"
        return document.user.id
        
class Query(object):
    user = graphene.Field(UserType,
                          id=graphene.Int(),
                          username=graphene.String())
    all_users = graphene.List(UserType)
    posts_single = graphene.Field(PostType,
                                  _id=graphene.String(name="_id"),
                                  posted_at=graphene.types.datetime.DateTime(),
                                  frontpage_date = graphene.types.datetime.Date(),
                                  curated_date = graphene.types.datetime.Date(),
                                  userId = graphene.String(),
                                  document_id = graphene.String(),
                                  name="PostsSingle")
    all_posts = graphene.List(PostType)
    comment = graphene.Field(CommentType,
                             id=graphene.String(),
                             posted_at=graphene.types.datetime.Date(),
                             userId = graphene.Int())
    all_comments = graphene.List(CommentType)

    vote = graphene.Field(VoteType,
                          id=graphene.Int())

    all_votes = graphene.List(VoteType)
    
    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')

        if id:
            return User.objects.get(id=id)
        if username:
            return User.objects.get(username=username)

        return None
    
    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_posts_single(self, info, **kwargs):
        id = kwargs.get('document_id')
        if id:
            return Post.objects.get(id=id)

        return None
        
    def resolve_all_posts(self, info, **kwargs):
        return Post.objects.all()

    def resolve_comment(self, info, **kwargs):
        id = kwargs.get('id')

        if id:
            return Post.objects.get(id=id)

        return None

    def resolve_all_comments(self, info, **kwargs):
        return Comment.objects.select_related('post').all()

    def resolve_vote(self, info, **kwargs):
        id = kwargs.get('id')

        if id:
            return Vote.objects.get(id=id)

        return None
        
