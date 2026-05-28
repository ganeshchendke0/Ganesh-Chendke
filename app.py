from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

app = Flask(__name__, static_folder='.', static_url_path='', template_folder='.')
CORS(app)

# Email configuration - Update these with your details
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"  # Use app-specific password for Gmail
RECIPIENT_EMAIL = "ganesh@example.com"  # Your email to receive messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-message', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        
        # Extract form data
        full_name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        phone = data.get('phone', '').strip()
        subject = data.get('subject', '').strip()
        message = data.get('message', '').strip()
        
        # Validation
        if not all([full_name, email, phone, subject, message]):
            return jsonify({'success': False, 'message': 'All fields are required'}), 400
        
        # Create email content
        email_body = f"""
        <html>
            <body style="font-family: Arial, sans-serif;">
                <h2>New Contact Form Submission</h2>
                <p><strong>Name:</strong> {full_name}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Phone:</strong> {phone}</p>
                <p><strong>Subject:</strong> {subject}</p>
                <p><strong>Message:</strong></p>
                <p>{message.replace(chr(10), '<br>')}</p>
                <hr>
                <p><small>Submitted on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</small></p>
            </body>
        </html>
        """
        
        # Send email
        try:
            msg = MIMEMultipart()
            msg['From'] = SENDER_EMAIL
            msg['To'] = RECIPIENT_EMAIL
            msg['Subject'] = f"New Message: {subject}"
            
            msg.attach(MIMEText(email_body, 'html'))
            
            # Connect to Gmail SMTP
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            server.quit()
            
            return jsonify({
                'success': True, 
                'message': 'Your message has been sent successfully!'
            }), 200
            
        except smtplib.SMTPException as e:
            print(f"SMTP Error: {e}")
            return jsonify({
                'success': False, 
                'message': 'Failed to send email. Please try again later.'
            }), 500
            
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({
            'success': False, 
            'message': f'An error occurred: {str(e)}'
        }), 500

@app.route('/contact-info', methods=['GET'])
def contact_info():
    """API endpoint to get contact information"""
    return jsonify({
        'email': RECIPIENT_EMAIL,
        'phone': '+91-XXXXXXXXXX'  # Update with your phone
    })

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000, use_reloader=False)
