
# Create your views here.
from django.shortcuts import get_object_or_404, render, redirect
from .forms import StudentForm
from .models import Student


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to student list page
    else:
        form = StudentForm()

    return render(request, 'crudapp/student_create.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'crudapp/student_list.html', {'students': students})

def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'crudapp/student_update.html', {'form': form, 'student': student})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')