def ANSImode():
    import ctypes, os
    if os.sys.platform == "win32":
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    else:
        pass
