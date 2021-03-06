from django.shortcuts import render
from users.serializers import *
from rest_framework.generics import*
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets,status
from rest_framework.views import *
# Create your views here.

# class CreateUsersView(CreateAPIView):
#     queryset = UserDetails.objects.all()
#     serializer_class = UsersSerializer

class CustomObtainAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        response=super(CustomObtainAuthToken,self).post(request,*args,**kwargs)
        print('response.data::::',response.data)
        token=Token.objects.get(key=response.data['token'])
        user=User.objects.get(id=token.user_id)
        serializer=UserLoginSerializer(user,many=True)
        user_details = UserDetails.objects.filter(user_id=user.id)
        contact_no = [data.contact_no for data in user_details]

        if user:
            user_group = user.groups.all()
            for item in user_group:
                user_group = item.name
            if user_group:
                user_group_name = user_group
            else:
                user_group_name = ""
            #perm_tuple = [{'id': x.id, 'name': x.name} for x in Permission.objects.filter(user=user)]
            #print('user_group',type(user_group))
            data_dict = {
                'token': token.key,
                'user_id': user.pk,
                'username':user.username,
                'email': user.email,
                'group': user_group_name,
                'contact_no':contact_no[0] if contact_no else ''
            }
            if user.is_staff:
                data_dict['user_role']="staff"
            if user.is_superuser:
                data_dict['user_role'] = "admin"


            return Response(data_dict)
        else:
            return Response({'message':'Invalid Login','status':status.HTTP_400_BAD_REQUEST})



class EditStepTowOwnerDetailsView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = EditStepTowOwnerDetailsSerializer


class UserDetailsAndAppMasterDetailsView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UsersAppDetailsSerializer

class UserListByFranchiseIDView(ListAPIView):
    serializer_class = UserListByFranchiseIDSerializer
    def get_queryset(self):
        franchise_id = self.kwargs['franchise_id']
        #print('franchise_id::',franchise_id)
        if franchise_id:
            queryset = UserDetails.objects.filter(franchise_id=franchise_id)
            return queryset

class UserActiveView(RetrieveUpdateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserActiveSerializer


