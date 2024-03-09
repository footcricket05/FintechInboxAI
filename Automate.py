import imaplib
import email
from email.header import decode_header
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

# Load your dataset
data = pd.read_csv("data.csv")  # Adjust path as needed

# Function to classify email content
def classify_email(content):
    # Perform feature extraction
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(data['Email_Content'])
    y = data['Category']
    
    # Train classifier
    clf = MultinomialNB(alpha=0.1)  # Adjust alpha parameter to prevent overfitting
    clf.fit(X, y)
    
    # Predict category for the entered content
    X_new = vectorizer.transform([content])
    predicted_category = clf.predict(X_new)
    
    return predicted_category[0]

# Function to decode email subject
def decode_subject(subject):
    decoded_subject = ''
    for part, encoding in decode_header(subject):
        if isinstance(part, bytes):
            decoded_subject += part.decode(encoding or 'utf-8')
        else:
            decoded_subject += part
    return decoded_subject

# Function to process incoming emails
def process_emails(username, password, imap_server):
    # Connect to the IMAP server
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(username, password)
    mail.select("inbox")  # Select the inbox folder

    # Search for unread emails
    result, data = mail.search(None, "UNSEEN")
    if result == "OK":
        for num in data[0].split():
            # Fetch the email
            result, email_data = mail.fetch(num, "(RFC822)")
            if result == "OK":
                raw_email = email_data[0][1]
                msg = email.message_from_bytes(raw_email)
                
                # Extract email content
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            email_content = part.get_payload(decode=True).decode()
                            break
                else:
                    email_content = msg.get_payload(decode=True).decode()
                
                # Classify email content
                category = classify_email(email_content)
                
                # Decode email subject
                subject = decode_subject(msg["Subject"])
                
                print(f"Subject: {subject}")
                print(f"Category: {category}")
                
                # Mark the email as read
                mail.store(num, "+FLAGS", "\\Seen")

    # Close the connection
    mail.close()
    mail.logout()

# Set your email credentials and IMAP server address
username = "email address"
password = "email password"
imap_server = "imap.gmail.com"

# Process incoming emails
process_emails(username, password, imap_server)
