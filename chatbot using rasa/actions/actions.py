from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Tracker
from rasa_sdk.types import DomainDict

class ActionSetName(Action):

    def name(self) -> str:
        return "action_set_name"

    def run(self, dispatcher, tracker, domain):

        user_name = tracker.get_slot("name")

        if user_name:
            dispatcher.utter_message(
                text=f"Nice to meet you {user_name} 🚀"
            )
        else:
            dispatcher.utter_message(
                text="I didn't catch your name."
            )

        return []