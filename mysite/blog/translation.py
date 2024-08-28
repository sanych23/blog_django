from modeltranslation.translator import translator, TranslationOptions
from .models import CategoryPost, Posts, Comment



class CategoryPostTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'keywords',)


class PostsTranslationOptions(TranslationOptions):
    fields = ("title", "content",)


class CommentTranslationOptions(TranslationOptions):
    fields = ("content",)


translator.register(CategoryPost, CategoryPostTranslationOptions)
translator.register(Posts, PostsTranslationOptions)
translator.register(Comment, CommentTranslationOptions)

