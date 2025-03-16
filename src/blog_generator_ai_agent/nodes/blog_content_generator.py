from src.blog_generator_ai_agent.state.state import State
from langchain_core.messages import SystemMessage, HumanMessage

class BlogContentGenerator:
    """
    blog content generation
    """
    def __init__(self,model):
        self.llm = model
    
    def process(self,state: State):
        """Generates a blog without title based on given video transcription."""

        if not state["yt_transcription"]:
            print("❌ Error: No transcription provided to blog_sections_generator")
            return {"blog_content": "No transcription available"}

        try:
            blog = self.llm.invoke(
             [
                SystemMessage(
                    content=(
                        "You are an expert blog writer. Generate a well-structured, engaging blog from the given video transcription. "
                        "Ensure the content is reader-friendly, includes bullet points where necessary, and maintains logical flow. "
                        "Do not include a title."
                        # "Do not add too much content just add 2-3 paragraphs."
                    )
                ),
                HumanMessage(
                    content=(
                        "Here is the video transcription:\n"
                        f"{state['yt_transcription']}\n\n"
                        "### Instructions:\n"
                        "- The blog should be structured into paragraphs.\n"
                        "- Use bullet points where appropriate.\n"
                        "- Keep sentences concise and easy to read.\n"
                        "- Maintain a professional yet engaging tone.\n"
                        "- Do not add a title to the blog."
                        # "- Do not add too much content just add 2-3 paragraphs.It should not be big content."
                        # "- It should be short and crisp."
                    )
                ),
            ]
        )

        # print("✅ Generated Blog:", blog)
            return {"blog_content": blog.content}

        except Exception as e:
            print(f"❌ Error generating blog: {e}")
        return {"blog_content": "Error generating blog"}