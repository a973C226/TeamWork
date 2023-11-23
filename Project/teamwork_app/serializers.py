from rest_framework import serializers

from .models import Employee, Project


class ProjectSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'description',
            'employee',
            'creator',
        ]
