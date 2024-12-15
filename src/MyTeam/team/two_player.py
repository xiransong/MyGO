from autogen import GroupChat

from MyTeam.team import Team



class TwoPlayer(Team):

    def __init__(self, config, data, agent_list):
        super().__init__(config, data, agent_list)
        self.group_chat = GroupChat(
            agents=agent_list,
            messages=[],
            max_round=3,
        )

    def solve_a_problem(self, problem):
        pass
