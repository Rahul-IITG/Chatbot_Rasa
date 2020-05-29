# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
from database_api import DatabaseAPI


class ActionCustomFallback(Action):
	def name(self) -> Text:
		return "custom_fallback_action"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		dispatcher.utter_message("So sorry, I am unable to understand what you said, please contact the support team using the mentioned link for further assistantance. Link: https://procurement.mastercard.com")
		
		return [UserUtteranceReverted()]



class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        # the session should begin with a `session_started` event
        dispatcher.utter_message("Hi Varrick, I'm Zhu Lee.")
        events = [SessionStarted()]
        
        # any slots that should be carried over should come after the
        # `session_started` event
        # an `action_listen` should be added at the end as a user message follows
        events.append(ActionExecuted("action_listen"))

        return events
# class ActionCustomFallback(Action):
# 	def name(self) -> Text:
# 		return "action_default_ask_affirmation"

# 	def run(self, dispatcher: CollectingDispatcher,
# 			tracker: Tracker,
# 			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

# 		dispatcher.utter_message("Can you please rephrase it. i did not understand clearly")
		
# 		return [UserUtteranceReverted()]

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

class ActionSetAnswer1yes(Action):
	def name(self) -> Text:
		return "action_set_answer1_yes"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		
		return [SlotSet("answer1",True)]

class ActionSetAnswer1no(Action):
	def name(self) -> Text:
		return "action_set_answer1_no"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		
		return [SlotSet("answer1",False)]

class ActionSetAnswer2yes(Action):
	def name(self) -> Text:
		return "action_set_answer2_yes"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		
		return [SlotSet("answer2",True)]

class ActionSetAnswer2no(Action):
	def name(self) -> Text:
		return "action_set_answer2_no"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		
		return [SlotSet("answer2",False)]

class ActionSetAnswer3yes(Action):
	def name(self) -> Text:
		return "action_set_answer3_yes"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		
		return [SlotSet("answer3",True)]

class ActionSetAnswer3no(Action):
	def name(self) -> Text:
		return "action_set_answer3_no"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		
		return [SlotSet("answer3",False)]

class ActionSetAnswer4yes(Action):
	def name(self) -> Text:
		return "action_set_answer4_yes"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		
		return [SlotSet("answer4",True)]

class ActionSetAnswer4no(Action):
	def name(self) -> Text:
		return "action_set_answer4_no"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		
		return [SlotSet("answer4",False)]

class ActionSetAnswer5yes(Action):
	def name(self) -> Text:
		return "action_set_answer5_yes"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		
		return [SlotSet("answer5",True)]

class ActionSetAnswer5no(Action):
	def name(self) -> Text:
		return "action_set_answer5_no"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		
		return [SlotSet("answer5",False)]


class ActionSetAnswer6yes(Action):
	def name(self) -> Text:
		return "action_set_answer6_yes"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		
		return [SlotSet("answer6",True)]

class ActionSetAnswer6no(Action):
	def name(self) -> Text:
		return "action_set_answer6_no"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		
		return [SlotSet("answer6",False)]


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

class ActionDatabase99(Action):

	def name(self) -> Text:
		return "action_database_99"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		e_id="exxxxxx"
		output="99"
		user_name="Varrik"

		DatabaseAPI(e_id,user_name,output)

		return []


class ActionDatabase0(Action):

	def name(self) -> Text:
		return "action_database_0"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		e_id = "exxxxxx"
		output = "0"
		user_name = "Varrik"

		DatabaseAPI(e_id, user_name, output)

		return []


class ActionDatabase1(Action):

	def name(self) -> Text:
		return "action_database_1"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		e_id = "exxxxxx"
		output = "1"
		user_name = "Varrik"

		DatabaseAPI(e_id, user_name, output)

		return []