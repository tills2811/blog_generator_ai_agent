from langgraph.graph import StateGraph, START,END, MessagesState
from langgraph.prebuilt import tools_condition,ToolNode
from langchain_core.prompts import ChatPromptTemplate
from src.blog_generator_ai_agent.nodes.assistant_node import Assistant
from src.blog_generator_ai_agent.nodes.blog_content_generator import BlogContentGenerator
from src.blog_generator_ai_agent.nodes.content_aagregator import ContentAggregator
from src.blog_generator_ai_agent.nodes.decide_node import DecidingNode
from src.blog_generator_ai_agent.nodes.title_generator_node import TitleGenerator
from src.blog_generator_ai_agent.nodes.yt_transcribe_node import YTTranscription
from src.blog_generator_ai_agent.state.state import State
# from src.blog_generator_ai_agent.nodes.basic_chatbot_node import BasicChatbotNode
# from src.blog_generator_ai_agent.nodes.chatbot_with_Tool_node import ChatbotWithToolNode
# from src.blog_generator_ai_agent.tools.serach_tool import get_tools,create_tool_node




class GraphBuilder:

    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)

    def blog_generator_graph(self):
        """
        Builds a blog blog generator ai agent 
        """

        self.yt_transcribe=YTTranscription()
        self.title_generator=TitleGenerator(self.llm)
        self.blog_content_generator=BlogContentGenerator(self.llm)
        self.content_aggregator=ContentAggregator()
        self.decide_node=DecidingNode(self.llm)
        self.assistant=Assistant(self.llm)


        # self.basic_chatbot_node=BasicChatbotNode(self.llm)
        self.graph_builder.add_node("deciding_node",self.decide_node.process)
        self.graph_builder.add_node("assistant",self.assistant.process)
        self.graph_builder.add_node("yt_transcribe",self.yt_transcribe.process)
        self.graph_builder.add_node("title_generator",self.title_generator.process)
        self.graph_builder.add_node("blog_content_generator",self.blog_content_generator.process)
        self.graph_builder.add_node("content_aggregator",self.content_aggregator.process)



        self.graph_builder.add_edge(START,"deciding_node")
        self.graph_builder.add_conditional_edges("deciding_node", self.decide_node.route_decision, {  
        "yt_transcribe": "yt_transcribe",
        "assistant": "assistant",
    },)
        self.graph_builder.add_edge("yt_transcribe", "title_generator")
        self.graph_builder.add_edge("yt_transcribe", "blog_content_generator")
        self.graph_builder.add_edge("title_generator", "content_aggregator")
        self.graph_builder.add_edge("blog_content_generator", "content_aggregator")
        self.graph_builder.add_edge("content_aggregator", END)
        self.graph_builder.add_edge("assistant", END)


#     def chatbot_with_tools_build_graph(self):
#         """
#         Builds an advanced chatbot graph with tool integration.
#         This method creates a chatbot graph that includes both a chatbot node 
#         and a tool node. It defines tools, initializes the chatbot with tool 
#         capabilities, and sets up conditional and direct edges between nodes. 
#         The chatbot node is set as the entry point.
#         """
#         ## Define the tool and tool node

#         # tools=get_tools()
#         # tool_node=create_tool_node(tools)

#         ##Define LLM
#         llm = self.llm

#         # Define chatbot node
#         # obj_chatbot_with_node = ChatbotWithToolNode(llm)
#         # chatbot_node = obj_chatbot_with_node.create_chatbot(tools)

#         # Add nodes
#         # self.graph_builder.add_node("chatbot", chatbot_node)
#         # self.graph_builder.add_node("tools", tool_node)
# # 
#         # Define conditional and direct edges
#         self.graph_builder.add_edge(START,"chatbot")
#         self.graph_builder.add_conditional_edges("chatbot", tools_condition)
#         self.graph_builder.add_edge("tools","chatbot")

    
    
    
    def setup_graph(self, usecase: str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase == "Blog generator AI Agent":
            self.blog_generator_graph()

        # if usecase == "Chatbot with Tool":
        #     self.chatbot_with_tools_build_graph()
        return self.graph_builder.compile()
    




    
