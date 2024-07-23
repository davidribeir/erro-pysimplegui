'''Traceback (most recent call last):
  File "C:\Users\Guidi Vendas\AppData\Local\Programs\Python\Python311\Lib\site-packages\PySimpleGUI\PySimpleGUI.py", line 22376, in read    self.dict = json.load(f)
                ^^^^^^^^^^^^
  File "C:\Users\Guidi Vendas\AppData\Local\Programs\Python\Python311\Lib\json\__init__.py", line 293, in load 
    return loads(fp.read(),
           ^^^^^^^^^^^^^^^^
  File "C:\Users\Guidi Vendas\AppData\Local\Programs\Python\Python311\Lib\json\__init__.py", line 346, in loads
    return _default_decoder.decode(s)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Guidi Vendas\AppData\Local\Programs\Python\Python311\Lib\json\decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Guidi Vendas\AppData\Local\Programs\Python\Python311\Lib\json\decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "c:\Users\Guidi Vendas\Desktop\Nova pasta\s.py", line 1, in <module>
    import PySimpleGUI as sg
  File "C:\Users\Guidi Vendas\AppData\Local\Programs\Python\Python311\Lib\site-packages\PySimpleGUI\__init__.py", line 1, in <module>   
    from .PySimpleGUI import *
  File "C:\Users\Guidi Vendas\AppData\Local\Programs\Python\Python311\Lib\site-packages\PySimpleGUI\PySimpleGUI.py", line 25978, in <module>
    pysimplegui_user_settings = UserSettings(filename=DEFAULT_USER_SETTINGS_PYSIMPLEGUI_FILENAME, path=DEFAULT_USER_SETTINGS_PYSIMPLEGUI_PATH)
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Guidi Vendas\AppData\Local\Programs\Python\Python311\Lib\site-packages\PySimpleGUI\PySimpleGUI.py", line 22024, in __init__
    self.load(filename=filename, path=path)
  File "C:\Users\Guidi Vendas\AppData\Local\Programs\Python\Python311\Lib\site-packages\PySimpleGUI\PySimpleGUI.py", line 22323, in load    self.read()
  File "C:\Users\Guidi Vendas\AppData\Local\Programs\Python\Python311\Lib\site-packages\PySimpleGUI\PySimpleGUI.py", line 22392, in read    _error_popup_with_traceback('User Settings read warning', 'Error reading settings from file', self.full_filename, e)
  File "C:\Users\Guidi Vendas\AppData\Local\Programs\Python\Python311\Lib\site-packages\PySimpleGUI\PySimpleGUI.py", line 21781, in _error_popup_with_traceback
    _error_popup_with_code(title, filename, line_num, error_message, *args, emoji=emoji)
  File "C:\Users\Guidi Vendas\AppData\Local\Programs\Python\Python311\Lib\site-packages\PySimpleGUI\PySimpleGUI.py", line 21819, in _error_popup_with_code
    window = Window(title, layout, keep_on_top=True)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Guidi Vendas\AppData\Local\Programs\Python\Python311\Lib\site-packages\PySimpleGUI\PySimpleGUI.py", line 9895, in __init__
    if pysimplegui_user_settings.get('-enable debugger-', False) or debugger_enabled:
       ^^^^^^^^^^^^^^^^^^^^^^^^^
NameError: name 'pysimplegui_user_settings' is not defined
'''
