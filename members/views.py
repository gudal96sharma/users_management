from django.shortcuts import render
from rest_framework.views import APIView,Response,status
from .serializers import *
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

# Create your views here.
class Registration(APIView):
    def post(self,request):
        result = {}
        result['status'] =  'NOK'
        result['valid']  =  False
        result['result'] = {"message":"Unauthorized access","data" :{}}
        serializer       = UserSerializer(data = request.data)
        if serializer.is_valid():
            username = serializer.validated_data['email']
            password = (''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8)))
            serializer.validated_data['password'] = password
            serializer.save()
            name = request.data['name']
            msg_plain = ''
            msg_html = render_to_string(
                'users/create_user.html', {'name': name, 'username': username, 'password': password})
            send_mail('Dashboard', msg_plain,
                        settings.EMAIL_HOST_USER, [username], html_message=msg_html,)                   
                     
            result['status']    =   "OK"
            result['valid']     =   True
            result['result']['message'] =   "User registered successfully"
            result['result']['data'] = serializer.data
            return Response(result,status=status.HTTP_200_OK)

        else:
            result['result']['message'] = (list(serializer.errors.keys())[
                0]+' - '+list(serializer.errors.values())[0][0]).capitalize()
            return Response(result, status=status.HTTP_422_UNPROCESSABLE_ENTITY)