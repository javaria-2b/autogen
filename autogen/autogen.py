llm_config = {"model": "gpt-3.5-turbo"}
import autogen

task = '''
        Write a python code which will get 2 numbers as the input from the user and add them.
       '''


coder = autogen.AssistantAgent(
    name="Coder",
    system_message="You are a Code. You write accurate and concise " 
        "code (with title) on given topics. You must polish your "
        "coding skills based on the feedback you receive and give a refined "
        "version. Only return your final work without additional comments.",
    llm_config=llm_config,
)


reply = coder.generate_reply(messages=[{"content": task, "role": "user"}])


print(reply)


critic = autogen.AssistantAgent(
    name="Critic",
    is_termination_msg=lambda x: x.get("content", "").find("TERMINATE") >= 0,
    llm_config=llm_config,
    system_message="You are a critic. You review the work of "
                "the coder and provide constructive "
                "feedback to help improve the quality of the content.",
)


res = critic.initiate_chat(
    recipient=coder,
    message=task,
    max_turns=2,
    summary_method="last_msg"
)


res = critic.initiate_chat(
    recipient=coder,
    message=task,
    max_turns=2,
    summary_method="last_msg"
)



print(res.summary)


