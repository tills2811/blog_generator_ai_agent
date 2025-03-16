import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage
import json


class DisplayResultStreamlit:
    def __init__(self,usecase,graph,user_message):
        self.usecase= usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message

        if usecase == "Blog generator AI Agent":
            with st.chat_message("user"):
                st.write(user_message)

            # Stream through the graph and get the response events
            for event in graph.stream({'user_message':  user_message}):
             
                for value in event.values():
                    # Show user message
                    if "yt_url" in value:
                        continue  # Skip redundant yt_url display

                    # Get the title from the response and show it
                    # if 'title' in value:
                    #     with st.chat_message("assistant"):
                    #         st.write(f"Title: {value['title']}")

                    # # Get the blog content from the response and show it
                    # if 'blog_content' in value:
                    #     with st.chat_message("assistant"):
                    #         st.write(f"Blog Content: {value['blog_content']}")

                    # Get the final content from the response and show it
                    if 'final_content' in value:
                        with st.chat_message("assistant"):
                            st.write(f"Assistant: {value['final_content']}")

        # elif usecase=="Chatbot with Tool":
        #      # Prepare state and invoke the graph
        #     initial_state = {"messages": [user_message]}
        #     res = graph.invoke(initial_state)
        #     for message in res['messages']:
        #         if type(message) == HumanMessage:
        #             with st.chat_message("user"):
        #                 st.write(message.content)
        #         elif type(message)==ToolMessage:
        #             with st.chat_message("ai"):
        #                 st.write("Tool Call Start")
        #                 st.write(message.content)
        #                 st.write("Tool Call End")
        #         elif type(message)==AIMessage and message.content:
        #             with st.chat_message("assistant"):
        #                 st.write(message.content)
             