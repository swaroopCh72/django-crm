from django.shortcuts import render, redirect
from .forms import SignUpForm, AddRecordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Customer

# Create your views here.
def home(request):
    customers = Customer.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(
            request,
            username = username,
            password = password
        )
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('home')
    else:
        return render(request, 'home.html', {'customers': customers})
    
def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')   
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form':form})
    
    return render(request, 'signup.html', {'form':form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Customer.objects.get(id=pk)
        return render(request, 'customer_record.html', {'customer_record': customer_record})
    else:
        messages.error(request, 'You must be logged in to view this page.')
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Customer.objects.get(id=pk)
        customer_record.delete()
        messages.success(request, 'Record deleted successfully!')
        return redirect('home')
    else:
        messages.error(request, 'You must be logged in to perform this action.')
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save(commit=False)
                add_record.user = request.user
                add_record.save()
                messages.success(request, 'Record added successfully!')
                return redirect('home')
        else:
            return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to perform this action.')
        return redirect('home')
    

def update_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Customer.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=customer_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record updated successfully!')
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to perform this action.')
        return redirect('home')
    