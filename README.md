# COMMVAULT
LINK:http://127.0.0.1:5000/
Document Store Web Application
This is a web application for storing, searching, and downloading documents using AWS services. It allows users to upload files, search for files, and download them.

Table of Contents
Features
Prerequisites
Getting Started
AWS Setup
Application Setup
Deployment
Usage
Contributing
License
Features
Upload Feature: Users can upload documents by providing their email ID and a filename. Files are stored in an Amazon S3 bucket with a naming convention of emailID_filename.

Search Feature: Users can search for documents using their email ID and a search query. Results are displayed in the format emailID_filename.

Download Feature: Based on search results, users can select and download files.

Prerequisites
Before you begin, ensure you have met the following requirements:

AWS account with necessary permissions.
Python 3.x installed on your local machine.
AWS CLI configured with your credentials.
Getting Started
Follow these steps to get your project up and running:

AWS Setup
Create an Amazon EC2 instance (t2.micro) with an Amazon Linux 2023 AMI.
Create an Amazon S3 bucket to store documents/files.
Application Setup
Clone this repository to your local machine.

Install project dependencies by running:

shell
Copy code
pip install -r requirements.txt
Configure your AWS credentials and region by running:

shell
Copy code
aws configure
Follow the prompts to enter your Access Key ID, Secret Access Key, default region, and output format.

Modify the config.py file to specify your S3 bucket name and Flask app settings.

Deployment
Deploy your Flask application to the EC2 instance.

Install Nginx and Gunicorn on the EC2 instance.

Configure Nginx to act as a reverse proxy for your Flask application.

Start the Nginx and Gunicorn services.

Usage
Access the application through the EC2 instance's public IP address or domain name.

Use the web interface to upload, search, and download documents.
