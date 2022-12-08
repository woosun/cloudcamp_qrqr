import os
from uuid import uuid4

def rename_imagefile_to_uuid(instance,filename):
    print(instance)
    upload_to = f'image/{instance}'
    ext = filename.split('.')[-1]
    uuid = uuid4().hex

    if instance:
        filename = '{}_{}.{}'.format(uuid, instance, ext)
    else:
        filename = '{}.{}'.format(uuid, ext)
    print(upload_to)
    print(filename)
    return os.path.join(upload_to, filename)