from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests

Builder.load_file('frontend.kv')

class FirstScreen(Screen):
    def get_image_link(self):
        # Get user query from TextInput
        query = self.manager.current_screen.ids.user_query.text
        # Get wikipedia page and the first image link
        page = wikipedia.page(query)
        image_link = page.images[0]
        return image_link
    def download_image(self):    
        # Download the image
        headers = {'User-agent': 'Mozilla/5.0'}
        req = requests.get(self.get_image_link(), headers=headers)
        imagepath = 'files/image.jpg'
        with open(imagepath, 'wb') as file:
            file.write(req.content)
        # Set the image in the Image widget
        return imagepath
    def set_image(self):
        self.manager.current_screen.ids.img.source = self.download_image()

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    
    def build(self):
        return RootWidget()
    
MainApp().run()