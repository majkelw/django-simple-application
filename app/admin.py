from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Cat
from .models import User
from .models import UserCatOwner
from .models import Prey
from .models import Hunting
from .models import HuntingDetails

admin.site.register(User)
admin.site.register(UserCatOwner)
admin.site.register(Prey)
admin.site.register(Hunting)
admin.site.register(HuntingDetails)


def boolean_icons(value):
    icon_true = '✅'
    icon_false = '❌'
    html_icon = '<p>{}</p>'
    if value:
        return format_html(html_icon, mark_safe(icon_true))
    else:
        return format_html(html_icon, mark_safe(icon_false))


class Admin(admin.ModelAdmin):
    list_display = ['name', 'color', 'gender_type']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['gender']
        else:
            return []

    def gender_type(self, obj):
        return boolean_icons(obj.gender)


admin.site.register(Cat, Admin)
