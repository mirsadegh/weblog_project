from django.contrib import admin
from .models import Article, Category
# Register your models here.


# Admin header change
admin.site.site_header = "پنل مدیریت"


def make_published(modeladmin, request, queryset):
    rows_updated = queryset.update(status='p')
    if rows_updated == 1:
        message_bit = "منتشر شد"
    else:
        message_bit = "منتشر شدند"
    modeladmin.message_user(
        request, "{} مقاله {}".format(rows_updated, message_bit))


make_published.short_description = "انتشار مقالات انتخاب شده"


def make_draft(modeladmin, request, queryset):
    rows_updated = queryset.update(status='d')
    if rows_updated == 1:
        message_bit = "پیشنویس شد"
    else:
        message_bit = "پیشنویس شدند"
    modeladmin.message_user(
        request, "{} مقاله {}".format(rows_updated, message_bit))


make_draft.short_description = "پیشنویس مقالات انتخاب شده"


def active_cat(modeladmin, request, queryset):
    rows_updated = queryset.update(status=True)
    if rows_updated == 1:
        message_bit = "فعال شد"
    else:
        message_bit = "فعال شدند"
    modeladmin.message_user(
        request, "{} دسته بندی {}".format(rows_updated, message_bit))


active_cat.short_description = "فعال کردن دسته بندی انتخاب شده"


def deActive_cat(modeladmin, request, queryset):
    rows_updated = queryset.update(status=False)
    if rows_updated == 1:
        message_bit = "غیرفعال شد"
    else:
        message_bit = "غیرفعال شدند"
    modeladmin.message_user(
        request, "{} دسته بندی {}".format(rows_updated, message_bit))


deActive_cat.short_description = "غیرفعال کردن دسته بندی انتخاب شده"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'parent', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    actions = [active_cat, deActive_cat]


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_tag', 'slug', 'author',
                    'jpublish', 'status', 'category_to_str')
    list_filter = ('publish', 'status', 'author')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status', '-publish']
    actions = [make_published, make_draft]

    def category_to_str(self, obj):
        return ", ".join([category.title for category in obj.category.active()])
    category_to_str.short_description = 'دسته بندی'


admin.site.register(Article, ArticleAdmin)
