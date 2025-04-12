import frappe

def getDesignation(name):
    users = frappe.get_all(
        "Employee",
        fields=[
            "name",
            "employee_name",
            "designation",
            "date_of_joining",
        ],
    )


    for item in users:
        if item["employee_name"].lower() == name.lower():
            return f"date of joining: {item["date_of_joining"]}, employee name: {item["employee_name"]}, designation: {item["designation"]}"
    return "not available"