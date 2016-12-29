import os
import uuid
import textract
import detectlanguage
import simplejson as json
from textblob import TextBlob
from flask import Flask, request
from flask_restful import Api, Resource
from werkzeug.utils import secure_filename

###
# Config
app = Flask(__name__, static_path='/static')
# app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = './sources/post_files/'
app.config['PROCESS_FILE'] = './sources/process_file/'
api = Api(app)
detectlanguage.configuration.api_key = "5378434b7720069aa54798b5a70bcc88"


class API(Resource):
    def get(self):
        # FIXME: add frontend page
        return

    def post(self):
        # Get the name of the uploaded file
        file = request.files['file']

        # Unique File Name Generator
        unique_file_name = str(uuid.uuid4()) + secure_filename(file.filename)

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_file_name))

        # Open Saved File
        f = app.config['UPLOAD_FOLDER'] + unique_file_name

        # Process Saved File
        process_data = textract.process(f, encoding='utf-8')

        new_file_name = os.path.splitext(unique_file_name)[0]

        # Final File Process
        final_file = open(app.config['PROCESS_FILE'] + new_file_name + ".txt", 'wb+')
        final_file.write(process_data)
        final_file.close()

        final_file_open = open(app.config['PROCESS_FILE'] + new_file_name + ".txt", 'r+')
        final_file_path = app.config['PROCESS_FILE'] + new_file_name + ".txt"
        ####
        # File Process
        ####

        # Open and split file
        process_file = final_file_open.read().split()
        without_split_process_file = final_file_open.read()

        # Text Analysis with TextBlob
        text_blob_data = TextBlob(without_split_process_file)

        # Length of Words
        len_file = len(process_file)

        detection = detectlanguage.simple_detect(final_file_path)

        final_json_file = json.dumps({
            "document_analysis": {
                "file_name": file.filename,
                "file_size_bytes": os.path.getsize(final_file_path),
                "content_type": file.content_type,
                "length_of_raw_words": len_file,
                "target_language": detection,
                # "target_language": targetlang(final_file_path.decode('utf-8')),
                # "detect_lang": str(detect_langs(final_file_path.decode('utf-8')))
                # "number_of_character": '',
                # "number_of_chars": num_chars
                # "text_subjectivity": text_blob_data.subjectivity,
                # "text_polarity": text_blob_data.polarity
            }
        })

        return json.loads(final_json_file)

    def put(self):
        return "put"

    def delete(self):
        return "delete"


api.add_resource(API, '/')

if __name__ == '__main__':
    app.run(debug=True)
