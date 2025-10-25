from django import forms


class LoanApplicationForm(forms.Form):
    """Form for loan application with income, credit score, loan amount, employment history, and points."""

    income = forms.DecimalField(
        label='Annual Income',
        max_digits=12,
        decimal_places=2,
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your annual income',
            'step': '0.01'
        })
    )

    credit_score = forms.IntegerField(
        label='Credit Score',
        min_value=300,
        max_value=850,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your credit score (300-850)',
            'type': 'number'
        })
    )

    loan_amount = forms.DecimalField(
        label='Loan Amount',
        max_digits=12,
        decimal_places=2,
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the loan amount you need',
            'step': '0.01'
        })
    )

    years_employed = forms.IntegerField(
        label='Years Employed',
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter years of employment',
            'type': 'number'
        })
    )

    points = forms.IntegerField(
        label='Points',
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your points',
            'type': 'number'
        })
    )

