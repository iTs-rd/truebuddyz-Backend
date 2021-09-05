from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from ..models.other import *
from ..serializers.other import *
from ..filters import *

from ..add_data import add_data
add_data()
key=open('api\\project','r').read()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        user=User.objects.get(username=serializer.data['username'])
        token=Token.objects.get(user=user)
        response={str(token)}
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)

    # Return ID of user
    def list(self, request, *args, **kwargs):
        try:
            token=request.headers['authorization'][6:]
            userId = Token.objects.get(key=token).user.id
            return Response(userId, status=status.HTTP_200_OK)
        except:
            response = {'message': 'You can\'t use GET method like this'}
            return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

    def destroy(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use DELETE method like this'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use PUT method like this'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use GET method like this'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)


class RfQuestionBankViewSet(viewsets.ModelViewSet):
    queryset = RfQuestionBank.objects.all().order_by('?')
    serializer_class = RfQuestionBankSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )

    # apply filter
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        myFilter = RfQuestionBankFilter(request.GET,queryset=queryset)
        queryset=myFilter.qs

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # add key
    def create(self, request, *args, **kwargs):
        if key !=request.headers['encryption']: 
            response = {'message': 'You can\'t use POST method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # add key
    def retrieve(self, request, *args, **kwargs):
        if key !=request.headers['encryption']: 
            response = {'message': 'You can\'t use GET method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # add key
    def update(self, request, *args, **kwargs):
        if key !=request.headers['encryption']: 
            response = {'message': 'You can\'t use PUT method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    # add key
    def destroy(self, request, *args, **kwargs):
        if key !=request.headers['encryption']: 
            response = {'message': 'You can\'t use DELETE method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )

    # record is already created (in serializers.py)
    # only record is updated, not use PUT method because in URL we need to pass index of record
    def create(self, request, *args, **kwargs):
        try:
            token=request.headers['authorization'][6:]
            userId = Token.objects.get(key=token).user.id
            rating=request.data['value']
            if int(rating) < 1 or 5 < int(rating):
                response = {'message': 'Wrong Rating'}
                return Response(response, status=status.HTTP_403_FORBIDDEN)
            Rating.objects.filter(user=userId).update(value=rating)
            response = {'message': 'Ok'}
            return Response(response, status=status.HTTP_200_OK)
        except:
            response = {'message': 'Something went wrong'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    # add key
    def retrieve(self, request, *args, **kwargs):
        if key !=request.headers['encryption']: 
            response = {'message': 'You can\'t use GET method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # add key
    def update(self, request, *args, **kwargs):
        if key !=request.headers['encryption']: 
            response = {'message': 'You can\'t use PUT method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    # add key
    def destroy(self, request, *args, **kwargs):
        if key !=request.headers['encryption']: 
            response = {'message': 'You can\'t use DELETE method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # add key and apply filter
    def list(self, request, *args, **kwargs):
        if key !=request.headers['encryption']: 
            response = {'message': 'You can\'t use GET method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        queryset = self.filter_queryset(self.get_queryset())
        myFilter = RatingFilter(request.GET,queryset=queryset)
        queryset=myFilter.qs

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )

    # add key
    def retrieve(self, request, *args, **kwargs):
        if key !=request.headers['encryption']: 
            response = {'message': 'You can\'t use GET method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # add key
    def update(self, request, *args, **kwargs):
        if key !=request.headers['encryption']: 
            response = {'message': 'You can\'t use PUT method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    # add key
    def destroy(self, request, *args, **kwargs):
        if key !=request.headers['encryption']: 
            response = {'message': 'You can\'t use DELETE method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # add key and apply filter
    def list(self, request, *args, **kwargs):
        if key !=request.headers['encryption']: 
            response = {'message': 'You can\'t use GET method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class ContributionViewSet(viewsets.ModelViewSet):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )

    # add key
    def retrieve(self, request, *args, **kwargs):
        if key !=request.headers['encryption']: 
            response = {'message': 'You can\'t use GET method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # add key
    def update(self, request, *args, **kwargs):
        if key !=request.headers['encryption']: 
            response = {'message': 'You can\'t use PUT method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    # add key
    def destroy(self, request, *args, **kwargs):
        if key !=request.headers['encryption']: 
            response = {'message': 'You can\'t use DELETE method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # add key and apply filter
    def list(self, request, *args, **kwargs):
        if key !=request.headers['encryption']: 
            response = {'message': 'You can\'t use GET method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class TrendingViewSet(viewsets.ModelViewSet):
    queryset = Trending.objects.all().filter(is_active=True).order_by('rank')
    serializer_class = TrendingSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )

    # apply filter
    def list(self, request, *args, **kwargs):
        # queryset = Trending.objects.get(is_active=True)
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


        # queryset = self.filter_queryset(self.get_queryset())
        # myFilter = TrendingFilter(request.GET,queryset=queryset)
        # queryset=myFilter.qs

        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        # serializer = self.get_serializer(queryset, many=True)
        # return Response(serializer.data)

    # add key
    def create(self, request, *args, **kwargs):
        if key !=request.headers['encryption']: 
            response = {'message': 'You can\'t use POST method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # add key
    def retrieve(self, request, *args, **kwargs):
        if key !=request.headers['encryption']: 
            response = {'message': 'You can\'t use GET method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # add key
    def update(self, request, *args, **kwargs):
        if key !=request.headers['encryption']: 
            response = {'message': 'You can\'t use PUT method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    # add key
    def destroy(self, request, *args, **kwargs):
        if key !=request.headers['encryption']: 
            response = {'message': 'You can\'t use DELETE method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
