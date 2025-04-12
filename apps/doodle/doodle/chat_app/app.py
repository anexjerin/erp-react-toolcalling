from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# from .tools import custom_tools, tools_mapping
import json
import frappe
import os
from .tools_calling.tools import custom_tools, tools_mapping

load_dotenv()


def interact_with_llm_and_tools(human_message: str):
    llm = init_chat_model("deepseek-r1-distill-llama-70b", model_provider="groq")
    llm_with_tools_new = llm.bind_tools(custom_tools)
    llm_output = llm_with_tools_new.invoke(human_message)
    print(llm_output)
    if llm_output.content != "":
        return [llm_output.content]
    messages = []
    for tool_call in llm_output.tool_calls:
        tool = tools_mapping[tool_call["name"].lower()]
        tool_output = tool.invoke(tool_call["args"])
        print(type(tool_output))
        if type(tool_output) == list:
            print("hey\n")
            messages.extend(tool_output)
        else:
            messages.append(tool_output)
    return messages


@frappe.whitelist(allow_guest=False)
def chat_bot(data):
    return interact_with_llm_and_tools(data)

    # return 'hello'

    # leave_data = leave.get_leave_balance_data(data)
    # print(leave_data)
    # return leave_data
    # data = leave.get_doctype_fields("Leave Allocation")
    # print(data)


@frappe.whitelist(allow_guest=False)
def store_api_key(key):
    site_config_path = frappe.get_site_path("site_config.json")

    if not os.path.exists(site_config_path):
        frappe.throw(("site_config.json not found"))
    with open(site_config_path, "r") as f:
        config = json.load(f)
    config["external_api_key"] = key
    with open(site_config_path, "w") as f:
        json.dump(config, f, indent=4)

    return "API Key saved successfully!"


@frappe.whitelist(allow_guest=False)
def check_if_api_key():
    external_api_key = frappe.conf.get("file_watcher_port")
    if external_api_key is None:
        return "No API key found"
    return "Api key found"
