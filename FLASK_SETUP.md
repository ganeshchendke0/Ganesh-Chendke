# Portfolio Website - Flask Backend Setup

## Overview
This is a Python Flask backend for your portfolio website's contact form. It handles form submissions and sends emails.

## Prerequisites
- Python 3.7+ installed
- pip (Python package manager)

## Installation & Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Email Settings
Edit `app.py` and update these variables:
```python
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"  # Use app-specific password for Gmail
RECIPIENT_EMAIL = "ganesh@example.com"  # Where you want to receive messages
```

### For Gmail Users:
1. Enable 2-Factor Authentication on your Gmail account
2. Generate an App Password: https://myaccount.google.com/apppasswords
3. Use the generated password as `SENDER_PASSWORD`

### For Other Email Providers:
Update the SMTP settings in the `send_message()` function:
```python
server = smtplib.SMTP('your_smtp_server', 587)  # e.g., smtp.outlook.com
```

### 3. Run the Server
```bash
python app.py
```

The server will start on `http://localhost:5000`

### 4. Access Your Website
Open your browser and go to:
```
http://localhost:5000
```

## Features

- **Form Validation**: All fields are required
- **Email Notifications**: Receive emails when someone submits the contact form
- **Error Handling**: Displays user-friendly error messages
- **CORS Support**: Allows cross-origin requests
- **HTML Email**: Formatted email messages with submission details

## API Endpoints

### POST /send-message
Submits contact form data
- **Request Body**:
```json
{
  "name": "Full Name",
  "email": "user@example.com",
  "phone": "123-456-7890",
  "subject": "Message Subject",
  "message": "Your message"
}
```

- **Response (Success)**:
```json
{
  "success": true,
  "message": "Your message has been sent successfully!"
}
```

### GET /contact-info
Returns contact information
- **Response**:
```json
{
  "email": "ganesh@example.com",
  "phone": "+91-XXXXXXXXXX"
}
```

## Troubleshooting

### "Module not found" error
Make sure you've installed all dependencies:
```bash
pip install -r requirements.txt
```

### Email not sending
- Verify email and password are correct
- Check if 2FA is enabled (for Gmail)
- Ensure "Less secure app access" is disabled if using Gmail
- Check firewall/antivirus settings

### CORS errors
The backend already has CORS enabled. If issues persist, uncomment and modify the CORS settings in `app.py`.

## Development Mode
For development, the server runs with `debug=True`. This enables:
- Auto-reload on code changes
- Detailed error messages
- Interactive debugger

For production, change to `debug=False` and use a proper WSGI server like Gunicorn.

## File Structure
```
ganesh.html/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── index.html            # Frontend (updated with form handling)
├── style.css             # Styling
├── README.md             # This file
└── templates/
    └── index.html        # (optional - if using Flask templates)
```

## Next Steps

1. Install dependencies
2. Configure your email settings
3. Run the Flask server
4. Test the contact form on your website

Enjoy your new portfolio backend!
