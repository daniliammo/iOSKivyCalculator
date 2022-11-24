import os
from kivy.config import Config  # Должен импортироваться первым
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from SettingsJsonReader import SettingsReader
from kivy.lang.builder import Builder

Config.set("graphics", "resizable", '1')
Config.set('graphics', 'width', '1800')  # 4:3
Config.set('graphics', 'height', '900')
Config.write()

# Radius Settings
class NullGrayRoundedButton(Button):
    radiust = str(SettingsReader.lineRadius)
    GrayRadius = [eval(radiust)]


class GrayRoundedButton(Button):
    radiust = str(SettingsReader.lineRadius)
    GrayRadius = [eval(radiust)]


class LightGrayRoundedButton(Button):
    radiust = str(SettingsReader.lineRadius)
    radiustor = [eval(radiust)]


class OrangeRoundedButton(Button):
    OrangeRadius = str(SettingsReader.lineRadius)
    OrangeRadius = [eval(OrangeRadius)]


class LightSettingsRoundedButton(Button):
    radiust = str(SettingsReader.lineRadius)
    radiustor = [eval(radiust)]


# Настройки
class SettingsWindow(Popup):

    __version__ = '1.9'

    # Button Settings Size
    SizeSettingsButton = str(SettingsReader.SButtonSize)
    SizeSettingsButtonX = str(SettingsReader.SButtonSizeX)

    # Orange, Light Gray, Gray buttons font size
    ButtonFontSize = int(SettingsReader.SettingButton)

    # Padding
    PadyIng = str(SettingsReader.PaddingJson).replace(']', '').replace('[', '')

    # Ellipse or RoundedRectangle
    FalseOrTrue = bool(SettingsReader.boolIsEllipse)

    # Read Popup Resolution
    UIP2Resolution = int(SettingsReader.PopupResolution)

    UIResolutionfortxtin = int(SettingsReader.PopupResolutionX)
    UIResolutionx = UIP2Resolution, UIResolutionfortxtin

    # Read Settings Font Size

    StngsFontSize = int(SettingsReader.SettingsFontSize)

    # Read Radius Value

    ilineRadius = int(SettingsReader.lineRadius)

    # Read Answer Font Size
    setlineb = int(SettingsReader.AnsFontSize)

    FirstInt = int(SettingsReader.btnsize_evalx)

    # FUNC

    def WriteSettings(self):

        EllipseX = self.ids.EllipseCheckingBox.active
        ReplacePaddingList = '[' + self.ids.SetPopupSizeVZO.text + ']'

        if EllipseX is True:
            EllipseV = str(EllipseX)
            EllipseZ = EllipseV.replace('T', 't')

        if EllipseX is False:
            EllipseV = str(EllipseX)
            EllipseZ = EllipseV.replace('F', 'f')

        os.remove('settings.json')
        sFile = open('settings.json', 'w')
        sFile.write('{\n    "settings": [\n        {\n            "ISEllipse": ' + EllipseZ + ',\n            '
                    '"SettingsButtonSize": ' + self.ids.SettingsButtonSizeTxtInput.text + ','
                    '\n            "SettingsButtonSizeX": ' + self.ids.SettingsButtonSizeXTxtInput.text + ',\n            '
                    '"SettingsButton": ' + self.ids.SetFontButton.text + ',\n            "PopupResolution": ' + self.ids.SetPopupSizeX.text +
                    ',\n            "PopupResolutionX": ' + self.ids.SetPopupSize.text +
                    ''
                    ',\n            "Radius": ' + self.ids.SetFontR.text +
                    ',\n'
                    '            "SettingsFontSize": ' + self.ids.TIFontSizeSettings.text +
                    ''
                    ',\n            "Answer-Font-Size": ' + self.ids.SetFontAnswer.text + ',\n'
                    '            "EmptyBoxLayoutSize": '
                    '35,\n '
                    '           "Settings-Button-Size-Float": 125,\n'
                    '            "Settings-Button-Size-Float-X": 35,\n            '
                    '"Язык": "🇷🇺",\n            "Padding": ' + ReplacePaddingList + '\n        }\n    ]\n}'
                                                                                               '\n')
        sFile.close()
        self.dismiss()

# MAIN


class CalcGridLayout(GridLayout):

    # Padding
    PadyIng = list(SettingsReader.PaddingJson)

    # Button Settings Size
    SizeSettingsButton = int(SettingsReader.SButtonSize)
    SizeXSettingsButton = int(SettingsReader.SButtonSizeX)

    # Settings Button Font Size calculate
    FontSizeSettingsButton = SizeXSettingsButton * SizeSettingsButton
    FontSizeSettingsButtonX = FontSizeSettingsButton // SizeSettingsButton // 1.5
    # print(FontSizeSettingsButtonX, 'Font Size ==', FontSizeSettingsButtonX)

    # BoxLayout Height bxl

    SetSizeEmptyBox = int(SettingsReader.EmptyBoxLsize)

    # Answer Font Size

    setline = int(SettingsReader.AnsFontSize)
    setlineb = int(SettingsReader.SettingButton)

    # FUNC

    def positive_number(self):

        if self.ids.entry.text == '':
            pass

        else:
            if "-" in self.ids.entry.text:
                self.ids.entry.text = f'{self.ids.entry.text.replace("-", "")}'

            else:
                self.ids.entry.text = f"-{self.ids.entry.text}"

    def Clear(self):

        x = self.ids.entry.text

        if 'Ошибка' in self.ids.entry.text:
            self.ids.entry.text = ''

        if len(x) > -1:
            a = self.ids.entry.text[:-1]
            self.ids.entry.text = a

    def Calculate(self, calculation):

        if calculation:

            try:
                self.display.text = str(eval(calculation))

            except:
                self.display.text = "Ошибка"


# Build


class iOSCalculatorEllipseApp(App):  # or iOSCalculatorApp

    title = "Калькулятор"

    def build(self):
        return CalcGridLayout()


class iOSCalculatorApp(App):  # or iOSCalculatorApp

    title = "Калькулятор"

    def build(self):
        return CalcGridLayout()


if SettingsReader.boolIsEllipse is True:
    Builder.load_file('ioscalculator.kv')
    calcAppE = iOSCalculatorEllipseApp()  # or iOSCalculatorApp
    calcAppE.run()

else:
    Builder.load_file('ioscalculator.kv')
    calcApp = iOSCalculatorApp()  # or iOSCalculatorApp
    calcApp.run()
