import os
# from kivy.config import Config  # Конфиг Импортируется первым и прописан тоже первым.
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
# Config.set('graphics', 'resizable', 1)
# Config.set('graphics', 'width', '650')
# Config.set('graphics', 'height', '1015')
# Config.write()


class SettingsWindow(Popup):

    def remove_log(self):
        try:
            os.remove('log.txt')

        except Exception as rlog:
            print(rlog)

    def SetFontSize(self):

        self.FontSizeX = self.ids.SetFont.text
        print('FontSize: ', str(self.FontSizeX))

        if not os.path.exists('settings.txt'):
            settingsfile = open("settings.txt", "w")
            settingsfile.close()

        with open('settings.txt') as file:
            for line in file:
                print(line)

        with open('settings.txt', 'r') as f:
            old_data = f.read()

        new_data = old_data.replace(str(line), str(self.FontSizeX))

        with open('settings.txt', 'w') as f:
            f.write(new_data)

        print('Установлено: ', str(self.FontSizeX))
        self.dismiss()

        ###############################################################

        self.FontSizeXB = self.ids.SetFontButton.text
        print('FontSize: ', str(self.FontSizeXB))

        if not os.path.exists('settingsbutton.txt'):
            settingsfile = open("settingsbutton.txt", "w")
            settingsfile.close()

        with open('settingsbutton.txt') as file:
            for line in file:
                print(line)

        with open('settingsbutton.txt', 'r') as f:
            old_data = f.read()

        new_data = old_data.replace(str(line), str(self.FontSizeXB))

        with open('settingsbutton.txt', 'w') as f:
            f.write(new_data)


class CalcGridLayout(GridLayout):

    if not os.path.exists('settings.txt'):
        settingsfilec = open("settings.txt", "w", encoding='utf-8')
        settingsfilec.write('128')
        settingsfilec.close()

    try:
        with open('settings.txt') as file:
            for line in file:
                setline = line
                print(line)

    except Exception as exx:
        print(exx)

    if not os.path.exists('settingsbutton.txt'):
        settingsfilec = open("settingsbutton.txt", "w", encoding='utf-8')
        settingsfilec.write('72')
        settingsfilec.close()

    try:
        with open('settingsbutton.txt') as file:
            for lineb in file:
                setlineb = lineb
                print(lineb)

    except Exception as exxb:
        print(exxb)

    def positive_number(self):

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
            self.ids.entry.text = (a)

    def Check(self):

        if "," not in (self.ids.entry.text):
            print('Запятая не обнаружена.')

        elif "," in self.ids.entry.text:
            axa = self.ids.entry.text.replace(",", ".")
            print(axa)
            print('Запятая обнаружена.')

    def Calculate(self, calculation):

        if calculation:
            try:
                self.display.text = str(eval(calculation))

            except Exception as e:

                self.display.text = "Ошибка"  # + str(e)
                settingsfile = open("log.txt", "a", encoding='utf-8')
                settingsfile.write('\n' + str(e))
                settingsfile.close()


class iOSCalculatorApp(App):

    def build(self):

        # Window.set_system_cursor('hand')
        # Window.show_cursor = (True)
        # Window.clearcolor = (1, 1, 1, 1)
        return CalcGridLayout()


calcApp = iOSCalculatorApp()
calcApp.run()
