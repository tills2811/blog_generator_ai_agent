from pydantic import BaseModel, Field
from src.blog_generator_ai_agent.state.state import State
from langchain_core.messages import SystemMessage, HumanMessage



class TitleGenerator:
    """
    Title generation
    """
    def __init__(self,model):
        self.llm = model


    def process(self,state:State):
        """Generates a title based on given video transcription"""

        if not state["yt_transcription"]:
            print("❌ Error: No transcription provided to title_generator")
            return {"title": "No transcription available"}
        
        class Title(BaseModel):
            title: str = Field(
            description="Give a good title for the given video transcription which we can use for a blog"
        )


        title_llm = self.llm.with_structured_output(Title)

        # Generate queries
        title_agent = title_llm.invoke(
            [
                SystemMessage(content="Generate a title for a given video transcription."),
                HumanMessage(content=f"Here is the video transcription:\n{state['yt_transcription']}"),
            ]
        )

        print("Generated Title:", title_agent.title)
        # print("title_agent:",title_agent)

        return {"title": title_agent.title} 