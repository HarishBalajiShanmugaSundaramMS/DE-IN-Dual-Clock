# German-Indian Dual Clock

A Simple Dual Clock to display German and Indian Times

___

<h5>Screenshot</h5>
<img src='Images/Dual%20Clock.png' width=300>

<h5>TimeZones Used</h5>

| Country | Region | City    |
| ------- | ------ | ------- |
| Germany | Europe | Berlin  |
| India   | Asia   | Kolkata |




```python
// Use this line of code to get all time zones
import 
print(all_timezones)
```

<h5>Libraries Used</h5>

| Library | Version | Installation                  |
| ------- | ------- | ----------------------------- |
| Tkinter | 8.6     |                               |
| PIL     | 6.1.0   | python3 -m pip install pillow |
| Pytz    | 2019.1  | python3 -m pip install pytz   |



<h5>How to get this code running on your windows machine ?</h5>

Save the following piece of code as a DOS batch file (example: clock.bat)

The first path is where the python is installed, and the second path is where the source code of the dual clock is saved.

``` bash
@ECHO OFF

if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit

"C:\Users\Coder\Anaconda3\python.exe" "C:\Users\Coder\Code\Clock.py"

ECHO Congratulations! Your first batch file executed successfully.

PAUSE
```

By running the batch file, the dual clock program will start working on your windows machine.