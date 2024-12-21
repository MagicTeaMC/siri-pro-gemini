import google.generativeai as genai
from load_config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

async def generate_response(history, system_prompt):
    print("# [llm.py] [generate_response] Generating Response...")
    try:
        message = model.messages.create(
            max_tokens=1024,
            system=system_prompt,
            messages=history
        )
        
        response = message.content[0].text
        print("# [llm.py] [generate_response] Response Generated: " + response)
        return response
    except Exception as e:
        print("# [llm.py] [generate_response] Error: " + str(e))
        return "[ERROR] " + str(e)