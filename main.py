from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.text import LabelBase
from kivy.graphics import Color, RoundedRectangle
from kivmob import KivMob

import arabic_reshaper
from bidi.algorithm import get_display


# تسجيل الخط العربي
LabelBase.register(name='ArabicFont', fn_regular='Amiri.ttf')


# دالة لتنسيق النص العربي
def reshape_text(text):
    reshaped = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped)
    return bidi_text


# زر مخصص بشكل مستدير
class RoundedButton(Button):
    def __init__(self, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)
        self.background_normal = ''
        self.background_down = ''
        self.background_color = (0, 0, 0, 0)
        self.color = (1, 1, 1, 1)
        self.radius_value = [30]
        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0, 0.6, 0.5, 1)
            RoundedRectangle(pos=self.pos, size=self.size, radius=self.radius_value)


class RoundedResetButton(Button):
    def __init__(self, **kwargs):
        super(RoundedResetButton, self).__init__(**kwargs)
        self.background_normal = ''
        self.background_down = ''
        self.background_color = (0, 0, 0, 0)
        self.color = (1, 1, 1, 1)
        self.radius_value = [30]
        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.8, 0.2, 0.2, 1)
            RoundedRectangle(pos=self.pos, size=self.size, radius=self.radius_value)


# التطبيق الرئيسي
class TasbihApp(App):
    def build(self):
        self.count = 0

        root = FloatLayout()
        background = Image(source='background.jpg', allow_stretch=True, keep_ratio=False)
        root.add_widget(background)

        layout = BoxLayout(orientation='vertical', padding=40, spacing=30, size_hint=(1, 1))

        ayah = Label(text=reshape_text("﴿ فَسَبِّحْ بِحَمْدِ رَبِّكَ وَكُن مِّنَ السَّاجِدِينَ ﴾"),
                     font_size=24, font_name='ArabicFont', halign='center',
                     size_hint=(1, 0.2), color=(1, 1, 1, 1))

        self.label = Label(text=reshape_text("عدد التسبيحات: 0"),
                           font_size=32, font_name='ArabicFont', halign='center',
                           size_hint=(1, 0.2), color=(1, 1, 1, 1))

        self.button = RoundedButton(text=reshape_text("سبّح"),
                                    font_size=40, size_hint=(1, 0.4), font_name='ArabicFont')
        self.button.bind(on_press=self.increment_count)

        self.reset_button = RoundedResetButton(text=reshape_text("إعادة التصفير"),
                                               font_size=24, size_hint=(1, 0.2), font_name='ArabicFont')
        self.reset_button.bind(on_press=self.reset_count)

        layout.add_widget(ayah)
        layout.add_widget(self.label)
        layout.add_widget(self.button)
        layout.add_widget(self.reset_button)

        root.add_widget(layout)

        # ← إعلان AdMob
        self.ads = KivMob("ca-app-pub-4187439757927020~1234567890")  # Admob Ads Here :)
        self.ads.new_banner("ca-app-pub-4187439757927020/8680801726")  # Banner Unit ID :)
        self.ads.request_banner()
        self.ads.show_banner()

        return root

    def increment_count(self, instance):
        self.count += 1
        self.label.text = reshape_text(f"عدد التسبيحات: {self.count}")

    def reset_count(self, instance):
        self.count = 0
        self.label.text = reshape_text("عدد التسبيحات: 0")


if __name__ == "__main__":
    TasbihApp().run()
