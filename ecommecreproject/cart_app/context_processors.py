from.models import Carts,CartItems
from .views import _cart_id


def counter(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=Carts.objects.filter(cart_id=_cart_id(request))
            carts_item=CartItems.objects.all().filter(cart=cart[:1])
            for cart_item in carts_item:
                item_count += cart_item.quantity
        except Carts.DoesNotExist:
            item_count =0
    return  dict(item_count=item_count)


