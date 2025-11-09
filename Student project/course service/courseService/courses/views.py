from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Student, StudentCourse
from .serializers import CourseSerializer, StudentSerializer, StudentCourseSerializer

# --- COURSE CRUD ---

@api_view(['GET'])
def get_courses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_course(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_course(request, id):
    try:
        course = Course.objects.get(id=id)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CourseSerializer(course, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_course(request, id):
    try:
        course = Course.objects.get(id=id)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)
    course.delete()
    return Response({'message': 'Course deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# --- SEARCH ---

@api_view(['GET'])
def search_course(request):
    name = request.GET.get('name', '')
    instructor = request.GET.get('instructor', '')
    category = request.GET.get('category', '')
    courses = Course.objects.filter(name__icontains=name, instructor__icontains=instructor, category__icontains=category)
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


# --- STUDENT ENROLLMENT ---

@api_view(['POST'])
def enroll_student(request):
    serializer = StudentCourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_course_students(request, id):
    students = StudentCourse.objects.filter(course_id=id)
    serializer = StudentCourseSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_student_courses(request, id):
    courses = StudentCourse.objects.filter(student_id=id)
    serializer = StudentCourseSerializer(courses, many=True)
    return Response(serializer.data)
