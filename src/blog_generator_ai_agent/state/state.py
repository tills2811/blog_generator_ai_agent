from typing import Annotated, Literal, Optional
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from typing import TypedDict, Annotated, List
from langchain_core.messages import HumanMessage, AIMessage
from pydantic import BaseModel

class State(TypedDict):
    """
    Represents the structure of the state used in the graph.
    """
    user_message:str
    decision:str
    yt_url: str
    yt_transcription: str = ""
    title: str = ""
    blog_content: str = ""
    final_content:str = ""