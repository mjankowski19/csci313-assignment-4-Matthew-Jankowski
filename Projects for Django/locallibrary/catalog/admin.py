from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language

admin.site.register(Genre)
admin.site.register(Language)

class BooksInline(admin.TabularInline):
    model = Book

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
admin.site.register(Author, AuthorAdmin)

# Register the Admin classes for Book using the decorator
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
admin.site.register(Book, BookAdmin)

# Register the Admin classes for BookInstance using the decorator
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )

admin.site.register(BookInstance, BookInstanceAdmin)
