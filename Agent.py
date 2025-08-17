import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")


prompt_template = PromptTemplate(
    input_variables=["feedback"],
    template="""
    You are a helpful assistant for the restaurant 'SteamNoodles'.
    Your task is to analyze the sentiment of the following customer feedback and generate a short, polite, and context-aware reply.

    The sentiment can be positive, negative, or neutral. The reply should acknowledge the customer's key points.

    Customer Feedback: "{feedback}"

    Generated Reply:
    """
)


feedback_response_agent = LLMChain(llm=llm, prompt=prompt_template)

def get_automated_response(customer_feedback: str) -> str:
    """
    Generates an automated response for a given customer feedback.
    
    Args:
        customer_feedback: The text of the customer's review.
        
    Returns:
        A polite and context-aware automated reply.
    """
    response = feedback_response_agent.invoke({"feedback": customer_feedback})
    return response['text']


print("--- Customer Feedback Response Agent Demo ---")


positive_feedback = "The spicy ramen was absolutely delicious, and the service was incredibly fast! Best noodles in town."
positive_response = get_automated_response(positive_feedback)
print(f"\n[+] Sample Positive Feedback:\n'{positive_feedback}'")
print(f"\n[=] Automated Response:\n'{positive_response.strip()}'")


negative_feedback = "I was really disappointed with my visit. The broth was lukewarm, and my order took almost 45 minutes to arrive."
negative_response = get_automated_response(negative_feedback)
print(f"\n[-] Sample Negative Feedback:\n'{negative_feedback}'")
print(f"\n[=] Automated Response:\n'{negative_response.strip()}'")
