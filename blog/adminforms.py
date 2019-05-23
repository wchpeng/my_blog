# -*- coding:utf-8 -*-
from django import forms

from blog.models import BlogTag, BlogCategory
from my_blog.middleware import get_request_user_filter
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from utils.markdown_util import md2html
from mdeditor.widgets import MDEditorWidget


class BlogAdminForm(forms.ModelForm):
    exclude = ["author"]
    text = forms.CharField(widget=MDEditorWidget, label="md内容", required=False)
    text_html = forms.CharField(widget=CKEditorUploadingWidget(), label="html 内容", required=False)

    category = forms.ModelChoiceField(
        queryset=BlogCategory.objects,
        limit_choices_to=get_request_user_filter,
        label='类型'
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=BlogTag.objects,
        widget=forms.CheckboxSelectMultiple,
        limit_choices_to=get_request_user_filter,
        label='标签'
    )

    def clean(self):
        if self.cleaned_data.get("is_md"):
            self.cleaned_data["text_html"] = md2html(self.cleaned_data.get("text"))
        return self.cleaned_data
