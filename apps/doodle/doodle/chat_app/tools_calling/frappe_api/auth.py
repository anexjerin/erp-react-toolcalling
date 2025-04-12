import frappe

def isAdmin(func):
    def wrapper(*args, **kwargs):
        if frappe.session.user != "Administrator":
            return "This details are not accessible to you"
        return func(*args, **kwargs)
    return wrapper