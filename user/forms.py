from django import forms

from .models import Post, Blog


class ArticlePost(forms.ModelForm):
    def __init__(self, user, type_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.type_name = type_name
        for field_name in ['title', 'description']:
            self.fields[field_name].help_text = None
            self.fields[field_name].label = ''

    class Meta:
        model = Post
        fields = ['title', 'description']

    def save(self, commit=True):
        post = super().save(commit=False)
        post.blog = Blog.objects.get(user=self.user)
        post.type = self.type_name
        if commit:
            post.save()
        return post


class FilePost(ArticlePost):
    def __init__(self, user, type_name, allowed_type, *args, **kwargs):
        super().__init__(user, type_name, *args, **kwargs)
        self.allowed_type = allowed_type
        self.fields['file'].help_text = None
        self.fields['file'].label = ''

    class Meta:
        model = Post
        fields = ['title', 'description', 'file']

    def is_valid(self):
        if not super().is_valid():
            return False

        file = self.cleaned_data.get('file')

        if file:
            filename = file.name
            if filename.split('.')[1] in self.allowed_type:
                return True

        return False


def get_form(type_name, user, data_post=None, data_files=None):
    if type_name == 'article':
        return ArticlePost(user, type_name, data_post)

    if type_name == 'video':
        return FilePost(user, type_name, ['mp4'], data_post, data_files)

    if type_name == 'image':
        return FilePost(user, type_name, ['jpg'], data_post, data_files)
