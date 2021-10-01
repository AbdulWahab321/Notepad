#imports
import ctypes

pg = 0x5221
class Styles:
    """
    In Mixed Combo class the names have been compressed due to very long names
 ========================================================
DESOIARIH: DEFAULT_DESKTOP_ONLY + ICON_ERROR + ABORT + RETRY + IGNORE + HELP + FOCUSED 
 
SDALIQYNCF: SYSTEM_MODAL + ICON_QUESTION + YES + NO + CANCEL + FOCUSED  

SCTCOHELF: SYSTEM_MODAL + CANCEL + TRY_AGAIN + CONTINUE + HELP + FOCUSED 
    """
    class Buttons:
        ABORT_RETRY_IGNORE = 2
        CANCEL_TRY_CONTINUE = 6
        HELP = 0x4000
        
        OK = 0
        OK_CANCEL = 1
        RETRY_CANCEL = 5
        YES_NO = 4
        YES_NO_CANCEL = 3

    class Mixed_Combo:

        RETRY_ICONINFORMATION_CANCEL = 0x8145
        SYSTEM_MODAL_ICONQUESTION_OK_CANCEL_HELP = 0x5221
        ICON_INFORMATION_ABORT_RETRY_IGNORE_HELP = 0x4322
        ICON_EXCLAMATION_RETRY_CANCEL = 0x2345
        ICON_EXCLAMATION_YES_NO_CANCEL = 0x2343
        SYSTEM_MODAL_RETRY_CANCEL_FOCUSED = 0x9865
        SYSTEM_MODAL_CANCEL_TRY_CONTINUE_FOCUSED = 0x9876
        ICON_WARNING_OK_HELP_FOCUSED = 0x8456230
        SYSTEM_MODAL_ICONQUESTION_RETRY_CANCEL = 0x1025
        SYSTEM_MODAL_ICON_INFO_RETRY_CANCEL_FOCUSED = 0x1245
        ICON_ERROR_YES_NO = 0x3214
        ICON_ERROR_ABORT_RETRY_IGNORE = 0x0012
        ICON_WARNING_RETRY_CANCEL = 0x35
        
        SCTCOHEL = 0x5466
        DESOIARIH = 0x874512
        SDALIQYNCF = 0x1323
    class Icons:
        ICON_EXCLAMATION = ICON_WARNING = 0x30
        ICON_INFORMATION = ICON_ASTERISK = 0x40
        ICON_QUESTION = 0x20
        ICON_STOP = ICON_ERROR = ICON_HAND = 0x10


    class Others:
        SYSTEM_MODAL = 0x1000
        TASK_MODAL = 0x2000

        DEFAULT_DESKTOP_ONLY = 0x20000
        RIGHT = 0x80000
        RIGHT_TO_LEFT_READING = 0x100000

        SET_FOREGROUND = 0x10000
        TOP_MOST = 0x40000
        SERVICE_NOTIFICATION = 0x200000

        
def alert(text="text", style=0, title="title"):
    """
text = some text to show in alert
style = Either Some attributes in Attributes Class or some number
title = title to be shown in alert    
    
Returns the clicked button text
eg: msgbox.alert(text="example", style=Buttons.OKCANCEL, title="EXAMPLE") 
      returns "ok" if ok is pressed and "cancel" if cancel is pressed
    """
    IDABORT = 3
    IDCANCEL = 2
    IDCONTINUE = 11
    IDIGNORE = 5
    IDNO = 7
    IDOK = 1
    IDRETRY = 4
    IDTRYAGAIN = 10
    IDYES = 6

    rt_value = int(ctypes.windll.user32.MessageBoxW(None, text, title, style))
    
    if rt_value == IDABORT:
        return "abort"
    elif rt_value == IDCANCEL:
        return "cancel"
    elif rt_value == IDCONTINUE:
        return "continue"
    elif rt_value == IDIGNORE:
        return "ignore"
    elif rt_value == IDNO:
        return "no"
    elif rt_value == IDOK:
        return "ok"
    elif rt_value == IDRETRY:
        return "retry"
    elif rt_value == IDTRYAGAIN:
        return "try_again"
    elif rt_value == IDYES:
        return "yes"
    else:
        return rt_value
