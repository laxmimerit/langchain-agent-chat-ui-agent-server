import warnings
warnings.filterwarnings('ignore')

from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent


# Initialize model
model = ChatGoogleGenerativeAI(model='gemini-3-flash-preview')

# Create the deep agent with memory and secure file backend
agent = create_agent(
    model=model,
)


