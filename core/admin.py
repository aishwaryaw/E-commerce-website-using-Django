from django.contrib import admin
from core.models import Item, Order, OrderItem, Coupon, Address, Payment, Refund, UserProfile
# Register your models here.

def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested = False, refund_granted = True)

make_refund_accepted.short_description = 'Update orders to refund granted'


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'ordered',
        'being_delivered',
        'received',
        'refund_requested',
        'refund_granted',
        'shipping_address',
        'billing_address',
        'coupon',
        'payment'
    ]

    list_filter = [
        'ordered',
        'being_delivered',
        'received',
        'refund_requested',
        'refund_granted',
    ]

    list_display_links = [
        'user',
        'shipping_address',
        'billing_address',
        'coupon',
        'payment'
    ]

    search_fields = [
        'user__username',
        'ref_code'
    ]
    actions = [ make_refund_accepted ]

class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'address_type',
        'default'
    ]

    list_filter = [
        'default', 'address_type', 'country'
    ]

    search_fields = [ 'user__username', 'street_address', 'apartment_address', 'zip' ]


admin.site.register(Item)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Coupon)
admin.site.register(Address, AddressAdmin)
admin.site.register(Payment)
admin.site.register(Refund)
admin.site.register(UserProfile)
