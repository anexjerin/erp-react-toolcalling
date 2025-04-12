import frappe


def getItemPrice(name):
    items = frappe.get_all(
        "Item",
        fields=["name", "item_group", "stock_uom", "item_name", "valuation_rate"],
    )
    if items is not None:
        for item in items:
            if item["item_name"].lower() == name.lower():
                return f"price : {item["valuation_rate"]}"
            # return item
        return None


def getDesignation(name):
    items = frappe.get_all(
        "Employee",
        fields=[
            "name",
            "employee_name",
            "designation",
            # "department",
            "date_of_joining",
        ],
    )
    # return name
    names = ''
    # for item in items:
    #     names += item['employee_name'] + '\n'
    # return names


    for item in items:
        if item["employee_name"].lower() == name.lower():
            return f"date of joining: {item["date_of_joining"]}, employee name: {item["employee_name"]}, designation: {item["designation"]}"
        # return "not available for"
    return "not available"


def getLeaveDet(employee_name):
    items = frappe.get_all(
        "Employee",
        fields=[
            "name",
            "employee_name",
        ],
    )
    employee_id = None

    for item in items:
        if item["employee_name"].lower() == employee_name.lower():
            employee_id = item["name"]
            break
            # return employee_id

    employee = frappe.get_all(
        "Leave Allocation",
        filters={"employee": employee_id},
        fields=[
            "leave_type",
            "total_leaves_allocated",
            "unused_leaves",
            "leave_period",
            # "leave_balance",
        ],
    )
    # employee = frappe.get_all(
    #     "Leave Application",
    #     filters={"employee": employee_id},
    #     fields=["from_date", "to_date", "leave_type", "status"],
    # )

    result = ""
    for emp in employee:
        # result += f"{emp['leave_type']} : {emp['from_date']} , {emp['status']} \n"
        result += f"{emp['leave_type']} : {emp['total_leaves_allocated']} , {emp['unused_leaves']} {emp['leave_period']}\n"
    return result
