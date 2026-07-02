Output docs/pytest-ci-demo.gif

Require vhs
Set FontSize 13
Set Width 1200
Set Height 600
Set PlaybackSpeed 3
Set Framerate 24
Set Theme "Dracula"

Sleep 500ms
Type "python3 -m pytest automation/ -m 'not appium and not selenium and not slow' --tb=no -q"
Sleep 800ms
Enter
Sleep 100s
Sleep 3s
