from shop.context_processor import get_cart


def cart_middleware(get_response):
    def inner(request):
        request.cart = get_cart(request)
        return get_response(request)
    return inner
