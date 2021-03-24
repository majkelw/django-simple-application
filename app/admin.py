from django.contrib import admin
from .models import Cat
from .models import User
from .models import UserCatOwner
from .models import Prey
from .models import Hunting
from .models import HuntingDetails

admin.site.register(Cat)
admin.site.register(User)
admin.site.register(UserCatOwner)
admin.site.register(Prey)
admin.site.register(Hunting)
admin.site.register(HuntingDetails)
