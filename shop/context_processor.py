from shop.models import Cart


def get_cart(request):
    cart_id = request.session.get('cart_id')
    if cart_id is None:
        cart = Cart.objects.create(
            session_id=request.session.session_key,
            active=True
        )

        if request.user.is_authenticated:
            cart.owner = request.user
            cart.save()

        request.session['cart_id'] = cart.id
    else:
        try:
            cart = Cart.objects.get(pk=cart_id)
        except Cart.DoesNotExist:
            del request.session['cart_id']
            return None
    return cart


def process(request):
    return {
        "cart": get_cart(request)
    }