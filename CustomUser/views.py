from CustomUser.models import Users
from CustomUser.forms import UsersCreationForm
from rest_framework import status
from rest_framework.views import APIView, Response, Request


# Create your views here.


class CreateUserView(APIView):
    class_model = Users
    class_model_form = UsersCreationForm

    def post(self, request: Request):
        form = self.class_model_form(data=request.data)

        if not form.is_valid():
            print(f'form data: {form.cleaned_data}\n request data: {request.data}')
            return Response(status.HTTP_400_BAD_REQUEST)

        print(form.save(False))

        return Response(status.HTTP_201_CREATED)
