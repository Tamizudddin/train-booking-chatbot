from langchain_ollama import OllamaLLM

def get_train_bot_response(user_prompt: str, chat_history: str):
    # Initialize the local Ollama model
    llm = OllamaLLM(model="llama3", temperature=0.3)
    
    # Construct a simple prompt string
    formatted_prompt = f"""
    You are an AI assistant specialized in Indian Railways and train bookings. 
    Your goal is to help users find train schedules, check PNR status, understand ticket classes (1A, 2A, 3A, SL, CC), 
    and guide them safely to the official IRCTC website for final checkout and payment.
    
    Chat History:
    {chat_history}
    
    User: {user_prompt}
    Assistant:
    """
    
    # Generate response directly from the model
    response = llm.invoke(formatted_prompt)
    return response