# from flask import Flask, render_template, request, jsonify
# import imaplib
# import email
# from transformers import BartForConditionalGeneration, BartTokenizer, pipeline
# import torch

# app = Flask(__name__)

# model_name = 'facebook/bart-large-cnn'
# tokenizer = BartTokenizer.from_pretrained(model_name)
# model = BartForConditionalGeneration.from_pretrained(model_name)

# sentiment_analyzer = pipeline('sentiment-analysis', model='distilbert-base-uncased')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/summarize', methods=['POST'])
# def summarize_email():
#     email_id = request.form['email_id']
#     password = request.form['password']

#     mail = imaplib.IMAP4_SSL('imap.gmail.com')

#     try:
#         mail.login(email_id, password)
#     except imaplib.IMAP4.error:
#         return "Invalid email credentials"

#     mail.select('inbox')

#     summaries = []

#     from datetime import date
#     today = date.today()
#     today_date = today.strftime("%d-%b-%Y")  # Use the full year format (e.g., "25-Oct-2023")

#     status, email_ids = mail.search(None, 'SINCE', today_date)
#     email_ids = email_ids[0].split()

#     for email_id in email_ids:
#         status, msg_data = mail.fetch(email_id, '(RFC822)')
#         raw_email = msg_data[0][1]
#         msg = email.message_from_bytes(raw_email)
#         sender = msg['From']
#         subject = msg['Subject']
#         body = ""

#         if msg.is_multipart():
#             for part in msg.walk():
#                 if part.get_content_type() == "text/plain":
#                     body = part.get_payload(decode=True).decode()
#                     break
#         else:
#             body = msg.get_payload(decode=True).decode()

#         if body:
#             word_count = len(body.split())
#             if word_count < 10:
#                 summary = body
#             else:
#                 if word_count < 50:
#                     summary = generate_summary(body, max_length=20)
#                 else:
#                     summary = generate_summary(body, max_length=50)

#             sentiment_result = sentiment_analyzer(summary)
#             label = sentiment_result[0]['label']
#             score = sentiment_result[0]['score']

#             if score >= 0.7:
#                 email_label = "Important"
#             elif score >= 0.4:
#                 email_label = "Least Important"
#             else:
#                 email_label = "Not Important"

#             email_info = {
#                 'From': sender,
#                 'Email Subject': subject,
#                 'Generated Summary': summary,
#                 'Sentiment Label': email_label,
#                 'Sentiment Score': score
#             }
#             summaries.append(email_info)

#     mail.logout()

#     return jsonify(summaries)

# def generate_summary(email_text, max_length=20):
#     inputs = tokenizer([email_text], return_tensors='pt', max_length=1024, truncation=True)

#     with torch.no_grad():
#         try:
#             summary_ids = model.generate(**inputs, max_length=max_length)
#         except ValueError:
#             # Handle cases where min_length is greater than max_length
#             summary_ids = model.generate(**inputs, max_length=max_length, min_length=20)

#     summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
#     return summary

# if __name__ == '__main__':
#     app.run(debug=True)


















# from flask import Flask, render_template, request, jsonify
# import imaplib
# import email
# from transformers import BartForConditionalGeneration, BartTokenizer, pipeline
# import torch
# from flask_cors import CORS  # Import the CORS extension

# app = Flask(__name__)
# CORS(app)  # Configure CORS to allow requests from any origin

# model_name = 'facebook/bart-large-cnn'
# tokenizer = BartTokenizer.from_pretrained(model_name)
# model = BartForConditionalGeneration.from_pretrained(model_name)

# sentiment_analyzer = pipeline('sentiment-analysis', model='distilbert-base-uncased')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/summarize', methods=['POST'])
# def summarize_email():
#     email_id = request.form['email_id']
#     password = request.form['password']

#     mail = imaplib.IMAP4_SSL('imap.gmail.com')

#     try:
#         mail.login(email_id, password)
#     except imaplib.IMAP4.error:
#         return "Invalid email credentials"

#     mail.select('inbox')

#     summaries = []

#     from datetime import date
#     today = date.today()
#     today_date = today.strftime("%d-%b-%Y")  # Use the full year format (e.g., "25-Oct-2023")

#     status, email_ids = mail.search(None, 'SINCE', today_date)
#     email_ids = email_ids[0].split()

#     for email_id in email_ids:
#         status, msg_data = mail.fetch(email_id, '(RFC822)')
#         raw_email = msg_data[0][1]
#         msg = email.message_from_bytes(raw_email)
#         sender = msg['From']
#         subject = msg['Subject']
#         body = ""

#         if msg.is_multipart():
#             for part in msg.walk():
#                 if part.get_content_type() == "text/plain":
#                     body = part.get_payload(decode=True).decode()
#                     break
#         else:
#             body = msg.get_payload(decode=True).decode()

#         if body:
#             word_count = len(body.split())
#             if word_count < 10:
#                 summary = body
#             else:
#                 if word_count < 50:
#                     summary = generate_summary(body, max_length=20)
#                 else:
#                     summary = generate_summary(body, max_length=50)

#             sentiment_result = sentiment_analyzer(summary)
#             label = sentiment_result[0]['label']
#             score = sentiment_result[0]['score']

#             if score >= 0.7:
#                 email_label = "Important"
#             elif score >= 0.4:
#                 email_label = "Least Important"
#             else:
#                 email_label = "Not Important"

#             email_info = {
#                 'From': sender,
#                 'Email Subject': subject,
#                 'Generated Summary': summary,
#                 'Sentiment Label': email_label,
#                 'Sentiment Score': score
#             }
#             summaries.append(email_info)

#     mail.logout()

#     return jsonify(summaries)

# def generate_summary(email_text, max_length=20):
#     inputs = tokenizer([email_text], return_tensors='pt', max_length=1024, truncation=True)

#     with torch.no_grad():
#         try:
#             summary_ids = model.generate(**inputs, max_length=max_length)
#         except ValueError:
#             # Handle cases where min_length is greater than max_length
#             summary_ids = model.generate(**inputs, max_length=max_length, min_length=20)

#     summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
#     return summary

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, render_template, request, jsonify
# import imaplib
# import email
# from transformers import BartForConditionalGeneration, BartTokenizer, pipeline
# import torch

# app = Flask(__name__)

# model_name = 'facebook/bart-large-cnn'
# tokenizer = BartTokenizer.from_pretrained(model_name)
# model = BartForConditionalGeneration.from_pretrained(model_name)

# sentiment_analyzer = pipeline('sentiment-analysis', model='distilbert-base-uncased')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/summarize', methods=['POST'])
# def summarize_email():
#     email_id = request.form['email_id']
#     password = request.form['password']

#     mail = imaplib.IMAP4_SSL('imap.gmail.com')

#     try:
#         mail.login(email_id, password)
#     except imaplib.IMAP4.error:
#         return "Invalid email credentials"

#     mail.select('inbox')

#     summaries = []

#     from datetime import date
#     today = date.today()
#     today_date = today.strftime("%d-%b-%Y")  # Use the full year format (e.g., "25-Oct-2023")

#     status, email_ids = mail.search(None, 'SINCE', today_date)
#     email_ids = email_ids[0].split()

#     for email_id in email_ids:
#         status, msg_data = mail.fetch(email_id, '(RFC822)')
#         raw_email = msg_data[0][1]
#         msg = email.message_from_bytes(raw_email)
#         sender = msg['From']
#         subject = msg['Subject']
#         body = ""

#         if msg.is_multipart():
#             for part in msg.walk():
#                 if part.get_content_type() == "text/plain":
#                     body = part.get_payload(decode=True).decode()
#                     break
#         else:
#             body = msg.get_payload(decode=True).decode()

#         if body:
#             word_count = len(body.split())
#             if word_count < 10:
#                 summary = body
#             else:
#                 if word_count < 50:
#                     summary = generate_summary(body, max_length=20)
#                 else:
#                     summary = generate_summary(body, max_length=50)

#             sentiment_result = sentiment_analyzer(summary)
#             label = sentiment_result[0]['label']
#             score = sentiment_result[0]['score']

#             if score >= 0.7:
#                 email_label = "Important"
#             elif score >= 0.4:
#                 email_label = "Least Important"
#             else:
#                 email_label = "Not Important"

#             email_info = {
#                 'From': sender,
#                 'Email Subject': subject,
#                 'Generated Summary': summary,
#                 'Sentiment Label': email_label,
#                 'Sentiment Score': score
#             }
#             summaries.append(email_info)

#     mail.logout()

#     return jsonify(summaries)

# def generate_summary(email_text, max_length=20):
#     inputs = tokenizer([email_text], return_tensors='pt', max_length=1024, truncation=True)

#     with torch.no_grad():
#         try:
#             summary_ids = model.generate(**inputs, max_length=max_length)
#         except ValueError:
#             # Handle cases where min_length is greater than max_length
#             summary_ids = model.generate(**inputs, max_length=max_length, min_length=20)

#     summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
#     return summary

# if __name__ == '__main__':
#     app.run(debug=True)




from flask import Flask, render_template, request, jsonify
import imaplib
import email
from transformers import BartForConditionalGeneration, BartTokenizer, pipeline
import torch

app = Flask(__name__)

model_name = 'facebook/bart-large-cnn'
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

sentiment_analyzer = pipeline('sentiment-analysis', model='distilbert-base-uncased')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize_email():
    email_id = request.form['email_id']
    password = request.form['password']

    mail = imaplib.IMAP4_SSL('imap.gmail.com')

    try:
        mail.login(email_id, password)
    except imaplib.IMAP4.error:
        return "Invalid email credentials"

    mail.select('inbox')

    summaries = []

    from datetime import date
    today = date.today()
    today_date = today.strftime("%d-%b-%Y")  # Use the full year format (e.g., "25-Oct-2023")

    status, email_ids = mail.search(None, 'SINCE', today_date)
    email_ids = email_ids[0].split()

    for email_id in email_ids:
        status, msg_data = mail.fetch(email_id, '(RFC822)')
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)
        sender = msg['From']
        subject = msg['Subject']
        body = ""

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
                    break
        else:
            body = msg.get_payload(decode=True).decode()

        if body:
            word_count = len(body.split())
            if word_count < 10:
                summary = body
            else:
                if word_count < 50:
                    summary = generate_summary(body, max_length=20)
                else:
                    summary = generate_summary(body, max_length=50)

            sentiment_result = sentiment_analyzer(summary)
            label = sentiment_result[0]['label']
            score = sentiment_result[0]['score']

            if score >= 0.7:
                email_label = "Important"
            elif score >= 0.4:
                email_label = "Least Important"
            else:
                email_label = "Not Important"

            email_info = {
                'From': sender,
                'Email Subject': subject,
                'Generated Summary': summary,
                'Sentiment Label': email_label,
                'Sentiment Score': score
            }
            summaries.append(email_info)

    mail.logout()

    return jsonify(summaries)

def generate_summary(email_text, max_length=20):
    inputs = tokenizer([email_text], return_tensors='pt', max_length=1024, truncation=True)

    with torch.no_grad():
        try:
            summary_ids = model.generate(**inputs, max_length=max_length)
        except ValueError:
            # Handle cases where min_length is greater than max_length
            summary_ids = model.generate(**inputs, max_length=max_length, min_length=20)

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

if __name__ == '__main__':
    app.run(debug=True)
