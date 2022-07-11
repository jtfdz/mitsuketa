from django.shortcuts import render, redirect
from .forms import SubmissionForm
from django.contrib import messages
# Create your views here.

def send_submissions(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubmissionForm(request.POST)
        # print(request.POST.get('name_of_the_element'))
        # check whether it's valid:
        print(request.POST)
        if form.is_valid():
            form.save()
            # selected = form.cleaned_data.get("problem")
            # process the data in form.cleaned_data as required
            # ...
            messages.success(request, f'submission accepted!')
            # redirect to a new URL:
            return redirect('send_submissions')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SubmissionForm()

    return render(request, 'app_submissions/send_submissions.html', {'form': form})
