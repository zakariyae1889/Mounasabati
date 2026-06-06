import uuid
from slugify import slugify
from models.service import Service

def generate_uinque_slug(db,service_name:str)->str:
    slug=slugify(service_name)
    while db.query(Service).filter(Service.slug==slug).first():
        slug=slugify(service_name)+"-"+str(uuid.uuid4())[:8]
    return slug