from django.shortcuts import render, get_object_or_404, redirect
from .models import CriminalCase, CrimeSubcategory
from .forms import CriminalCaseForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q


@login_required
def load_subcategories(request):
    crime_type_id = request.GET.get('crime_type')
    subcategories = CrimeSubcategory.objects.filter(crime_type_id=crime_type_id).order_by('name')
    return JsonResponse(list(subcategories.values('id', 'name')), safe=False)

# Create a new criminal case
@login_required
def case_create(request):
    if request.method == 'POST':
        form = CriminalCaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('case_list')
    else:
        form = CriminalCaseForm()
    return render(request, 'case_form.html', {'form': form})

# List all cases
@login_required
def case_list(request):
    cases = CriminalCase.objects.all()
    return render(request, 'case_list.html', {'cases': cases})

# Update an existing case
@login_required
def case_update(request, pk):
    criminal_case = get_object_or_404(CriminalCase, pk=pk)
    if request.method == 'POST':
        form = CriminalCaseForm(request.POST, request.FILES, instance=criminal_case)
        if form.is_valid():
            form.save()
            return redirect('case_list')
    else:
        form = CriminalCaseForm(instance=criminal_case)
    return render(request, 'case_form.html', {'form': form})

# Delete a case
@login_required
def case_delete(request, pk):
    criminal_case = get_object_or_404(CriminalCase, pk=pk)
    if request.method == 'POST':
        criminal_case.delete()
        return redirect('case_list')
    return render(request, 'case_delete.html', {'case': criminal_case})


@login_required
def open_cases_list(request):
    cases = CriminalCase.objects.filter(Q(case_status='active') | Q(case_status='in_progress'))
    return render(request, 'case_filter.html', {'cases': cases, 'title': 'Open Cases'})


@login_required
def closed_cases_list(request):
    cases = CriminalCase.objects.filter(case_status='closed')
    return render(request, 'case_filter.html', {'cases': cases, 'title': 'Closed Cases'})