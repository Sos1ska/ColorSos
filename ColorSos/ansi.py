# Author: Sos1ska
# https://vk.com/nikitasos1ska
# https://github.com/Sos1ska
from .win32 import ANSImode

billet='\u001b['

Fore=dict(
    list(
        zip(
            ['black',
            'red',
            'green',
            'yellow',
            'blue',
            'purple',
            'cyan',
            'white'
            ],
            list(range(30, 38))
        )
    )
)
Style=dict(
    list(
        zip(
            [
            'bold',
            'faded',
            'italics',
            'underlined',
            'flashing',
            'striketrough'
            ],
            list(range(1,10))
        )
    )
)
Background=dict(
    list(
        zip(
            [
            'black',
            'red',
            'green',
            'yellow',
            'blue',
            'purple',
            'cyan',
            'white'
            ],
            list(range(40, 48))
        )
    )
)

class ANSIError(Exception): ...
def check_autolog():
    try:
        from LOGer import autolog
    except ImportError:
        return False
    finally:
        return True
class SetColor(ANSIError):
    def Fore(color, skip_error=False):
        ANSImode()
        if skip_error == False:
            if color not in Fore:
                if check_autolog() == True:
                    from LOGer import autolog
                    autolog(typelog='error', text=f'Not Found Color -> {color}', typemsg='CRITICAL', nick='ColorSos', wayerror='ERROR_COLORSOS')
                elif check_autolog() == False:
                    raise ANSIError(f'Not Found Color -> {color}')
            else:
                return billet+str(Fore[color])+'m'
    def Style(type, skip_error=False):
        ANSImode()
        if skip_error == False:
            if type not in Style:
                if check_autolog() == True:
                    from LOGer import autolog
                    autolog(typelog='error', text=f'Not Found Color -> {type}', typemsg='CRITICAL', nick='ColorSos', wayerror='ERROR_COLORSOS')
                elif check_autolog() == False:
                    raise ANSIError(f'Not Found Color -> {type}')
            else:
                return billet+str(Style[type])+'m'
    def BackGround(color, skip_error=False):
        ANSImode()
        if skip_error == False:
            if color not in Fore:
                if check_autolog() == True:
                    from LOGer import autolog
                    autolog(typelog='error', text=f'Not Found Color -> {color}', typemsg='CRITICAL', nick='ColorSos', wayerror='ERROR_COLORSOS')
                elif check_autolog() == False:
                    raise ANSIError(f'Not Found Color -> {color}')
            else:
                return billet+str(Background[color])+'m'
    def Clear():
        ANSImode()
        return billet+str(0)+'m'