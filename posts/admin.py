from django.contrib import admin
from posts.models import Ticket, Review
from authentication.models import User


# @admin.register(Author)
class TicketAdmin(admin.ModelAdmin):
    pass
# Register your models here.


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, TicketAdmin)
admin.site.register(User, TicketAdmin)
