import streamlit as st
from openai import OpenAI

class Page1:
    def __init__(self):
        # Initialize the OpenAI client using the API key from secrets.
        # from secret_keys import openai_api_key
        self.client = OpenAI(api_key = st.secrets.OpenAIAPI.openai_api_key)

        prompt = """
        Take the role of an experienced trip adviser who  is specializes in assisting unique travel experiences.
        You have extensive knowledge about various destinations, have read widely on travel trends,
        and understand the difficulty of planning memorable trips for diverse preferences.
        """

        # Using st.session_state to store the exchange of messages.
        if "trip_adviser_messages" not in st.session_state:
            st.session_state["trip_adviser_messages"] = [
                {"role": "system", "content": prompt}
            ]

        # Function for interacting with a chatbot.
        def communicate():
            messages = st.session_state["trip_adviser_messages"]

            user_message = {"role": "user", "content": st.session_state["user_input"]}
            messages.append(user_message)

            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            bot_message = response.choices[0].message
            messages.append(bot_message)

            st.session_state["user_input"] = ""

        # User Interface
        st.title("Trip Adviser AI")
        st.image("tripAdviser.png")
        st.write("Discover, Plan, and Explore Seamlessly.")

        user_input = st.text_input("Please enter a message here.", key="user_input", on_change=communicate)

        if st.session_state["trip_adviser_messages"]:
            messages = st.session_state["trip_adviser_messages"]

            for message in reversed(messages[1:]):
                if isinstance(message, dict):
                    speaker = "😎" if message["role"] == "user" else "🤖"
                    st.write(speaker + ": " + message["content"])
                else:
                    st.write("🤖: " + message.content)

class Page2:
    def __init__(self):
        # Initialize the OpenAI client using the API key from secrets.
        # from secret_keys import openai_api_key
        self.client = OpenAI(api_key = st.secrets.OpenAIAPI.openai_api_key)

        prompt = """
        You are a business adviser, acting as a senior startup specialist who is a expert in growing platforms specific to startup business.
        You have read all the biggest startup books and understand how the flow of startup business works.

        """

        # Using st.session_state to store the exchange of messages.
        if "business_adviser" not in st.session_state:
            st.session_state["business_adviser"] = {
                "messages": [
                    {"role": "system", "content": prompt}
                ]
            }

        # Function for interacting with a chatbot.
        def communicate():
            messages = st.session_state["business_adviser"]["messages"]

            user_message = {"role": "user", "content": st.session_state["user_input"]}
            messages.append(user_message)

            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            bot_message = response.choices[0].message
            messages.append(bot_message)

            st.session_state["user_input"] = ""

        # User Interface
        st.title("Business Adviser AI")
        st.image("businessAdviser.png")
        st.write("Create your own business.")

        user_input = st.text_input("Please enter a message here.", key="user_input", on_change=communicate)

        if st.session_state["business_adviser"]["messages"]:
            messages = st.session_state["business_adviser"]["messages"]

            for message in reversed(messages[1:]):
                if isinstance(message, dict):
                    speaker = "😎" if message["role"] == "user" else "🤖"
                    st.write(speaker + ": " + message["content"])
                else:
                    st.write("🤖: " + message.content)


class Page3:
    def __init__(self):
        # Initialize the OpenAI client using the API key from secrets.
        # from secret_keys import openai_api_key
        self.client = OpenAI(api_key = st.secrets.OpenAIAPI.openai_api_key)

        prompt = """
        You are a dream interpreter.
        Assume the persona of a dream analyst who specializes in the meanings behind dreams.
        You have immersed yourself in dream symbolism, studied various dream theories,
        and have a deep understanding of the psychological aspects associated with dream interpretation.

        """

        # Using st.session_state to store the exchange of messages.
        if "dream_interprater" not in st.session_state:
            st.session_state["dream_interprater"] = {
                "messages": [
                    {"role": "system", "content": prompt}
                ]
            }

        # Function for interacting with a chatbot.
        def communicate():
            messages = st.session_state["dream_interprater"]["messages"]

            user_message = {"role": "user", "content": st.session_state["user_input"]}
            messages.append(user_message)

            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            bot_message = response.choices[0].message
            messages.append(bot_message)

            st.session_state["user_input"] = ""

        # User Interface
        st.title("Dream Adviser AI")
        st.image("dreamInterprater.png")
        st.write("Talk about your dream.")

        user_input = st.text_input("Please enter a message here.", key="user_input", on_change=communicate)

        if st.session_state["dream_interprater"]["messages"]:
            messages = st.session_state["dream_interprater"]["messages"]

            for message in reversed(messages[1:]):
                if isinstance(message, dict):
                    speaker = "😎" if message["role"] == "user" else "🤖"
                    st.write(speaker + ": " + message["content"])
                else:
                    st.write("🤖: " + message.content)

class Page4:
    def __init__(self):
        # Initialize the OpenAI client using the API key from secrets.
        # from secret_keys import openai_api_key
        self.client = OpenAI(api_key = st.secrets.OpenAIAPI.openai_api_key)

        prompt = """
        You are a prompt teacher.
        Imagine yourself as an expert instructor in the art of creating engaging and effective prompts for various purposes.
        You have deep knowledge on diverse writing styles,
        and you are skilled in techniques that inspire creativity and clearity.

        """

        # Using st.session_state to store the exchange of messages.
        if "prompt_teacher" not in st.session_state:
            st.session_state["prompt_teacher"] = {
                "messages": [
                    {"role": "system", "content": prompt}
                ]
            }

        # Function for interacting with a chatbot.
        def communicate():
            messages = st.session_state["prompt_teacher"]["messages"]

            user_message = {"role": "user", "content": st.session_state["user_input"]}
            messages.append(user_message)

            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            bot_message = response.choices[0].message
            messages.append(bot_message)

            st.session_state["user_input"] = ""

        # User Interface
        st.title("Prompt Teacher AI")
        st.image("promptTeacher.png")
        st.write("Master on prompt.")

        user_input = st.text_input("Please enter a message here.", key="user_input", on_change=communicate)

        if st.session_state["prompt_teacher"]["messages"]:
            messages = st.session_state["prompt_teacher"]["messages"]

            for message in reversed(messages[1:]):
                if isinstance(message, dict):
                    speaker = "😎" if message["role"] == "user" else "🤖"
                    st.write(speaker + ": " + message["content"])
                else:
                    st.write("🤖: " + message.content)

class Page5:
    def __init__(self):
        # Initialize the OpenAI client using the API key from secrets.
        # from secret_keys import openai_api_key
        self.client = OpenAI(api_key = st.secrets.OpenAIAPI.openai_api_key)

        prompt = """
        Think as an intermediate level European Portuguese Language teacher.
        You are an expert in teaching european portuguese with specific emphasis on spoken and colloquial portuguese.
        You answer questions by providing many detailed examples and explaining choices of verbs and tenses. In addition
        you are expert in providing tips and hints and detailed guidance on how to improve both spoken and written
        European portuguese. You will answer in the English language but provide examples where relevant in European Portuguese.

        """

        # Using st.session_state to store the exchange of messages.
        if "portuguese_language_teacher" not in st.session_state:
            st.session_state["portuguese_language_teacher"] = {
                "messages": [
                    {"role": "system", "content": prompt}
                ]
            }

        # Function for interacting with a chatbot.
        def communicate():
            messages = st.session_state["portuguese_language_teacher"]["messages"]

            user_message = {"role": "user", "content": st.session_state["user_input"]}
            messages.append(user_message)

            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            bot_message = response.choices[0].message
            messages.append(bot_message)

            st.session_state["user_input"] = ""

        # User Interface
        st.title("Portuguese Langauge Teacher")
        # st.image("Portuguese_Langauge_Teacher.png")
        st.write("Master on European Portuguese.")

        user_input = st.text_input("Please enter a message here.", key="user_input", on_change=communicate)

        if st.session_state["portuguese_language_teacher"]["messages"]:
            messages = st.session_state["portuguese_language_teacher"]["messages"]

            for message in reversed(messages[1:]):
                if isinstance(message, dict):
                    speaker = "😎" if message["role"] == "user" else "🤖"
                    st.write(speaker + ": " + message["content"])
                else:
                    st.write("🤖: " + message.content)



def main():
    sidebar = st.sidebar

    page = sidebar.radio("Select Chatbot", ["Trip Adviser", "Business Adviser","Dream Interprater", "Prompt Teacher","Portuguese Langauge Teacher"])

    if page == "Trip Adviser":
        Page1()
    elif page == "Business Adviser":
        # Reset the business_adviser_messages session state to ensure the initial system message is always added
        st.session_state["business_adviser_messages"] = []
        Page2()
    elif page == "Dream Interprater":
        st.session_state["dream_interprater_messages"] = []
        Page3()
    elif page == "Prompt Teacher":
        st.session_state["prompt_teacher_messages"] = []
        Page4()
    elif page == "Portuguese Langauge Teacher":
        st.session_state["portuguese_language_teacher_messages"] = []
        Page5()


if __name__ == "__main__":
    main()

