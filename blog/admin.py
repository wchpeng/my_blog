# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.html import format_html

from my_blog.admin import MyselfInfoList
from blog.adminforms import BlogAdminForm
from blog.models import Blog, BlogCategory, BlogTag
from blog.adminfilters import CreaterTimeFilter


class BlogAdminSite(MyselfInfoList):
    save_on_top = True

    form = BlogAdminForm
    list_editable = ("is_md",)
    filter_horizontal = ("tags",)
    search_fields = ["title", "creater__username"]
    readonly_fields = ["create_time"]
    list_display = ["title", "is_md", "create_time", "operator"]
    list_filter = (
        CreaterTimeFilter,
        ("creater", admin.RelatedOnlyFieldListFilter)
    )

    fieldsets = (
        # ("内容", {"fields": ("title", "text"), "classes": ["collapse"]}),
        ("内容", {"fields": ("title", "is_md", "text_html", "text"), "classes": ["collaps"]}),
        ("分类", {"fields": ("category", "tags")}),
        ("时间", {"fields": ("expire_to", "create_time")})
    )

    def operator(self, obj):
        # html 的话，必须返回 <class 'django.utils.safestring.SafeText'> 格式的数据，否则不会解析
        return format_html('<a href="/admin/blog/blog/' + str(obj.id) + '/change">编辑</a>')

    operator.short_description = "操作"

    class Media:
        js = [
            'myself_admin/toggle_html_and_md.js',
            'http://libs.baidu.com/jquery/2.1.1/jquery.min.js'
        ]
    
    
class BlogTagAdminSite(MyselfInfoList):
    pass


class BlogCategoryAdminSite(MyselfInfoList):
    pass


admin.site.register(Blog, BlogAdminSite)
admin.site.register(BlogTag, BlogTagAdminSite)
admin.site.register(BlogCategory, BlogCategoryAdminSite)

