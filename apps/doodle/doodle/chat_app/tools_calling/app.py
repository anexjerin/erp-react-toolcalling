from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from .tools import custom_tools, tools_mapping
from .frappe_api import users, items

import frappe

load_dotenv()


def interact_with_llm_and_tools(human_message: str, user: str, roles):
    # llm = init_chat_model("gpt-4o-mini", model_provider="openai", api_key="your-api-key")
    # llm = init_chat_model("gpt-4o-mini", model_provider="openai")
    # llm = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")
    # res = llm.invoke(human_message)
    # res = 'hi'
    # return res.content
    roles = frappe.get_roles(user)
    return roles
    llm_with_tools_new = llm.bind_tools(custom_tools)
    llm_output = llm_with_tools_new.invoke(human_message)
    print(llm_output)
    if llm_output.content != "":
        return [llm_output.content]
    messages = []
    for tool_call in llm_output.tool_calls:
        tool = tools_mapping[tool_call["name"].lower()]
        # print(tool)
        tool_output = tool.invoke(tool_call["args"])
        messages.append(tool_output)
    return messages


# def interact_with_llm_and_tools(human_message: str):
#    return items.getLeave(human_message)


@frappe.whitelist(allow_guest=False)
def custom_function(data):
    user = frappe.session.user
    roles = frappe.get_roles(user)
    return interact_with_llm_and_tools(data, user, roles)
