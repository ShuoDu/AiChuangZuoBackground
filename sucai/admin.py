from django.contrib import admin

from .models import deck_type
from .models import field_type
from .models import message
from .models import message_img

admin.site.register(deck_type)
admin.site.register(field_type)
admin.site.register(message)
admin.site.register(message_img)
