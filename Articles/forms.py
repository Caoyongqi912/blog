from django import forms
from django.forms import fields


class CommentForm(forms.Form):
    comment_content = fields.CharField(required=False)
    comment_img = fields.ImageField(required=False)
