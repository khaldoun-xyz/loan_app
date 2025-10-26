import requests
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .forms import LoanApplicationForm


@require_http_methods(["GET", "POST"])
def loan_application(request):
    """
    Handle loan application form submission.
    Submits data to REST API if available, otherwise shows success message.
    """
    if request.method == "POST":
        form = LoanApplicationForm(request.POST)
        if form.is_valid():
            data = {
                "income": float(form.cleaned_data["income"]),
                "credit_score": form.cleaned_data["credit_score"],
                "loan_amount": float(form.cleaned_data["loan_amount"]),
                "years_employed": form.cleaned_data["years_employed"],
                "points": form.cleaned_data["points"],
            }

            api_url = "http://loan_api:8000/predict"
            headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }
            try:
                response = requests.post(api_url, json=data, headers=headers, timeout=5)
                response.raise_for_status()

                api_response = response.json()

                if isinstance(api_response, dict) and "approve" in api_response:
                    if api_response["approve"]:
                        result = {
                            "message": "Congratulations, your application was approved."
                        }
                    else:
                        result = {"message": "Unfortunately, your request was denied."}
                else:
                    result = api_response

                return render(
                    request, "loans/success.html", {"result": result, "form": form}
                )

            except requests.exceptions.RequestException:
                result = {
                    "message": "Thank you. A loan expert will review your application and get back to you shortly."
                }
                return render(
                    request, "loans/success.html", {"result": result, "form": form}
                )
    else:
        form = LoanApplicationForm()

    return render(request, "loans/loan_application.html", {"form": form})
