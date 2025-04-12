import frappe
from .auth import isAdmin
from datetime import datetime
import calendar



def create_leave_application(
    employee, from_date, to_date, reason, leave_type="Sick Leave"
):
    leave_application = frappe.get_doc(
        {
            "doctype": "Leave Application",
            "employee": employee,
            "leave_type": leave_type,
            "from_date": from_date,
            "to_date": to_date,
            "reason": reason,
        }
    )

    leave_application.insert()
    leave_application.submit()


def get_expense_approver(employee_name):
    employee = get_employee_id(employee_name)
    if employee == None:
        return "employee not found expense approver"
    employee = frappe.get_doc("Employee", employee)
    return employee.expense_approver


def get_id_expiring_date(employee_name):
    employee = get_employee_id(employee_name)
    if employee == None:
        return "employee not found expense approver"
    employee = frappe.get_doc("Employee", employee)
    return (
        f"your id number: {employee.passport_number} expiring on: {employee.valid_upto}"
    )


def get_employee_id(name):
    employees = frappe.get_all(
        "Employee",
        fields=[
            "name",
            "employee_name",
        ],
    )
    employee_id = None
    for employee in employees:
        if employee["employee_name"].lower() == name.lower():
            employee_id = employee["name"]
            break
    return employee_id


def get_leave_balance_data(employee_name):
    # lle_list = frappe.get_all("Leave Ledger Entry", fields=["*"])
    # return lle_list
    employee = get_employee_id(employee_name)
    if employee == None:
        return "employee not found"
    allocations = frappe.get_all(
        "Leave Allocation",
        filters={"employee": employee},
        fields=["leave_type", "total_leaves_allocated"],
    )
    allocated_leaves = {}
    for allocation in allocations:
        allocated_leaves[allocation.leave_type] = (
            allocated_leaves.get(allocation.leave_type, 0)
            + allocation.total_leaves_allocated
        )

    leave_applications = frappe.get_all(
        "Leave Application",
        filters={"employee": employee},
        fields=["leave_type", "total_leave_days"],  # Get leave type and leave days
    )

    for application in leave_applications:
        if application.leave_type in allocated_leaves:
            allocated_leaves[application.leave_type] -= application.total_leave_days

    return allocated_leaves


@isAdmin
def get_employee_on_vacation_this_month():
    today_date = datetime.today().date()
    last_date = calendar.monthrange(today_date.year, today_date.month)[1]
    first_day = today_date.replace(day=1)
    end_of_month = today_date.replace(day=last_date)
    print(today_date)
    print(end_of_month)

    # if frappe.session.user != "Administrator":
    #     return "This details are not accessible to you"
    employees_on_vacation = frappe.get_all(
        "Leave Application",
        filters={
            # "status": "Approved",
            "from_date": ["<=", end_of_month],
            # "from_date": today_date,
            "to_date": [">=", today_date],
        },
        fields=["employee_name", "from_date", "to_date", "leave_type"],
        # fields=["*"],
    )
    print(employees_on_vacation)
    vaccation_deatails = []
    for employee in employees_on_vacation:
        vaccation_deatails.append ({
            "Employee name": employee.employee_name,
            "From date": employee.from_date,
            "To date": employee.to_date,
            "Leave type": employee.leave_type,
        })

    print(vaccation_deatails)
    # if vaccation_deatails == None:
    # return "No employee"
    return vaccation_deatails
