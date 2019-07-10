from django.contrib import admin

# Register your models here.
from .models import Articles, Classify, Comments


@admin.register(Articles)
class ArticleAdmin(admin.ModelAdmin):
    # 这个的作用是给出一个筛选机制，一般按照时间比较好
    date_hierarchy = 'add_time'
    exclude = ('views',)
    # 在查看修改的时候显示的属性，第一个字段带有<a>标签，所以最好放标题
    list_display = ('id', 'title', 'author', 'add_time')

    # 设置需要添加<a>标签的字段
    list_display_links = ('title',)
    # 激活过滤器，这个很有用
    list_filter = ('add_time', 'classify')
    list_per_page = 10  # 每页数量

    def get_queryset(self, request):
        qs = super(ArticleAdmin, self).get_queryset(request)
        if request.user.is_authenticated:
            return qs
        else:
            return qs.filter(author=request.user)


@admin.register(Classify)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)



@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'comment_time'
    list_display = ('id', 'comment_person', 'comment_time', 'comment_content')
    ordering = ('-id',)
    # 设置需要添加a标签的字段
    list_display_links = ('id', 'comment_content')

    # 使用方法来自定义一个字段，并且给这个字段设置一个名称
    def show_content(self, obj):
        return obj.content[:30]

    show_content.short_description = '评论内容'
    list_per_page = 10  # 每页数量

# 自定义管理站点的名称和URL标题
admin.site.site_header = '网站管理'
admin.site.site_title = '博客后台管理'
