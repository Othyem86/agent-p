import sys
import os
from dotenv import load_dotenv
from google import genai

def main():
    args = sys.argv[1:]

    if not args:
        print("AI Code Assistant\n")
        print('Usage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    prompt = " ".join(args)


    load_dotenv()
    ai_api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=ai_api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=prompt
    )
    
    # Print results
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()
