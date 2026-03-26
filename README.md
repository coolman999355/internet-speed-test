# internet-speed-test
A simple Python program to test your internet download speed, upload speed, and ping directly from the terminal.

This project uses the speedtest-cli library to measure your connection and presents the results in a user-friendly menu.

Features
Measure download speed (in Mbps)
Measure upload speed (in Mbps)
Check ping (latency in ms)
Interactive menu for easy selection
Works on Windows, Linux, and MacOS with Python installed
Installation
Make sure you have Python installed (tested with Python 3.10+).
Install the required library using the command:
py -m pip install --user speedtest-cli
Usage
Clone or download this repository.
Run the Python script:
py main.py
Choose an option from the menu:
Choose an option:
1) Download Speed
2) Upload Speed
3) Ping
Your Choice: 
The result will display in Mbps (for speed) or ms (for ping).
Example
Choose an option:
1) Download Speed
2) Upload Speed
3) Ping
Your Choice: 1
Download Speed: 85.42 Mbps
Notes
The program continuously runs until you close it.
speedtest-cli automatically selects the best server for accurate ping results.
License

This project is open-source and free to use.
