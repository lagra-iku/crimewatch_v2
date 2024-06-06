from django.shortcuts import render, redirect, get_object_or_404
from .forms import PoliceOfficersForm, AddNewOfficerForm, LoginForm, CaseForm
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
import bcrypt
from .models import AddNewOfficer, Case
from django.contrib import messages
from .forms import CriminalRecordForm


def app(request):
    return render(request, 'pages/dashboard.html')

def whistledown(request):
    return render(request, 'ladywhistledown.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                officer = AddNewOfficer.objects.get(username=username)
            except AddNewOfficer.DoesNotExist:
                messages.error(request, 'Invalid username or password.')
                return render(request, 'login.html', {'form': form})

            if bcrypt.checkpw(password.encode('utf-8'), officer.password.encode('utf-8')):
                # Authenticate the user
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('app')
                else:
                    messages.error(request, 'Invalid username or password.')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

def register_officers(request):
    if request.method == 'POST':
        form = AddNewOfficerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_officers')
    else:
        form = AddNewOfficerForm()
    return render(request, 'register_officers.html', {'form': form})


def add_new_officer(request):
    if request.method == 'POST':
        form = AddNewOfficerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard') 
    else:
        form = AddNewOfficerForm()
    return render(request, 'add_new_officer.html', {'form': form})

def case_list(request):
    cases = Case.objects.all()
    return render(request, 'cases/case_list.html', {'cases': cases})

def case_detail(request, pk):
    case = get_object_or_404(Case, pk=pk)
    return render(request, 'cases/case_detail.html', {'case': case})

def case_new(request):
    if request.method == "POST":
        form = CaseForm(request.POST, request.FILES)
        if form.is_valid():
            case = form.save()
            return redirect('/admin', pk=case.pk)
    else:
        form = CaseForm()
    return render(request, 'cases/case_edit.html', {'form': form})

def case_edit(request, pk):
    case = get_object_or_404(Case, pk=pk)
    if request.method == "POST":
        form = CaseForm(request.POST, request.FILES, instance=case)
        if form.is_valid():
            case = form.save()
            return redirect('case_detail', pk=case.pk)
    else:
        form = CaseForm(instance=case)
    return render(request, 'cases/case_edit.html', {'form': form})

def create_criminal_record(request):
    if request.method == 'POST':
        form = CriminalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CriminalRecordForm()
    return render(request, 'create_criminal_record.html', {'form': form})

