from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import Doctor, Patient  # Asegúrate de importar los modelos correctos

# Vistas

def About(request):
    return render(request, 'about.html')

def Home(request):
    return render(request, 'home.html')

def Contact(request):
    return render(request, 'contact.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request, 'index.html')

def Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('index')  # Redirigir a la página principal después de iniciar sesión
        else:
            error = "Invalid credentials. Please try again."

    return render(request, 'login.html', {'error': error})

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors = Doctor.objects.all()
    return render(request, 'view_doctor.html', {'doctors': doctors})

def Delete_Doctor(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    try:
        doctor = Doctor.objects.get(id=pid)
        doctor.delete()
    except Doctor.DoesNotExist:
        pass
    return redirect('view_doctor')

from django.shortcuts import render, redirect
from .models import Doctor,Patient



def Add_Doctor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        specialty = request.POST.get('special')
        email = request.POST.get('email')
        address = request.POST.get('address')
        
        # Aquí puedes guardar la información en la base de datos
        # Suponiendo que tienes un modelo Doctor:
        from .models import Doctor
        try:
            Doctor.objects.create(name=name, mobile=mobile, specialty=specialty, email=email, address=address)
            return render(request, 'add_doctor.html', {'error': 'No'})
        except Exception as e:
            return render(request, 'add_doctor.html', {'error': 'Yes'})
    return render(request, 'add_doctor.html')

def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    patients = Patient.objects.all()
    return render(request, 'view_patient.html', {'patients': patients})

def Delete_Patient(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    try:
        patient = Patient.objects.get(id=pid)
        patient.delete()
    except Patient.DoesNotExist:
        pass
    return redirect('view_patient')

def Add_Patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    
    if request.method == "POST":
        try:
            n = request.POST['name']
            g = request.POST['gender']
            m = request.POST['mobile']
            a = request.POST['address']
    
            Patient.objects.create(name=n, gender=g, mobile=m, address=a)
            return redirect('view_patient')  # Redirigir a la vista de pacientes después de agregar uno nuevo
        except KeyError:
            error = 'Error occurred while adding patient.'
    
    return render(request, 'add_patient.html', {'error': error})

# Eliminé la parte relacionada con Appointment

def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    
    # Asegúrate de ajustar la lógica para la vista de citas si es necesario
    
    return render(request, 'view_appointment.html')

# Eliminé la parte relacionada con Appointment
