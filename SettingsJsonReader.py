import json


class SettingsReader:
    with open('settings.json') as json_file:
        data = json.load(json_file)

        for s in data['settings']:
            # print('Settings:\n')

            # print('    ISEllipse: ' + str(s['ISEllipse']))
            boolIsEllipse = (s['ISEllipse'])  # bool

            # print('    Settings-Button-Size-Float: ' + str(s['Settings-Button-Size-Float-X']))
            btnsize_eval = (s['Settings-Button-Size-Float'])  # bool

            # print('    Settings-Button-Size-Float-X: ' + str(s['Settings-Button-Size-Float-X']))
            btnsize_evalx = (s['Settings-Button-Size-Float-X'])  # bool

            # print('    SettingsButtonSize: ' + str(s['SettingsButtonSize']))
            SButtonSize = (s['SettingsButtonSize'])  # int

            # print('    SettingsButtonSizeX: ' + str(s['SettingsButtonSizeX']))
            SButtonSizeX = (s['SettingsButtonSizeX'])  # int

            # print('    PopupResolution: ' + str(s['PopupResolution']))
            PopupResolution = (s['PopupResolution'])  # int

            # print('    PopupResolutionX: ' + str(s['PopupResolutionX']))
            PopupResolutionX = (s['PopupResolutionX'])  # int

            # print('    SettingsFontSize: ' + str(s['SettingsFontSize']))
            SettingsFontSize = (s['SettingsFontSize'])  # int

            # print('    Answer-Font-Size: ' + str(s['Answer-Font-Size']))
            AnsFontSize = (s['Answer-Font-Size'])  # int

            # print('    Radius: ' + str(s['Radius']))
            lineRadius = (s['Radius'])  # int

            # print('    EmptyBoxLayoutSize: ' + str(s['EmptyBoxLayoutSize']))
            EmptyBoxLsize = (s['EmptyBoxLayoutSize'])  # int

            # print('    SettingsButton: ' + str(s['SettingsButton']))
            SettingButton = (s['SettingsButton'])  # int

            # print('    Язык: ' + s['Язык'])
            # calclang = (s['Язык'])  # str

            # print('    Padding: ' + str(s['Padding']))
            PaddingJson = (s['Padding'])  # list

            # print('')
