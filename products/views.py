from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Item
from .serializers import ItemSerializer, MenuItemSerializer
from rest_framework.decorators import api_view
from .models import MenuItem

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

# Create your views here.
class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def menu_list(request):
    # hardcoded menu items
    menu_items = [
        {'name': 'Margherita Pizza','price': '199','desc': 'Classic cheese & tomato'},
        {'name': 'Veg Burger', 'price': '149', 'desc': 'Patty with fresh veggies'},
        {'name': 'Pasta Alferfo', 'price': '129', 'desc': 'Creamy garalic sauce'},
    ]
    return render(request, 'products/menu.html', {'menu_items': menu_items})



@api_view(['GET','POST'])
def menuitem_list_create(request):
    try:
        if request.method == 'GET':
            qs = MenuItem.objects.all().order_by('-created_at')
            rid = request.query_params.get('restaurant')
            if rid: qs = qs.filter(restaurant_id = rid)
            return Response(MenuItemSerializer(qs,many= True).data)

        s = MenuItemSerializer(data = request.data)
        s.is_valid(raise_exception = True)
        s.save()
        return Response(s.data, status = status.HTTP_201_CREATED)

    except DatabaseError:
        return Response({'detail':'db error'}, status = status.HTTP_500_INTERNAL_SERVER_ERROR))
    except Exception:
        return Response('detail': 'server error', status = status.HTTP_500_INTERNAL_SERVER_ERROR)