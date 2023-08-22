from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager

class MedicationPromptScreen(Screen):
    def set_reminder(self):
        # Retrieve medication details from user input
        medication_name = self.ids.medication_name_input.text
        medication_dosage = self.ids.medication_dosage_input.text
        medication_time = self.ids.medication_time_input.text

        # Display the reminder as a popup
        reminder_content = f"Take {medication_dosage} of {medication_name} at {medication_time}."
        reminder_popup = Popup(title="Reminder", content=Label(text=reminder_content),
                               size_hint=(None, None), size=(400, 200))
        reminder_popup.open()

class DashboardScreen(Screen):
    def show_reminders(self):
        # Implement the functionality for the Reminders option
        reminders_content = "You have the following reminders:\n1. Doctor's appointment at 10 AM\n2. Take medicine at 3 PM"
        reminders_popup = Popup(title='Reminders', content=Label(text=reminders_content),
                                size_hint=(None, None), size=(400, 200))
        reminders_popup.open()

    def show_diet_plan(self):
        # Implement the functionality for the Diet Plan option
        diet_plan_content = "Your Diet Plan for today:\nBreakfast: Oatmeal\nLunch: Grilled Chicken Salad\nDinner: Steamed Vegetables"
        diet_plan_popup = Popup(title='Diet Plan', content=Label(text=diet_plan_content),
                                size_hint=(None, None), size=(400, 200))
        diet_plan_popup.open()

    def show_settings(self):
        # Implement the functionality for the Settings option
        settings_content = "Settings functionality will be implemented."
        settings_popup = Popup(title='Settings', content=Label(text=settings_content),
                               size_hint=(None, None), size=(400, 200))
        settings_popup.open()

    def call_doctor(self):
        # Implement the functionality for the Call option
        call_content = "Calling Doctor..."
        call_popup = Popup(title='Call', content=Label(text=call_content),
                           size_hint=(None, None), size=(400, 200))
        call_popup.open()

class MainScreen(Screen):
    pass

class MeditronicsApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()

        # Create the main screen
        main_screen = MainScreen(name='main')
        sm.add_widget(main_screen)

        # Create the medication prompt screen
        medication_prompt_screen = MedicationPromptScreen(name='medication_prompt')
        sm.add_widget(medication_prompt_screen)

        # Create the dashboard screen
        dashboard_screen = DashboardScreen(name='dashboard')
        sm.add_widget(dashboard_screen)

        return sm

if __name__ == '__main__':
    MeditronicsApp().run()