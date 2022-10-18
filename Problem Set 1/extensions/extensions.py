fileName = input('File name: ').strip().lower()
fileExtension = fileName.rpartition('.')[2]
mediaTypes = {
    'gif' : 'image/gif',
    'jpg' : 'image/jpeg',
    'jpeg' : 'image/jpeg',
    'png' : 'image/png',
    'pdf' : 'application/pdf',
    'txt' : 'text/plain',
    'zip' : 'application/zip'
}

if fileExtension in mediaTypes:
    print(mediaTypes[fileExtension])
else:
    print('application/octet-stream')