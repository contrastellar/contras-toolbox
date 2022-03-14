#SingleInstance, Force ; Forces a single instance of the script. Useful if you edit and re-open your script many times.
#InstallKeybdHook ; Keyboard hook. Higher chances to make it work with your game.

1::
                Send {F11}
                Sleep 750
                Send {F11}
                Sleep 750
                Send {F11}
                Sleep 750
                Send {F11}
                Sleep 750
                Send {F10}
                Sleep 750
                Send {F11}
                Sleep 750
                Send {Delete}
                Sleep 750
                Send {F11}
                Sleep 750
        Loop
        {

                Send {F11}
                Sleep 350
                Send {F11}
                Sleep 350
                Send {F11}
                Sleep 350
                Send {F10}
                Sleep 350
                Send {F11}
                Sleep 350
                Send {Delete}
                Sleep 350
                Send {F11}
                Sleep 500

        }
        Return

2::Pause ; Pause the script (and resume).

3:: Reload ; restart script

;--V Functions down here V--


RandSleep(x,y) ; Neat function to have random sleep times.
{
        Random, rand, %x%, %y%
        Sleep %rand%
}