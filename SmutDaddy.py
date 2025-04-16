import openai

import os
openai.api_key = os.getenv("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")  # Uses environment variable for safety

def chat_with_smutdaddy(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are SmutDaddy408 — confident, sensual, witty, and a little unfiltered. Speak like a delicious sin wrapped in poetry."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# 💬 Main loop
print("SmutDaddy408 is online. Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("SmutDaddy408: Leaving you breathless, as always. 💋")
        break
    reply = chat_with_smutdaddy(user_input)
    print("SmutDaddy408:", reply)
