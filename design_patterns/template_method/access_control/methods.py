import functools
from . import LoginPermissionChecker, VisitorPermissionChecker, CardPermissionChecker
from flask import abort, session
from werkzeug.exceptions import Unauthorized
from common import *

def check_login_permission(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if not LoginPermissionChecker().check_permission(): Unauthorized()
        return f(*args, **kwargs)
    return wrapper

def check_visitor_permission(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if not VisitorPermissionChecker().check_permission(): Unauthorized()
        return f(*args, **kwargs)
    return wrapper

def check_card_permission(f):
    @functools.wraps(f)
    def wrapper(current_proc = None, *args, **kwargs):
        # Question: is there possible security problem revealing card uuid in session?
        permission_checker = CardPermissionChecker.get_card_permission_checker(current_proc)
        if not permission_checker or not permission_checker.check_permission():
            Unauthorized()
        return f(*args, **kwargs)
    return wrapper
