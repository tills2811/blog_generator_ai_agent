from src.blog_generator_ai_agent.state.state import State


class ContentAggregator:
    """Aggregates the both content"""
    
    def process(self,state:State):
        """Synthesize full content"""

        # Get title and blog content from state
        blog_title = state["title"]
        content = state["blog_content"]

         # Ensure title and content are not empty
        if not blog_title:
            blog_title = "Untitled"
        if not content:
            content = "No blog content available."

         # Format completed sections for final content
        final_content = "\n\n---\n\n".join([blog_title, content])

        return {"final_content": final_content}