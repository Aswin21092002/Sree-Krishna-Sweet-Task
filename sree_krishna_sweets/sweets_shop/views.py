from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ComplaintForm
from .models import Complaint, Shop

def submit_complaint(request):
    # Get the shop object
    shop = get_object_or_404(Shop, name='Sree Krishna Sweets')  # Fetch the shop with the common name

    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.shop = shop  # Set the common shop name
            complaint.save()
            
            # Send email to admin
            send_mail(
                'New Complaint',
                f'Complaint in {shop.zone.name}, {shop.location}:\n\n{form.cleaned_data["description"]}',
                'your-email@example.com',
                ['admin@example.com'],
                fail_silently=False,
            )
            
            # Show success message
            messages.success(request, 'Complaint submitted successfully!')
            return redirect('complaint_status', complaint_id=complaint.id)
    else:
        form = ComplaintForm()

    return render(request, 'complaint_form.html', {'form': form})

def complaint_status(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    return render(request, 'complaint_status.html', {'complaint': complaint})

def resolve_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    complaint.is_resolved = True
    complaint.save()
    
    # Notify shop of resolution
    send_mail(
        'Complaint Resolved',
        f'Your complaint for Sree Krishna Sweets has been resolved.',
        'your-email@example.com',
        [complaint.shop.phone_number + '@sms-gateway.com'],  # Assume SMS via email gateway
        fail_silently=False,
    )
    
    messages.success(request, 'Complaint resolved successfully!')
    return redirect('complaint_status', complaint_id=complaint.id)
