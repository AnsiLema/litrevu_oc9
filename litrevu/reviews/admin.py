from django.contrib import admin

from reviews.models import Review
from reviews.models import User

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "year_of_release", "genre")

admin.site.register(Review, ReviewAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "review")

admin.site.register(User, UserAdmin)
