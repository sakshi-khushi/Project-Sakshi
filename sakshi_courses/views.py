from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from.models import *
from .serializers import*

class sakshi_lmsSignupUser(APIView):
    def post(self,request):
        userdata=sakshi_lmsSignupSerializers(data=request.data)
        if userdata.is_valid():
            sakshi_lmsUser.objects.create(**userdata.data)#dictionary
            message = {"message":"User created Successfully"}
            return JsonResponse(message,status=status.HTTP_201_CREATED)
        return JsonResponse(userdata.errors,status=status.HTTP_400_BAD_REQUEST) 

class sakshi_lmsGetUserDetails(APIView):
    def get(self,request):
        result = list(sakshi_lmsUser.objects.filter().values())
        return JsonResponse(result,status=status.HTTP_200_OK,safe=False)

class sakshi_lmsUpdateEmail(APIView):
    def put(self,request):
        userdata=sakshi_lmsUpdateEmailSerializers(data=request.data)
        if userdata.is_valid():
            email=userdata.data["email"]
            number=userdata.data["number"]
            sakshi_lmsUser.objects.filter(number=number).update(email=email)
            message={"message":"email updated succefully"}
            return JsonResponse(message,status=status.HTTP_200_OK)
        return JsonResponse(userdata.errors,status=status.HTTP_400_BAD_REQUEST)
       
class sakshi_lmsDeleteUser(APIView):
    def delete(self,request,number):
        sakshi_lmsUser .objects.filter(number=number).delete()
        message={"message": "user deleted successfully"}
        return JsonResponse(message,status=status.HTTP_204_NO_CONTENT)
# Create your views here.
