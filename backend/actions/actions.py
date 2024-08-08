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


from actions.tracking import *




# from db_connection import *


# using data base connection
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
    
    

class ActionAskForWinterWorkingHours(Action):

    def name(self) -> Text:
        return "action_ask_for_winter_working_hours"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        jsonObj = {
            "workHoursTable" : True,
            "workingHours": 
            [
                {
                "day": "الإثنين - الجمعة :",
                "time": "08h - 12h00 | 14h30 - 17h00"
                },
                {
                "day": "السبت:",
                "time": "09h - 12h15"
                }
            ] 
        }
        
        dispatcher.utter_message(text="البريد التونسي يستعمل الأوقات هاذي في الفترة ما بين 1 سبتمر حتى 30 جوان⏰ ")
        dispatcher.utter_message(json_message= jsonObj)
        
        return []


class ActionAskForSummerWorkingHours(Action):

    def name(self) -> Text:
        return "action_ask_for_summer_working_hours"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        jsonObj = {
            "workHoursTable" : True,
            "workingHours": 
            [
                {
                "day": "الإثنين - الخميس :",
                "time": "07h30 - 13h30"
                },
                {
                "day": "الجمعة  :",
                "time": "07h30 - 12h30"
                },
                {
                "day": "السبت:",
                "time": "09h - 12h15"
                }
            ]
        }
        
        dispatcher.utter_message(text="البريد التونسي يستعمل الأوقات هاذي في الفترة ما بين 1 جويلية حتى 31 أوت🍉⛱️ ")
        dispatcher.utter_message(json_message= jsonObj)
        
        return []


class ActionAskForSummerWorkingHours(Action):

    def name(self) -> Text:
        return "action_ask_for_poste_office_work_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        jsonObj= {
            "workHoursButtons": True,
            }
        dispatcher.utter_message(text=" نظام العمل بالبريد التونسي يتبدل حسب التوقيت الإداري ⌚.\n\n شنوة التوقيت الي تحب تعرفو ؟  ")
        dispatcher.utter_message(json_message= jsonObj)
        
        return []