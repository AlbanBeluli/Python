import openai

#Insert you API key here
openai.api_key = "YOUR_API_KEY" 
messages = []
system_msg = input("What type of chatbot would you like to create?\nFor Example: Coding Assistant\n ")
messages.append({"role": "system", "content": system_msg})

print("Say hello to your new assistant:\n")
while input != "quit()": 
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
