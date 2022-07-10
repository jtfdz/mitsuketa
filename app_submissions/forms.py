from django import forms

class SubmissionForm(forms.Form):
    problem = forms.ChoiceField(choices = ((True, "report a problem"), (False, "submit a manga")) )
    manga_name = forms.CharField(label="manga's name", max_length=40, min_length=1)
    page_name = forms.CharField(label="page's name, no links!")
    comment = forms.CharField(label='anything to add?')
