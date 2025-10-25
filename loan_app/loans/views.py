import requests
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .forms import LoanApplicationForm


@require_http_methods(["GET", "POST"])
def loan_application(request):
    """
    Handle loan application form submission.
    Submits data to REST API if available, otherwise shows error message.
    """
    if request.method == 'POST':
        form = LoanApplicationForm(request.POST)
        if form.is_valid():
            # Prepare data for API submission
            data = {
                'income': float(form.cleaned_data['income']),
                'credit_score': form.cleaned_data['credit_score'],
                'loan_amount': float(form.cleaned_data['loan_amount']),
                'years_employed': form.cleaned_data['years_employed'],
                'points': form.cleaned_data['points'],
            }

            # Try to call the REST API
            api_url = 'http://localhost:8000/api/loan-application/'  # Update this URL as needed
            try:
                response = requests.post(
                    api_url,
                    json=data,
                    timeout=5
                )
                response.raise_for_status()

                # API call successful
                result = response.json()
                return render(request, 'loans/success.html', {
                    'result': result,
                    'form': form
                })

            except requests.exceptions.ConnectionError:
                error_message = 'Unable to connect to the loan processing service. Please try again later.'
                return render(request, 'loans/loan_application.html', {
                    'form': form,
                    'error': error_message
                })
            except requests.exceptions.Timeout:
                error_message = 'The loan processing service is taking too long to respond. Please try again later.'
                return render(request, 'loans/loan_application.html', {
                    'form': form,
                    'error': error_message
                })
            except requests.exceptions.HTTPError as e:
                error_message = f'Error from loan processing service: {e.response.status_code}. Please try again later.'
                return render(request, 'loans/loan_application.html', {
                    'form': form,
                    'error': error_message
                })
            except requests.exceptions.RequestException as e:
                error_message = f'An error occurred while processing your application: {str(e)}'
                return render(request, 'loans/loan_application.html', {
                    'form': form,
                    'error': error_message
                })
    else:
        form = LoanApplicationForm()

    return render(request, 'loans/loan_application.html', {'form': form})
