from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from ..models.quiz import *
from ..serializers.quiz import *
from ..filters import *

key=open('api\\project','r').read()


class QuizQuestionBankViewSet(viewsets.ModelViewSet):
    queryset = QuizQuestionBank.objects.all().order_by('?')
    serializer_class = QuizQuestionBankSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )

    @action(detail=False, methods=['GET'])
    def entertainment(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        myFilter = QuizQuestionBankFilter(request.GET,queryset=queryset)
        queryset=myFilter.qs[:6]

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # apply filter
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        myFilter = QuizQuestionBankFilter(request.GET,queryset=queryset)
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


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    # Return particular Quiz OR All quiz of requested user
    def list(self, request, *args, **kwargs):  
        try:      
            if len(request.query_params)==0:
                token=request.headers['authorization'][6:]
                userId = Token.objects.get(key=token).user.id
                queryset=Quiz.objects.filter(user=userId)
            elif len(request.query_params)==1:
                queryset = self.filter_queryset(self.get_queryset())
                myFilter = QuizFilter(request.GET,queryset=queryset)
                queryset=myFilter.qs
            else:
                response = {'message': 'You can\'t use GET method like this'}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except:
            response = {'message': 'Something went wrong'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

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


class QuizResponseViewSet(viewsets.ModelViewSet):
    queryset = QuizResponse.objects.all()
    serializer_class = QuizResponseSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )

    # apply filter
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        myFilter = QuizResponseFilter(request.GET,queryset=queryset)
        queryset=myFilter.qs

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

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