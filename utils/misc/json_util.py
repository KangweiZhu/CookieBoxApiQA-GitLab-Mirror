from modal.test_case import ApiTestCase


def default_serializer(obj):
    if isinstance(obj, ApiTestCase):
        return obj.beautifier()
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")