from django import forms

class CreatePageForm(forms.Form):
	title = forms.CharField()
	Textarea = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 30}))


class EditPageForm(forms.Form):
	Textarea = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 30}))
