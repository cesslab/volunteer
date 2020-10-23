from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = "Your name here"

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = "volunteer"
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    volunteer_found = models.BooleanField(initial=False)


class Player(BasePlayer):
    volunteered = models.BooleanField(initial=False)

    def live_volunteer(self, data):
        self.group.volunteer_found = True
        self.volunteered = True
        print(f"Message {data} received from {self.id_in_group}")
        return {0: {"id_in_group": self.id_in_group}}