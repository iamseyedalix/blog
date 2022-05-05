from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import UserProfile
from djoser import utils


# Create your views here.
@api_view(['POST', 'PUT'])
def UserManager(request):
    if request.method == 'POST':
        try:
            body = request.data
            username = str(body['username'])
            password = body['password']
            first_name = None
            last_name = None
            age = None
            if 'first_name' in body: first_name = body['first_name']
            if 'last_name' in body: last_name = body['last_name']
            if 'age' in body: age = int(body['age'])

            if User.objects.filter(username=username).exists():
                return Response({"error": "This username is validate!!!"}, status=status.HTTP_400_BAD_REQUEST)

            #create user
            this_user = User()
            this_user.username = username
            this_user.set_password(password)
            if 'email' in body: this_user.email = body['email']

            this_user.save()

            #create user profile
            this_profile = UserProfile(user=this_user, first_name=first_name, last_name=last_name, age=age)
            this_profile.save()

            #login to acc (TOKEN)
            token = utils.login_user(request, this_user)

            return Response({
                "user_info": {
                    "id": this_profile.id,
                    "username": this_profile.user.username,
                    "first_name": this_profile.first_name,
                    "last_name": this_profile.last_name,
                    "age": this_profile.age,
                    "email": this_profile.user.email
                },
                "token": token.key
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"Error": e})

    elif request.method == 'PUT':
        try:
            body = request.data
            this_user = request.user
            user_profile = UserProfile.objects.get(user=this_user)
            user_profile.first_name = body.get('first_name', user_profile.first_name)
            user_profile.last_name = body.get('last_name', user_profile.last_name)
            user_profile.age = body.get('age', user_profile.age)
            user_profile.save()
            return Response({
                "id": user_profile.id,
                "username": user_profile.user.username,
                "first_name": user_profile.first_name,
                "last_name": user_profile.last_name,
                "age": user_profile.age,
                "email": user_profile.user.email
            },status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
