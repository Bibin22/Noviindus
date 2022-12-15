from .models import *
from datetime import datetime,date, timedelta
from django.utils import timezone
from django.db.models import Q
def cart_count(request):
    if request.user.id != None:
        cart_count = Cart.objects.filter(user=request.user).count()
    else:
        cart_count = 0
    return {'cart_count': cart_count}

