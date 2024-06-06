from django.shortcuts import render, get_object_or_404, redirect
from .models import Officer
from .forms import OfficerForm
from django.contrib.auth.decorators import login_required

# Create a new officer
@login_required
def officer_create(request):
    if request.method == 'POST':
        form = OfficerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('officer_list')
    else:
        form = OfficerForm()
    return render(request, 'officer_form.html', {'form': form})

# List all officers
@login_required
def officer_list(request):
    officers = Officer.objects.all()
    return render(request, 'officer_list.html', {'officers': officers})

# Update an existing officer
@login_required
def officer_update(request, pk):
    officer = get_object_or_404(Officer, pk=pk)
    if request.method == 'POST':
        form = OfficerForm(request.POST, instance=officer)
        if form.is_valid():
            form.save()
            return redirect('officer_list')
    else:
        form = OfficerForm(instance=officer)
    return render(request, 'officer_form.html', {'form': form})

# Delete an officer
@login_required
def officer_delete(request, pk):
    officer = get_object_or_404(Officer, pk=pk)
    if request.method == 'POST':
        officer.delete()
        return redirect('officer_list')
    return render(request, 'officer_delete.html', {'officer': officer})