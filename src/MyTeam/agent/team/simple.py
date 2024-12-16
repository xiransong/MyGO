from MyTeam.agent import AgentSystem, init_ConversableAgent


class Solo(AgentSystem):

    def __init__(self, config, data):
        super().__init__(config, data)


class TwoAgent(AgentSystem):

    def __init__(self, config, data):
        self.Alice = init_ConversableAgent(
            llm_type="ollama", llm_name="llama3.2", 
            agent_name="Alice", system_message="", 
        )
        self.Bob = init_ConversableAgent(
            llm_type="ollama", llm_name="phi3", 
            agent_name="Bob", system_message="", 
        )

    def get_reply(self, problem):
        chat_result = self.Alice.initiate_chat(
            recipient=self.Bob,
            message="What is triangle inequality?",
            summary_method=None,
            max_turns=2,
        )
        reply = self.Alice.generate_reply(messages=chat_result.chat_history)
        return reply


class GroupChat(AgentSystem):

    def __init__(self, config, data):
        super().__init__(config, data)
 