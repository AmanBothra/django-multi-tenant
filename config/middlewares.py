import threading
from .utils import tenant_db_from_request

THREAD_LOCAL = threading.local()


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        db = tenant_db_from_request(request)
        print(db, "======db")
        setattr(THREAD_LOCAL, "DB", db)
        response = self.get_response(request)
        return response


def get_current_db_name():
    """
    get current db
    """
    return getattr(THREAD_LOCAL, "DB", None)


def set_db_for_router(db):
    """
    set db router according to router
    """
    setattr(THREAD_LOCAL, "DB", db)
