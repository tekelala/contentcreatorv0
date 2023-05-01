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
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

# Streamlit application
def app():
    # Title of the application
    st.title("Content Creator with GPT-3.5-turbo")

    # Input field for the user to enter a topic
    topic = st.text_input("Enter a topic:")

    # Button to generate content
    if st.button("Create"):
        # If the input field is not empty, get the content from GPT-3.5-turbo
        if topic:
            with st.spinner('Generating content...'):
                # Call the function to get the completion
                content = get_completion(topic)
                # Display the generated content
                st.write(content)
        else:
            st.error("Please enter a topic.")

# Run the application
if __name__ == "__main__":
    app()