import os
from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()
    ai_api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=ai_api_key)

    ai_model = "gemini-2.0-flash-001"
    prompt = "Why are AI agents good at coding? Use one paragraph maximum."

    response = client.models.generate_content(model=ai_model, contents=prompt)
    
    # Print results
    print("Hello from agent-p!")
    print()
    print("PROMPT")
    print(prompt)
    print()
    print("RESPONSE")
    print()
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
