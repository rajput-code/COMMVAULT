import botocore.exceptions

from flask import Flask, render_template, request, redirect, url_for
import boto3
import os

app = Flask(__name__)


s3 = boto3.client('s3')
S3_BUCKET_NAME = 'bucket-198'


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        email_id = request.form['email_id']
        filename = request.form['filename']
        file = request.files['file']

        if email_id and filename and file:
            object_key = f'{email_id}_{filename}'
            try:
                s3.upload_fileobj(file, S3_BUCKET_NAME, object_key)
                return redirect(url_for('search_files'))
            except botocore.exceptions.ClientError as e:
                if e.response['Error']['Code'] == 'AccessDenied':
                    return "Access Denied: You do not have permission to upload files."
                else:
                    return "An error occurred while uploading the file."

    return render_template('upload.html')
    
# Search Feature
@app.route('/search', methods=['GET', 'POST'])
def search_files():
    if request.method == 'POST':
        email_id = request.form['email_id']
        search_query = request.form['search_query']

        if email_id and search_query:
            # List objects in S3 bucket and filter based on email ID and search query
            objects = s3.list_objects_v2(Bucket=S3_BUCKET_NAME)
            results = [obj['Key'] for obj in objects.get('Contents', [])
                       if email_id in obj['Key'] and search_query in obj['Key']]

            return render_template('search_results.html', results=results)

    return render_template('search.html')

@app.route('/download/<path:key>')
def download_file(key):
    # Generate a temporary URL for file download
    url = s3.generate_presigned_url('get_object',
                                    Params={'Bucket': S3_BUCKET_NAME, 'Key': key},
                                    ExpiresIn=3600)  # URL expires in 1 hour

    return redirect(url)

if __name__ == '__main__':
    app.run(debug=True)
