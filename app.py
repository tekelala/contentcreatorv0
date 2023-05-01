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

# Streamlit application
def app():
    # Title of the application
    st.title("Content Creator, please provide the taks you want to get the step by step guide")

    # Input field for the user to enter a topic
    tasks = st.text_input("Enter a task:")

    # Where the magic happens, the prompt
    
    role_prompt = """Nice and insightful professor as Andrew Ng
    """
    
    goal_prompt = """to give an step by step guide on how leverage on AI tools \
    to be more efficient give your readers more time to focus on the things \
    that matter and use much better their human capabilities
    """
    
    prompt = f"""
    You are ```{role_prompt}``` and your goal is ```{goal_prompt}``` to perform with the assistance of AI tool the following ```{tasks}``` in 1000 words.
    """

    # Button to generate content
    if st.button("Create"):
        # If the input field is not empty, get the content from GPT-3.5-turbo
        if tasks:
            with st.spinner('Generating content...'):
                # Call the function to get the completion
                content = get_completion(prompt)
                # Display the generated content
                st.write(content)
        else:
            st.error("Please enter a task.")

# Run the application
if __name__ == "__main__":
    app()