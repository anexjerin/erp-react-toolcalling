from langchain_core.tools import tool
from .frappe_api.leave import get_leave_balance_data,get_expense_approver,get_id_expiring_date,get_employee_on_vacation_this_month


@tool
def find_leave_balance(name:str):
    """For cheking the leave balance available."""
    return get_leave_balance_data(name)

@tool
def apply_leave(name:str):
    """For applying leave."""
    return "applied leave"

@tool
def finding_expense_approver(name:str):
    """For finding Expense Approver."""
    return get_expense_approver(name)

@tool
def finding_id_expiring_date(name:str):
    """For visa/passport/emirate ID expiring date."""
    return get_id_expiring_date(name)

@tool
def finding_employee_on_vacation_this_month():
    """For finding employee on vacation."""
    return get_employee_on_vacation_this_month()

custom_tools = [
    find_leave_balance,
    apply_leave,
    finding_expense_approver,
    finding_id_expiring_date,
    finding_employee_on_vacation_this_month
]

tools_mapping = {
    "find_leave_balance": find_leave_balance,
    "apply_leave": apply_leave,
    "finding_expense_approver": finding_expense_approver,
    "finding_id_expiring_date": finding_id_expiring_date,
    "finding_employee_on_vacation_this_month": finding_employee_on_vacation_this_month
}