from django import forms
from .models import Submission

RADIO_CHOICES = ((0, "submit page / manga"),
                 (1, "report a problem"))

class SubmissionForm(forms.Form):
    problem = forms.ChoiceField(choices = RADIO_CHOICES)
    manga_name = forms.CharField(label="manga's name", max_length=40, min_length=1)
    page_name = forms.CharField(label="page's name, no links!", max_length=100)
    comment = forms.CharField(label='anything to add?', max_length=400)

    def save(self):
        data = self.cleaned_data
        submission = Submission(problem=data['problem'], manga_name=data['manga_name'],
                                page_name=data['page_name'], comment=data['comment'])
        submission.save()
