# from functools import partial
from unicodedata import category
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

# from crowdfunding.projects.permissions import IsOwnerOrReadOnly
from .models import Project, Pledge, PledgeType, Category
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer, PledgeTypeSerializer, CategorySerializer
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly
# from crowdfunding.projects import serializers
# from crowdfunding.projects import serializers


class CategoryList(APIView):
    def get (self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class PledgeTypeList(APIView):
    def get (self, request):
        pledge_type = PledgeType.objects.all()
        serializer = PledgeTypeSerializer(pledge_type, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PledgeTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class PledgeList(APIView):

    def get (self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )




class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        projects = Project.objects.all()
        
        projects = projects.filter(is_open=True)
       
        projects = projects.filter(is_archived=False)
        order_by = request.query_params.get('order_by', None)
        if order_by:
            projects = projects.order_by(order_by)
        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(projects, request)
        serializer = ProjectSerializer(result_page, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class LatestProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        projects = Project.objects.all()
        
        
    
        projects = projects.filter(is_open=True)
       
        
        projects = projects.filter(is_archived=False)
        
        projects = projects.order_by('-date_created')[:3]
        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(projects, request)
        serializer = ProjectSerializer(result_page, many=True)
        return Response(serializer.data)

class ProjectDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404 

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        data = request.data
        serializer = ProjectDetailSerializer(
            instance=project,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)


class MyProjectList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        projects = Project.objects.all().filter(owner=self.request.user.id)
        
        is_archived = request.query_params.get('is_archived', None)
        if is_archived:
            projects = projects.filter(is_archived=is_archived)
        order_by = request.query_params.get('order_by', None)
        if order_by:
            projects = projects.order_by(order_by)
        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(projects, request)
        serializer = ProjectSerializer(result_page, many=True)
        return Response(serializer.data)

class MyPledgeList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get (self, request):
        pledges = Pledge.objects.all().filter(supporter=self.request.user.id)
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)

