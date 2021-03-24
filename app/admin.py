from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Cat
from .models import User
from .models import UserCatOwner
from .models import Prey
from .models import Hunting
from .models import HuntingDetails


def boolean_icons(value):
    icon_true = '✅'
    icon_false = '❌'
    html_icon = '<p>{}</p>'
    if value:
        return format_html(html_icon, mark_safe(icon_true))
    else:
        return format_html(html_icon, mark_safe(icon_false))


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'cats_number']


class CatAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'color', 'gender_type']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['gender']
        else:
            return []

    def gender_type(self, obj):
        return boolean_icons(obj.gender)


class PreyAdmin(admin.ModelAdmin):
    list_display = ['id', 'type']


class HuntingAdmin(admin.ModelAdmin):
    list_display = ['id', 'cat', 'duration']


class HuntingDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'hunting', 'cat', 'prey']


class UserCatOwnerAdmin(admin.ModelAdmin):
    list_display = ['user', 'cat']


admin.site.register(Cat, CatAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserCatOwner,UserCatOwnerAdmin)
admin.site.register(Prey, PreyAdmin)
admin.site.register(Hunting, HuntingAdmin)
admin.site.register(HuntingDetails, HuntingDetailsAdmin)
