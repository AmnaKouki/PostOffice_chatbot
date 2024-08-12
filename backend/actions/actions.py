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
        
        dispatcher.utter_message(text="أوقات عمل البريد التونسي في الفترة ما بين 1 سبتمبر و 30 جوان  ")
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
        
        dispatcher.utter_message(text="أوقات عمل البريد التونسي في الفترة ما بين 1 جويلية و 31 أوت 🍉⛱️")
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
        dispatcher.utter_message(text=" نظام العمل بالبريد التونسي يتبدل حسب التوقيت الإداري 🕒\n\n شنوا التوقيت الي تحب تعرفو ؟  ")
        dispatcher.utter_message(json_message= jsonObj)
        
        return []
    
    
# what to say when asked about steps to send packages
class ActionAskAskHowToSendPackages(Action):

    def name(self) -> Text:
        return "action_ask_how_to_send_packages"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        jsonObj= {
            "stepsToSendPackages": True,
            "steps": [
                {
                "step": "تحضير الطرد 📦 ",
                "description": "لازم الطرد يكون مغلف مليح وتكون إستعملت مستلزمات التغليف إلي يقدمها مركز البريد التونسي"
                },
                {
                "step": "تعمير الإستمارة 📋",
                "description": "مركز البريد يعطيك أوراق لازم تعمرها بوضوح. تأكد من سلامة البيانات خاصة الإسم و العنوان و رقم الهاتف"
                },
                {
                "step": "إختار نوع خدمة التوصيل 👈",
                "description": "البريد السريع يقدملك برشة خدمات للتوصيل (توصيل داخل تونس, خارج تونس, ذهاب و إياب,...)"
                },
                {
                "step": "دفع الرسوم 💰",
                "description": "عون البريد باش يقوم بوزن الطرد و تقييم الكلفة. تنجم تخلص كاش 💸 أو عن طريق ال كارطة  💳"
                },
                {
                
                "step": "الحصول على رقم التتبع ✅",
                "description": "باش تستلم ورقة مكتوب عليها رقم التتبع. هو رقم باش يخليك قادر على تتبع الطرد متاعك وين وصل عن طريق الإنترنات "
                },
                {
                "step": "متابعة الطرد حتى التسليم 📌",
                "description": "توة الطرد متاعك في الحفظ و في الأمان مع البريد التونسي 😊 إتنجم إتبع رحلة الطرد متاعك على الإنترنات حتى توفى عملية التسليم."
                }
            ]
            }
        dispatcher.utter_message(text="📦 باش إتنجم تبعث أي حاجة على البريد السريع, لازمك إتبع الخطوات هاذي :")
        dispatcher.utter_message(json_message= jsonObj)
        
        return []
    

# answer the button for 'sending package conditions'
class ActionAskAskHowToSendPackages(Action):

    def name(self) -> Text:
        return "action_send_package_conditions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        jsonObj= {
            "list": True,
            "options": [
                "تأكد من تعبئة البيانات الشخصية الخاصة بك بشكل صحيح (خاصة العنوان و رقم الهاتف)",
                "لازم تستعمل معدات التغليف إلي يقدمها البريد السريع باش تحافظ على سلامة المبعوثات.",
                "الميزان لازم ما يفوتش الحد الأقصى ( 30 كغ )",
                "تجنب إرسال البضائع الممنوعة",
                "القوارير و الأوعية لازم تكون مسكرة بالباهي"
            ]
        
            
            }
        dispatcher.utter_message(text="باش اتنجم تبعث حاجة على البريد السريع, ثما شروط لازم تعرفها قبل:")
        dispatcher.utter_message(json_message= jsonObj)
        
        return []
    
    

class ActionRapidPosteServices(Action):

    def name(self) -> Text:
        return "action_give_rapid_poste_services"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        jsonObj= {
            "buttons": True,
            "options": [
                        ["تتبع الطرود البريدية 📦","نحب نعرف وين وصل الـ Colis متاعي"],
                        ["شروط الإيداع 📋","شنوا الشروط باش نبعث Colis"],
                        ["  كيفية إرسال الطرود ❓","كيفاش إنجم نبعث طرد ؟"],
                    ]
        
            
            }
        dispatcher.utter_message(text="البريد السريع يقدم لك برشة خدمات سريعة و موثوقة لتوصيل الطرود و البضائع داخل تونس و خارجها. شنوا تحب تعرف بالضبط ؟")
        dispatcher.utter_message(json_message= jsonObj)
        
        return []
    
