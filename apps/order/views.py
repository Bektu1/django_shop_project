from rest_framework import viewsets, permissions
from .models import Order 
from .serializers import OrderSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user.pk)
    
    @action(methods=['GET'], detail=True)
    def confirm(self, request, pk):
        order = self.get_object()
        order.status = 'in_process'
        order.save()
        return Response({'message': 'Заказ в процессе обработки'}, status=200)
    
    
    def get_permissions(self):
        if self.action == 'confirm':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()
    

    

