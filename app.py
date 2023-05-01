# Importing required libraries
import openai
import streamlit as st
import os

# Function to get the model completion
def get_completion(prompt, model="gpt-4"):
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
    
    role_prompt = """Nice and insightful AI and Businees Expert think of a mix of Andrew Ng, \
    Clayton Christensen and Richard Rumelt \
    you are the creator of Business Cyborgs, \
    you are an expert creating content for a business minded audience \
    so your steps by step guide should be easy to follow and understand. \
    Your purpose is to help businesspeople leverage technology to dramatically \
    increase their capabilities, allowing them to develop their roles and \
    free up time and energy to focus on activities that generate more value, \
    whether for the organization or for themselves. Never mention who you are or \
    the tools you use to reason about the topic and never ask the user to use \
    storytelling techniques perform the tasks.  
    
    """
    
    goal_prompt = """to give an step by step guide on how leverage on AI tools \
    to be more efficient give your readers more time to focus on the things \
    that matter and use much better their human capabilities. \
    You use the Nancy Duarte method to create your content and make it clear and impactful, \
    you are a master of the art of storytelling and you know how to use it.\
    """

    # Define a variable to store the contents of the file
    fixed_inspiration = ""

    # Open the file and read its contents
    try:
        with open('fixed_inspiration.txt', 'r', encoding='utf-8') as file:
        fixed_inspiration = file.read()
    except FileNotFoundError:
        print("The file 'fixed_inspiration.txt' was not found.")
    
    prompt = f"""
    You are ```{role_prompt}``` and take these {fixed_inspiration} of you as \
    an inspiration and style guide  and your goal is ```{goal_prompt}``` \
    with the assistance of AI tools and the following ```{tools_prompt}``` \
    to perform the following ```{tasks}``` in 1000 words. The structure of the content \
    is: 1. Introduction (A engaging short instriduction describing how to perform the task \
    as a Business Cyborg); 2. The step by step; 3. a short wrap up conclusion and an \
    invitation to the reader to try the tools, the method and to follow and become a Business Cyborg. \
    """

    # Button to generate content
    if st.button("Create"):
        # If the input field is not empty, get the content from GPT
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