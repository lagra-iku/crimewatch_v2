from django.shortcuts import render, get_object_or_404, redirect
from .models import CriminalRecord, CriminalCase
from .forms import CriminalForm
from django.contrib.auth.decorators import login_required
from crimewatch.views import home


@login_required
def criminal_create(request):
    if request.method == 'POST':
        # Print request.POST data
        print(request.POST)
        print(request.FILES)

        form = CriminalForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid")
            # Additional debug prints
            print("Cleaned Data:", form.cleaned_data)
            try:
                criminal_record = form.save()
                print("Criminal Record saved:", criminal_record)
                return redirect('criminal_list')
            except Exception as e:
                print("Error while saving:", e)
        else:
            print("Form errors:", form.errors)
    else:
        form = CriminalForm()
        print("Form not valid")

    return render(request, 'criminal_form.html', {'form': form})


# Read (list) criminals
@login_required
def criminal_list(request):
    criminals = CriminalRecord.objects.all()
    return render(request, 'criminal_list.html', {'criminals': criminals})


# Update a criminal
@login_required
def criminal_update(request, pk):
    criminal = get_object_or_404(CriminalRecord, pk=pk)
    if request.method == 'POST':
        form = CriminalForm(request.POST, request.FILES, instance=criminal)
        if form.is_valid():
            form.save()
            return redirect('criminal_list')
    else:
        form = CriminalForm(instance=criminal)
    return render(request, 'criminal_form.html', {'form': form})

@login_required
def criminal_detail(request, pk):
    criminal = get_object_or_404(CriminalRecord, id=pk)
    return render(request, 'criminal_detail.html', {'criminal': criminal})


# Delete a criminal
@login_required
def criminal_delete(request, pk):
    criminal = get_object_or_404(CriminalRecord, pk=pk)
    if request.method == 'POST':
        criminal.delete()
        return redirect('criminal_list')
    return render(request, 'criminal_delete.html', {'criminal': criminal})


@login_required
def male_criminals_list(request):
    criminals = CriminalRecord.objects.filter(gender='male')
    return render(request, 'criminal_filter.html', {'criminals': criminals, 'title': 'Male Criminals'})


@login_required
def female_criminals_list(request):
    criminals = CriminalRecord.objects.filter(gender='female')
    return render(request, 'criminal_filter.html', {'criminals': criminals, 'title': 'Female Criminals'})
