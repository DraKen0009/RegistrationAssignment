from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # You can add logic here to handle sending email if you don't want to use signals
            return redirect('registration_success')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def registration_success(request):
    return render(request, "accounts/registration_success.html")
