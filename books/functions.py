#function to upload files from form to static file (specified path)
def handle_uploaded_file(file):
    with open('books/static/books/'+file.name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
