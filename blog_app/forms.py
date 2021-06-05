from django import forms
from django.forms import widgets
from blog_app.models import Post,Comment
#Now creating forms 
class PostForm(forms.ModelForm):

    class Meta():
        model=Post
        fields=('author','title','text')   #Now creating connection with html file input widgets

        widgets={
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }


#Now creating Form for inputting comment
class CommentForm(forms.ModelForm):

    class Meta():
        model=Comment
        fields=('author','comment')

        widgets={
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'comment':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
