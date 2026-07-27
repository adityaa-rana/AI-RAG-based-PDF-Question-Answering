from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    ToolMessage,
)

# Shared chat history
chat_history = []


def get_chat_history():
    """
    Return the complete chat history.
    """

    return chat_history


def add_human_message(message: str):
    """
    Add a user message to the chat history.
    """

    chat_history.append(
        HumanMessage(content=message)
    )


def add_ai_message(message: str):
    """
    Add an AI response to the chat history.
    """

    chat_history.append(
        AIMessage(content=message)
    )


def add_tool_message(message: str, tool_name: str):
    """
    Add a tool response to the chat history.
    """

    chat_history.append(
        ToolMessage(
            content=message,
            name=tool_name
        )
    )


def clear_chat_history():
    """
    Clear the chat history.
    """

    chat_history.clear()