from enum import Enum
from mesa import Agent

class State(Enum):
    SUSCEPTIBLE = 0            # Users not yet exposed to misinformation
    MISINFORMED_USER = 1       # Users who believe and spread misinformation
    RESISTANT = 2              # Users resistant to misinformation
    FACT_CHECKER = 3           # Users who actively fact-check misinformation
    MISINFORMATION_BOT = 4     # First strain of misinformation bots
    MISINFORMATION_BOT_2 = 5   # Second strain of misinformation bots
    MISINFORMATION_BOT_3 = 6   # Third strain of misinformation bots


class VirusAgent(Agent):
    """Defines individual agents and their interactions."""

    def __init__(self, model, initial_state, virus_spread_chance, virus_check_frequency, resistance_duration, name=None):
        super().__init__(model)
        self.state = initial_state
        self.virus_spread_chance = virus_spread_chance
        self.virus_check_frequency = virus_check_frequency
        self.influence_chance = virus_check_frequency * 0.7
        self.resistance_duration = resistance_duration
        self.resistance_counter = 0
        self.infecting_strain = None  # Track the misinformation strain
        self.name = name  # Name for specific agents like "Misinformed User 1"

    def try_to_infect_neighbors(self):
        """Infect susceptible neighbors with the misinformation strain of the infecting agent."""
        neighbors_nodes = self.model.grid.get_neighborhood(self.pos, include_center=False)
        susceptible_neighbors = [
            agent for agent in self.model.grid.get_cell_list_contents(neighbors_nodes) if agent.state == State.SUSCEPTIBLE
        ]

        for a in susceptible_neighbors:
            if self.random.random() < self.virus_spread_chance:
                a.state = State.MISINFORMED_USER
                
                # Assign the infection strain based on the infector
                if self.state in [State.MISINFORMATION_BOT, State.MISINFORMATION_BOT_2, State.MISINFORMATION_BOT_3]:
                    self.model.botInfected += 1
                    a.infecting_strain = self.state  # Track which bot strain infected the user
                elif self.state == State.MISINFORMED_USER and self.infecting_strain:
                    self.model.userInfected += 1
                    a.infecting_strain = self.infecting_strain  # Maintain strain lineage

    def try_fact_check(self):
        """Fact-check nearby misinformed users and turn them resistant."""
        neighbors_nodes = self.model.grid.get_neighborhood(self.pos, include_center=False)
        misinformed_neighbors = [
            agent for agent in self.model.grid.get_cell_list_contents(neighbors_nodes) if agent.state == State.MISINFORMED_USER
        ]

        for a in misinformed_neighbors:
            if self.random.random() < self.virus_check_frequency:
                a.state = State.RESISTANT
                a.resistance_counter = self.resistance_duration

    def try_influence_misinformed(self):
        """Resistant agents attempt to influence misinformed neighbors."""
        neighbors_nodes = self.model.grid.get_neighborhood(self.pos, include_center=False)
        misinformed_neighbors = [
            agent for agent in self.model.grid.get_cell_list_contents(neighbors_nodes) if agent.state == State.MISINFORMED_USER
        ]

        for a in misinformed_neighbors:
            if self.random.random() < self.influence_chance:
                a.state = State.RESISTANT
                a.resistance_counter = self.resistance_duration

    def step(self):
        """Defines the behavior of each agent in a single simulation step."""
        if self.state in [State.MISINFORMED_USER, State.MISINFORMATION_BOT, State.MISINFORMATION_BOT_2, State.MISINFORMATION_BOT_3]:
            self.try_to_infect_neighbors()
        elif self.state == State.FACT_CHECKER:
            self.try_fact_check()
        elif self.state == State.RESISTANT:
            self.try_influence_misinformed()
            self.resistance_counter -= 1
            if self.resistance_counter <= 0:
                self.state = State.SUSCEPTIBLE  # Resistant users can become susceptible again
