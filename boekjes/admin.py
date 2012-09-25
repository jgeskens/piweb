from django.contrib import admin

from boekjes.models import Box, Book, Category


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'id', 'box', 'category', 'hardcover')
    list_filter = ('box', 'category', 'hardcover')
    search_fields = ('box__name', 'title', 'author')
admin.site.register(Book, BookAdmin)


class BookInline(admin.TabularInline):
    model = Book
    fields = ('title', 'author', 'category', 'hardcover')
    extra = 20


class BoxAdmin(admin.ModelAdmin):
    list_display = ('number', 'name')
    search_fields = ('name',)
    inlines = (BookInline,)
admin.site.register(Box, BoxAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Category, CategoryAdmin)
