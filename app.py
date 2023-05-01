# Importing required libraries
import openai
import streamlit as st
import os

# Function to get the model completion
def get_completion(prompt, model="gpt-3.5-turbo"):
    # Set the OpenAI API key from the environment variable
    openai_api_key = os.getenv('OPENAI_API_KEY')
    
    # Check if the API key is set
    if not openai_api_key:
        return "API key for OpenAI not found. Please set the 'OPENAI_API_KEY' environment variable."

    openai.api_key = openai_api_key
    messages = [{"role": "user", "content": prompt}]
        
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.8, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

# Function to get the table
def get_completion_table(prompt, model="gpt-3.5-turbo"):
    # Set the OpenAI API key from the environment variable
    openai_api_key = os.getenv('OPENAI_API_KEY')
    
    # Check if the API key is set
    if not openai_api_key:
        return "API key for OpenAI not found. Please set the 'OPENAI_API_KEY' environment variable."

    openai.api_key = openai_api_key
    messages = [{"role": "user", "content": prompt}]
        
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.8, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

# Streamlit application
def app():
    # Title of the application
    st.title("Content Creator, please provide the taks you want to get the step by step guide")

    # Input field for the user to enter a topic
    tasks = st.text_input("Enter a task:")

    # Multiselect widget for choosing tools
    predefined_tools = ["Microsoft 365", "Google Workspace", "OpenAI", "Canva", "Another Tool"]
    selected_tools = st.multiselect("Select tools to use:", options=predefined_tools)

    # Text input field for specifying an additional tool
    additional_tool = ""
    if "Another Tool" in selected_tools:
        additional_tool = st.text_input("Enter the name of the additional tool:")

    # Create the tools_prompt by concatenating the selected tools
    tools_prompt = ", ".join([tool for tool in selected_tools if tool != "Another Tool"])
    if additional_tool:
        tools_prompt += f", {additional_tool}"

    # Where the magic happens, the prompt
    
    role_prompt = """Nice and insightful AI expert as Andrew Ng \
    you are an expert creating content for a business minded audience \
    so your steps by step guide should be easy to follow and understand \
    """
    
    goal_prompt = """to give an step by step guide on how leverage on AI tools \
    to be more efficient give your readers more time to focus on the things \
    that matter and use much better their human capabilities, \
    your steps by step guide should be easy to follow and understand \
    and use of the following business tools: \
    - Google Workspace and Microsoft 365 when you choose one Microsoft \ 
    mention the equivalent of Google and viceversa\ 
    the other company equivalent  \
    - OpenAI
    - Canva
    """
    
    prompt = f"""
    You are ```{role_prompt}``` and your goal is ```{goal_prompt}``` \
    with the assistance of AI tools and the following ```{tools_prompt}``` \
    to perform the following ```{tasks}``` in 1000 words.
    """

    tools_prompt = 

    # Button to generate content
    if st.button("Create"):
        # If the input field is not empty, get the content from GPT-3.5-turbo
        if tasks:
            with st.spinner('Generating content...'):
                # Call the function to get the completion
                content = get_completion(prompt)
                # Call the function to get the table
                prompt_table = f""" Yor task is to take the {content} and create \
                    a table with the following columns: \
                    Step, Description, AI tool used, Link to the tool."""
                table_sbs = get_completion_table(prompt_table)
                # Display the generated content
                st.write(content)
                st.write(table_sbs)
        else:
            st.error("Please enter a task.")

# Run the application
if __name__ == "__main__":
    app()