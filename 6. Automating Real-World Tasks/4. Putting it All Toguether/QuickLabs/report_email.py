#!/usr/bin/env python3

import os
from datetime import date
import reports
import emails

desc_path = "/home/student-01-762b3df1d2aa/supplier-data/descriptions/"
report = []

def process_data(data):
    for item in data:
        report.append("name: {}<br/>weight: {}\n".format(item[0], item[1]))
    return report

text_data = []
for text_file in os.listdir(desc_path):
    with open(desc_path + text_file, 'r') as f:
        text_data.append([line.strip() for line in f.readlines()])
        f.close()

if __name__ == "__main__":
    summary = process_data(text_data)
    paragraph = "<br/><br/>".join(summary)
    title = "Processed Update on {}\n".format(date.today().strftime("%B %d, %Y"))
    attachment = "/tmp/processed.pdf"
    reports.generate_report(attachment, title, paragraph)

    sender = "automation@example.com"
    receiver = "student-01-762b3df1d2aa@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)

