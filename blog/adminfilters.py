# -*- coding:utf-8 -*-
from django.db.models.query_utils import Q
from django.contrib.admin import SimpleListFilter


class CreaterTimeFilter(SimpleListFilter):
    title = "创建时间"
    parameter_name = "create_AT"

    def __init__(self, request, params, model, model_admin):
        # self.get_queryset = model.objects.all()  # 如果这样写的话，前面针对每个用户显示他自己的博客就会出错
        self.get_queryset = model_admin.get_queryset(request)
        super(CreaterTimeFilter, self).__init__(request, params, model, model_admin)
    
    def lookups(self, request, model_admin):
        # 用两种方法返回过滤内容
        # 方法一：返回所有选项
        # return (
        #     ("80s", "80后"),
        #     ("90s", "90后"),
        #     ("other", "其他")
        # )

        # 方法二：只返回存在数据的选项
        if self.get_queryset.filter(create_time__gte="1980-01-01 00:00:00", create_time__lte="1990-01-01 00:00:00"):
            yield ("80s", "80后")
        if self.get_queryset.filter(create_time__gte="1990-01-01 00:00:00", create_time__lte="2000-01-01 00:00:00"):
            yield ("90s", "90后")
        if self.get_queryset.filter(Q(create_time__lte="1980-01-01 00:00:00")|Q(create_time__gte="2000-01-01 00:00:00")):
            yield ("other", "其他")

    def queryset(self, request, queryset):
        if self.value() == "80s":
            return self.get_queryset.filter(create_time__gte="1980-01-01 00:00:00", create_time__lte="1990-01-01 00:00:00")
        if self.value() == "90s":
            return self.get_queryset.filter(create_time__gte="1990-01-01 00:00:00", create_time__lte="2000-01-01 00:00:00")
        if self.value() == "other":
            return self.get_queryset.filter(Q(create_time__lte="1980-01-01 00:00:00") | Q(create_time__gte="2000-01-01 00:00:00"))
        return self.get_queryset.all()
