from django.conf import settings

def cart_contents(request):
    """ Function to return a dictionary to all templates """

    # list to hold the cart contents
    cart_plan = []
    total = 0
    product_count = 0

    context = {}

    return context