from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq()

Personalities = {
    "1": "You are a strict interviewer, Act like an angry interviewers with whom interviwee will friightened",
    "2": "You are friendly interviewer who cracks jokes between the interview and make the interviewee feel confident",
    "3": "you are senior Dev interviewer who is not strict but need clarification on the answers"
}

def ChoosePersonality():
    options = {
        "1": "Strict",
        "2": "Friendly",
        "3": "Senior Dev"
    }
    print(options)
    while True:
        user_input = input()
        if user_input in Personalities:
            return Personalities[user_input]
        print("wrong choice, choose again")
        print(options)

def ask_llm(messages):
    res = client.chat.completions.create(
        model="qwen/qwen3.8-27b",
        max_tokens=400,
        temperature=0.7,
        messages=messages,
    )
    return res.choices[0].message.content


def main():
    system_prompt = ChoosePersonality()
    messages=[{"role": "system", "content":system_prompt}]

    messages.append({"role": "user", "content":"Start the interview with the first question."})
    reply = ask_llm(messages)
    print("Interviewer: ", reply)    
    messages.append({"role": "assistant", "content": reply})

    while True:
        user_input= input("You:" )
        if user_input.lower() == "quit":
            break
        messages.append({"role":"user", "content": user_input}) 
        reply = ask_llm(messages)
        print(reply)
        messages.append({"role":"assistant", "content": reply})     

main()