from rest_framework import serializers
from .models import Company, JobPost, JobPostSkillSet


class CompanySerializer(serializers.ModelSerializer):

   class Meta:
      model = Company
      fields = "__all__"


class JobPostSerializer(serializers.ModelSerializer):

   class Meta:
      model = JobPost
      fields = "__all__"


class JobPostSkillSetSerializer(serializers.ModelSerializer):

   class Meta:
      model = JobPostSkillSet
      fields = "__all__"