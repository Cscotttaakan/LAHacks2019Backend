from mlapp import model_mongodb
from flask import Blueprint, current_app, redirect, request, session, url_for

crud = Blueprint('crud', __name__)

def upload_image_file(file):

    if not file:
        return None

    public_url = storage.upload_file(
            file.read(),
            file.filename,
            file.content_type
            )
    return public_url

@crud.route("/upload", methods=['POST'])
def process():
    if request.method == 'POST':
        data = request.form.to_dict(flat=True)

        image_url = upload_image_file(request.files.get('image'))

        if image_url:
            data['imageUrl'] = image_url

    return 'confirmation of upload'
