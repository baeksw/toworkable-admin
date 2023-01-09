from django.contrib import admin

from django.contrib.auth.models import Group, User

from core.models import TwPatchNote, TwCafe


admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.site_header = "Toworkable Admin"
admin.site.site_title = "Toworkable Admin / 관리자"
admin.site.index_title = "Welcome to B4PLAY TEAM-DATA"

class TwPatchNoteAdmin(admin.ModelAdmin):
    list_display = ('version', 'note')
    list_per_page = 15

class TwCafeAdmin(admin.ModelAdmin):
    list_display = (
        'cafe_name' 
        , 'location' 
        , 'tables' 
        , 'snack' 
        , 'toilet' 
        , 'cafe_size' 
        , 'power_socket' 
    #    , 'address' 
    #    , 'phone' 
    #    , 'ice_coffee' 
    #    , 'latitude' 
    #    , 'longitude'
    )
    search_fields = ( 'cafe_name', 'location')
    list_filter = ( 'location', 'cafe_size', 'tables')
    list_per_page = 20

# 
# class ScodeTypeAdmin(admin.ModelAdmin):
# #    list_display = ('id','code_type', 'code', 'pcode', 'name_en', 'name_ko')
#     list_display = ('id','name_ko', 'name_en' )
# 
# class ScodeTableAdmin(admin.ModelAdmin):
# #    list_display = ('id','code_type', 'code', 'pcode', 'name_en', 'name_ko')
#     list_display = ('code_type', 'name_ko','name_en','code', 'pcode', 'use_yn')
# #     list_editable = (
# #         'name_en'
# #         , 'name_ko'
# #     )
# #    list_filter = ('code_type__name_en',)
#     list_filter = ('code_type__name_ko',)
#     search_fields = ( 'name_en', 'name_ko')
#     readonly_fields = ["code", "pcode", "name_en", "name_ko", "code_type"]
#     list_per_page = 15
# 
#     def has_add_permission(self, request):
#         return False
# 
#     def has_delete_permission(self, request, obj=None):
#         return False

# Register your models here.
admin.site.register(TwPatchNote, TwPatchNoteAdmin) 
admin.site.register(TwCafe, TwCafeAdmin)
# admin.site.register(SCodeTable, ScodeTableAdmin)