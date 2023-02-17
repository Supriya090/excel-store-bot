# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType
from data_store_read import DataStore


class ActionSaveData(Action):

    def name(self) -> Text:
        return "action_save_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        DataStore(tracker.get_slot("name"), 
            tracker.get_slot("number"), 
            tracker.get_slot("email"), 
            tracker.get_slot("occupation"))
        dispatcher.utter_message(text="Data stored successfully!")

        return []

class FormDataCollect():
    def name(self) -> Text:
        return "information_form"

    @staticmethod 
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["name","number","email", "occupation"]

    def submit(self, dispatcher:"CollectingDispatcher", tracker:"Tracker", domain: Dict[Text, Any]) -> List[EventType]:
        dispatcher.utter_message("Here is the information that you provided. Do you want to save it? \nName: {0}, \nMobile Number: {1}, \nEmail Address: {2}, \nOccupation: {3}".format(
            tracker.get_slot("name"), 
            tracker.get_slot("number"), 
            tracker.get_slot("email"), 
            tracker.get_slot("occupation")))
        return []
