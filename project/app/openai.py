import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")



def chat3turbo(prompt, transcript):
    
    user = prompt['user_message']
    system = prompt['system_message']
    
    transcript_string = ""
    for message in transcript:
        role = message['role']
        content = message['content']
        transcript_string += f"{role}: {content}\n"
    print(transcript_string)
    
    if len(transcript) >1:
        prescript = "You've been having the following conversation with the user: " + transcript_string + " this is the user's next question: "
        user = prescript + user
        print("longer transcript.  New prompt: ")
        print(user)
    
    print("completion running")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=[
        {"role": "user", "content": user},
        {"role": "system", "content": system}
        ]  
    )

    response = completion.choices[0].message.content
    
    
    return response

def chat4(prompt, transcript):
    user = prompt['user_message']
    system = prompt['system_message']
    
    transcript_string = ""
    for message in transcript:
        role = message['role']
        content = message['content']
        transcript_string += f"{role}: {content}\n"
    print(transcript_string)
    
    if len(transcript) >1:
        prescript = "You've been having the following conversation with the user: " + transcript_string + " this is the user's next question: "
        user = prescript + user
        print("longer transcript.  New prompt: ")
        print(user)
        
        
    print("chat4 ran")
    completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": user},
        {"role": "system", "content": system}
    ]  
    )
    
    response = completion.choices[0].message.content
    print("response in gpt4")
    print(response)
    return response