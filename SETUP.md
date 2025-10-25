# Loan Application Webform Setup

## Overview
A simple Django webform has been created that allows users to submit loan applications with the following fields:
- **Income**: Annual income (decimal)
- **Credit Score**: Credit score between 300-850
- **Loan Amount**: Requested loan amount (decimal)
- **Years Employed**: Years of employment (integer)
- **Points**: Loyalty/bonus points (integer)

## Features

### Form Validation
- All fields are required
- Income and Loan Amount support decimal values
- Credit Score is validated between 300-850
- Years Employed and Points must be non-negative integers
- Bootstrap styling for professional appearance

### API Integration
The form attempts to submit data to a REST API endpoint:
- **Default API URL**: `http://localhost:8000/api/loan-application/`
- **Method**: POST
- **Timeout**: 5 seconds

### Error Handling
The application gracefully handles various error scenarios:
- **Connection Error**: "Unable to connect to the loan processing service"
- **Timeout Error**: "The loan processing service is taking too long to respond"
- **HTTP Error**: Displays the HTTP status code
- **General Error**: Displays the error message

### Success Response
Upon successful API submission, users are redirected to a success page displaying:
- Success confirmation message
- API response data in a formatted table
- Option to submit another application

## Project Structure

```
loan_app/
├── loan_app/                          # Main project directory
│   ├── settings.py                    # Django settings (includes 'loans' app)
│   ├── urls.py                        # Main URL configuration
│   ├── wsgi.py
│   ├── asgi.py
│   └── __init__.py
├── loans/                             # Loan application app
│   ├── templates/
│   │   └── loans/
│   │       ├── loan_application.html  # Main form template
│   │       └── success.html           # Success page template
│   ├── forms.py                       # Django form definition
│   ├── views.py                       # View logic with API integration
│   ├── urls.py                        # App URL configuration
│   ├── models.py
│   ├── admin.py
│   ├── apps.py
│   ├── tests.py
│   └── __init__.py
├── manage.py                          # Django management script
├── pixi.toml                          # Pixi environment configuration
└── db.sqlite3                         # SQLite database
```

## Installation & Running

### Prerequisites
- Python 3.14+
- Pixi package manager

### Setup Steps

1. **Install dependencies**:
   ```bash
   pixi install
   ```

2. **Run Django development server**:
   ```bash
   cd loan_app
   pixi run python manage.py runserver 0.0.0.0:8000
   ```

3. **Access the application**:
   - Open browser and navigate to: `http://localhost:8000/`

### Verify Installation
```bash
cd loan_app
pixi run python manage.py check
```

## Files Created/Modified

### New Files
- `loan_app/loans/forms.py` - Django form with all required fields
- `loan_app/loans/views.py` - View logic with API integration and error handling
- `loan_app/loans/urls.py` - URL routing for the loans app
- `loan_app/loans/templates/loans/loan_application.html` - Main form template
- `loan_app/loans/templates/loans/success.html` - Success page template

### Modified Files
- `loan_app/loan_app/settings.py` - Added 'loans' to INSTALLED_APPS
- `loan_app/loan_app/urls.py` - Added loans app URL include
- `pixi.toml` - Added 'requests' library dependency

## API Integration Details

### Request Format
```json
{
  "income": 50000.00,
  "credit_score": 750,
  "loan_amount": 25000.00,
  "years_employed": 5,
  "points": 100
}
```

### Customizing API Endpoint
To change the API endpoint, edit `loan_app/loans/views.py`:
```python
api_url = 'http://your-api-endpoint.com/api/loan-application/'
```

## Testing the Form

### Manual Testing
1. Navigate to `http://localhost:8000/`
2. Fill in all form fields with valid data
3. Click "Submit Application"
4. If API is unavailable, an error message will be displayed
5. If API is available, success page will show the response

### Form Validation Testing
- Try submitting with empty fields (validation error)
- Try credit score outside 300-850 range (validation error)
- Try negative values for Years Employed or Points (validation error)

## Styling
- **Framework**: Bootstrap 5.3.0 (CDN)
- **Color Scheme**: Purple gradient (667eea to 764ba2)
- **Responsive**: Mobile-friendly design
- **Features**: Smooth transitions, hover effects, error highlighting

## Dependencies
- Django >= 5.2.7
- Python >= 3.14.0
- requests >= 2.31.0

## Notes
- The application uses Django's CSRF protection
- Form data is validated on both client and server side
- All form fields use appropriate HTML5 input types
- Error messages are user-friendly and informative

