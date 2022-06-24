from genericpath import exists
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .models import (
    JobPostSkillSet,
    JobType,
    JobPost,
    Company
)
from django.db.models.query_utils import Q
from .serializers import CompanySerializer, JobPostSerializer, JobPostSkillSetSerializer


class SkillView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        skills = self.request.query_params.getlist('skills', '')
        print("skills = ", end=""), print(skills)
        

        return Response(status=status.HTTP_200_OK)


class JobView(APIView):

    def post(self, request):
        job_type = int( request.data.get("job_type", None) )
        # job_type = request.data.get("job_type", None)
        company_name = request.data.get("company_name", None)

        job_type_list = JobType.objects.filter(id=job_type).count()

        # job_type이 테이블에 존재하지 않는 데이터일 때
        if job_type_list == 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # 회사 이름이 존재하지 않을 때
    

        return Response(status=status.HTTP_200_OK)

