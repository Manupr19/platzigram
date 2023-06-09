#profile
from users.models import Profile
from django.contrib.auth.models import User
#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUseradmin
# Register your models here.
#admin.site.register(Profile)
@admin.register(Profile) #se llama decorador para hacerlo en una linea
class ProfileAdmin(admin.ModelAdmin):
    list_display=('pk','user','phone_number','website','picture')
    list_display_links=('pk','user')
    list_editable=('phone_number','website','picture')

    search_fields = ('user__email','user__username','user__first_name','user__last_name','phone_number')
    list_filter=('created','modified','user__is_active','user__is_staff')

    fieldsets=(
        ('Profile',{
            'fields':
            (('user','picture'),
             ),
        }),
        ('Extra info', {
        
        'fields':(('website','phone_number'),
                  ('biography')
        

        )
        })
    )
    class ProfileInline(admin.StackedInline):
        model = Profile
        can_delete = False
        verbose_name_plural='profiles'

    class UserAdmin(BaseUseradmin):
        #añadir profile admin to base user admin
        #inlines=(ProfileInline,)
        list_display=(
            'username',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'is_staff',

        )

    admin.site.unregister(User)
    admin.site.register(User,UserAdmin)
