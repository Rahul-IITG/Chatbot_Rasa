# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from database_api import DatabaseAPI
from rasa_sdk.events import UserUtteranceReverted

class ActionSetAnswersNull(Action):
	def name(self) -> Text:
		return "action_set_answers_null"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		# SlotSet("answer1",value=None)
		# SlotSet("answer2",value=None)
		# SlotSet("answer3",value=None)
		# SlotSet("answer4",value=None)
		# SlotSet("answer5",value=None)
		
		return [SlotSet("answer6",value=None)]

class ActionAnswer1Submit(Action):
	def name(self) -> Text:
		return "action_answer1_submit"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		return [SlotSet("answer1",tracker.latest_message['text'])]

class ActionAnswer2Submit(Action):
	def name(self) -> Text:
		return "action_answer2_submit"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		return [SlotSet("answer2",tracker.latest_message['text'])]
class ActionAnswer3Submit(Action):
	def name(self) -> Text:
		return "action_answer3_submit"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		return [SlotSet("answer3",tracker.latest_message['text'])]
class ActionAnswer4Submit(Action):
	def name(self) -> Text:
		return "action_answer4_submit"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		return [SlotSet("answer4",tracker.latest_message['text'])]
class ActionAnswer5Submit(Action):
	def name(self) -> Text:
		return "action_answer5_submit"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		return [SlotSet("answer5",tracker.latest_message['text'])]
class ActionAnswer6Submit(Action):
	def name(self) -> Text:
		return "action_answer6_submit"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		return [SlotSet("answer6",tracker.latest_message['text'])]

class ActionHelloWorld(Action):

	def name(self) -> Text:
		return "action_hello_world"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		Link="https://www.fb.com/"
		dispatcher.utter_template("utter_99", Tracker, link=Link)

		return []

class ActionDatabase(Action):

	def name(self) -> Text:
		return "action_database"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		e_id="exxxxxx"
		user_name="Buzz"
		output=tracker.get_slot('output')

		dispatcher.utter_message("This is {}".format(output))
		#DatabaseAPI(e_id,user_name,output)***

		return []

class ActionCustomFallback(Action):

	def name(self) -> Text:
		return "custom_fallback_action"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		dispatcher.utter_message("This is custom fallback")

		return [UserUtteranceReverted()]