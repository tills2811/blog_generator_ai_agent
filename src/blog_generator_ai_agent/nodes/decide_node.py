from typing import Literal
from pydantic import BaseModel, Field
from src.blog_generator_ai_agent.state.state import State
from langchain_core.messages import SystemMessage, HumanMessage

class DecidingNode:
    """
    Decides where to route the query based on the user input.
    """
    def __init__(self,model):
        self.llm = model
    
    def process(self,state:State):
        """ Decides where to route the query based on the user input."""

        class Route(BaseModel):
                step: Literal["yt","assistant"] = Field(
                None, description="The next step in the routing process"
        )

        route=self.llm.with_structured_output(Route)

        decision = route.invoke(
                [
                    SystemMessage(
                        content="Route the user message to yt or assistant."
                    ),
                    HumanMessage(content=state["user_message"]),
                ]
            )
    
        if (decision.step == "yt"):
                    extract_url = self.llm.invoke([
                            SystemMessage(
                                content="Extract youtube url from user message. Only extract youtube link. Don't add any message."
                            ),
                            HumanMessage(content=state["user_message"]),
                        ])
                    
                    return {"yt_url" : extract_url.content , "decision": "yt"}
            
    
        return {"decision": decision.step}
    
    def route_decision(self,state: State):
        # Return the node name you want to visit next
        if state["decision"] == "yt":
            return "yt_transcribe"
        elif state["decision"] == "assistant":
            return "assistant"