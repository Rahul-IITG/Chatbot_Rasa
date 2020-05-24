#config

policies:
  - name: TwoStageFallbackPolicy
    nlu_threshold: 0.3
    core_threshold: 0.3
    fallback_core_action_name: "custom_fallback_action"
    fallback_nlu_action_name: "custom_fallback_action"
    deny_suggestion_intent_name: "out_of_scope"

#actions.py

class ActionCustomFallback(Action):
	def name(self) -> Text:
		return "custom_fallback_action"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		dispatcher.utter_message("Please contact the support team")
		
		return [UserUtteranceReverted]

	class ActionCustomFallback(Action):
	def name(self) -> Text:
		return "action_default_ask_affirmation"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		dispatcher.utter_message(template: "utter_ask_affirmation")
		
		return [UserUtteranceReverted()]


	##stories


	#bot_challenge
	*bot_challenge
	- custom_fallback_action


	##domain

	templates:
		utter_ask_affirmation:
			- text: Did you mean?
		utter_ask_rephrase:
			- text: Please rephrase again

	actions:
		- custom_fallback_action
		-action_default_ask_affirmation