import uuid


def generate_unique_email():
    return f'autotest_{uuid.uuid4().hex[:12]}@test.com'
