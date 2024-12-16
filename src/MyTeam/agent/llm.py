import os
from autogen import ConversableAgent


def init_ConversableAgent(llm_type, llm_name, agent_name, system_message):
    assert llm_type in ['ollama', 'openai']
    if llm_type == 'ollama':
        config_list = [{
            "model": llm_name,
            "base_url": "http://localhost:11434/v1",
            "api_key": "ollama",   
        }]
    else:  # llm_type == 'openai'
        config_list = [{
            "model": llm_name,
            "api_key": os.environ["OPENAI_API_KEY"],
        }]
    agent = ConversableAgent(
        name=agent_name,
        system_message=system_message,
        llm_config={"config_list": config_list}
    )
    return agent
