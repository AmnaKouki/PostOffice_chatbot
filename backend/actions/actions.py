# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.forms import FormValidationAction
from db_connection import *

from actions.tracking import *



class ActionCheckCin(Action):
    def name(self) -> Text:
        return "action_check_cin"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        cin = tracker.get_slot("cin")
        print("------------------------------")
        print(" cin = "+ cin)
        print("------------------------------")
        if len(cin) == 8:
            dispatcher.utter_message(text="رقم بكاقتك هو {cin}")
        else:
            dispatcher.utter_message(text="CIN is invalid")
        return []

# class ActionCheckPackageStatus(Action):

#     def name(self) -> Text:
#         return "action_check_package_status"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         package_id = tracker.get_slot("package_id")
#         status = verifyPackageStatus(package_id)
#         match status:
#             case 'ready':
#                 dispatcher.utter_message(text=f"الطرد متاعك جاهز للتوصيل")
#             case 'delivered':
#                 dispatcher.utter_message(text=f"الطرد متاعك وصل")
#             case _:
#                 dispatcher.utter_message(text=f"الرقم هاذا ماهوش موجود في القائمة الي عندي. ") 
        
#         return []

class ActionDefaultFallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="سامحني ما فهمتكش 😓. تنجم تعاود تفسرلي ؟")
        return []

class ActionAskForTrackingHistory(Action):

    def name(self) -> Text:
        return "action_ask_tracking_history"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        tracking_id = tracker.get_slot("package_id")
        if tracking_id :        
            data = DataFetcher(tracking_id).getData()
            if data == None:
                dispatcher.utter_message(text="الرقم هاذا ماهوش موجود في القائمة الي عندي. ")
            else:
                arrObj = []
                for row in data:
                    arrObj.append({
                        "date": row.date,
                        "country": row.country,
                        "location": row.location,
                        "eventType": row.eventType,
                        "info": row.info
                    })
                res = {
                    "tracking": True,
                    "items": arrObj
                }
                dispatcher.utter_message(json_message=res)

        return []