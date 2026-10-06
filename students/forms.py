from django import forms
from .models import Enrollment


class EnrollmentForm(forms.ModelForm):

    class Meta:
        model = Enrollment
        fields = [
            'student',
            'course',
            'enrollment_date',
            'reason'
        ]

        widgets = {
            'enrollment_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'reason': forms.Textarea(
                attrs={
                    'rows': 4,
                    'placeholder': 'Enter your reason'
                }
            ),
        }

    def clean_reason(self):
        reason = self.cleaned_data['reason']

        if len(reason) < 10:
            raise forms.ValidationError(
                'Reason must contain at least 10 characters.'
            )

        return reason