from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response
from rest_framework.request import Request
from .serializers import BillSerializer, BillModel


# Create your views here.
class BillView(APIView):
    permission_classes = [IsAuthenticated]
    class_model = BillModel
    class_serializer = BillSerializer

    def get(self, request):
        bills = request.user.billmodel_set.all()
        serializer = self.class_serializer(bills, many=True)
        return Response(serializer.data)

    def post(self, request):
        request.data['user'] = request.user.id
        bill = self.class_serializer(data=request.data)
        if bill.is_valid():
            bill.save()
            return Response(bill.data, status=status.HTTP_201_CREATED)
        print(bill.errors, request.data)
        return Response(bill.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request):

        bills = self.class_model.objects.filter(id=int(request.data['id']))
        if len(bills) > 0:
            bills[0].delete()
            return Response(status=status.HTTP_302_FOUND)
        return Response(status=status.HTTP_404_NOT_FOUND)
