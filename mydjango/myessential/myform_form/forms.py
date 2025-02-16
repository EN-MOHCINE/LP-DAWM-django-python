from django import forms

JOBS = (
    ('Python', 'Python Developer'),
    ('JavaScript', 'JavaScript Developer'),
    ('Java', 'Java Developer')
)

CITIES = (
    ('Tanger', 'Capitale du nord'),
    ('Fes', 'Capitale culturelle'),
    ('Rabat', 'Capitale administrative'),
    ('Casablanca', 'Metropole economique')
)

LANGUAGES = (
    ('Ar', 'Arabic'),
    ('En', 'English'),
    ('sp', 'Spanish'),
    ('Fr', 'French')
)

class SignupForm(forms.Form):
    jobs = forms.ChoiceField(choices=JOBS)
    city = forms.MultipleChoiceField(choices=CITIES)
    language = forms.MultipleChoiceField(choices=LANGUAGES)
    cgu_accept = forms.BooleanField(initial=True)

class SignupFormWidget(forms.Form):
    pseudo = forms.CharField(max_length=8, required=False)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput)
    jobs = forms.ChoiceField(choices=JOBS, widget=forms.RadioSelect)
    city = forms.MultipleChoiceField(choices=CITIES, widget=forms.CheckboxSelectMultiple)
    language = forms.MultipleChoiceField(choices=LANGUAGES, widget=forms.SelectMultiple)
    cgu_accept = forms.BooleanField(initial=True)


class SignupFormData(forms.Form):
    pseudo = forms.CharField(max_length=8, required=False)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput)
    jobs = forms.ChoiceField(choices=JOBS, widget=forms.RadioSelect)
    language = forms.MultipleChoiceField(choices=LANGUAGES, 
                                         widget=forms.CheckboxSelectMultiple)
    cgu_accept = forms.BooleanField(initial=True)

    def clean_pseudo(self):
        pseudo = self.cleaned_data.get("pseudo")
        if '$' in pseudo:
            raise forms.ValidationError("Le pseudo ne doit pas contenir le $")
        return pseudo