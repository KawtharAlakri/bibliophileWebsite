from django import forms

class ReviewForm(forms.Form):
    title = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea())

class BookForm(forms.Form):
    title = forms.CharField(max_length=150)
    author = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea())
    pages = forms.IntegerField()
    genre = forms.CharField(max_length=100)
    ISBN = forms.CharField(max_length=100)
    cover = forms.FileField()
