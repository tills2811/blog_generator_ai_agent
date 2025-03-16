from langchain_core.messages import SystemMessage, HumanMessage

from src.blog_generator_ai_agent.state.state import State

class Assistant:
    """Gives answer based on user query."""
    def __init__(self,model):
        self.llm = model
    
    def process(self,state:State):
        
        assistant_reply= self.llm.invoke(
            [
                SystemMessage(content="You are a helpful assistant."),
                HumanMessage(content=state["user_message"]),
            ]
        )
        return{"final_content" : assistant_reply.content}