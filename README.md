# EntryShadow

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Detailed Description of the Script](#detailed-description-of-the-script)
- [Disclaimer](#disclaimer)
- [License](#license)

## Overview

This Python script sets up a comprehensive tool called EntryShadow that captures keyboard inputs, mouse actions, system information, screenshots, and microphone recordings. It periodically sends this data to a specified email address. The script is designed to run undetected, logging and transmitting data at regular intervals.

## Features

- Captures keyboard inputs
- Logs mouse movements, clicks, and scrolls
- Collects system information (hostname, IP address, processor, OS, and machine type)
- Takes screenshots
- Records audio from the microphone
- Sends collected data to a specified email address
- Automatically installs any missing dependencies

## Requirements

- Python 3.x
- Internet connection for sending emails and installing dependencies

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ElayDadon/entryshadow.git
   cd entryshadow
   ```

2. **Install dependencies:**

   The script will automatically install the required Python packages if they are not already installed. Alternatively, you can install them manually:

   ```bash
   pip install pyscreenshot sounddevice pynput
   ```

## Configuration

1. **Set up your email credentials:**

   Open the script and replace `YOUR_USERNAME` and `YOUR_PASSWORD` with your email address and password:

   ```python
   EMAIL_ADDRESS = "YOUR_USERNAME"
   EMAIL_PASSWORD = "YOUR_PASSWORD"
   ```

2. **Adjust the report interval:**

   Set the interval for sending reports (in seconds). The default is 60 seconds:

   ```python
   SEND_REPORT_EVERY = 60  # seconds
   ```

## Usage

1. **Run the script:**

   ```bash
   python entryshadow.py
   ```

   EntryShadow will start capturing data immediately.

2. **Stop the script:**

   To stop the script, you can manually kill the process from the terminal or command prompt. The script attempts to delete itself after stopping.

## Detailed Description of the Script

- **Imports and Dependency Management:**

  The script imports various modules needed for logging, system operations, threading, audio recording, and email sending. If some modules are not installed, the script attempts to install them automatically.

- **EntryShadow Class:**

  - `__init__(self, time_interval, email, password)`: Initializes EntryShadow with the specified interval and email credentials.
  - `appendlog(self, string)`: Appends captured data to the log.
  - `on_move(self, x, y)`, `on_click(self, x, y)`, `on_scroll(self, x, y)`: Capture mouse movements, clicks, and scrolls.
  - `save_data(self, key)`: Logs keyboard inputs.
  - `send_mail(self, email, password, message)`: Sends the collected data via email.
  - `report(self)`: Periodically sends the log data via email and resets the log.
  - `system_information(self)`: Captures system information.
  - `microphone(self)`: Records audio from the microphone and sends it via email.
  - `screenshot(self)`: Takes a screenshot and sends it via email.
  - `run(self)`: Starts EntryShadow and sets up listeners for keyboard and mouse events.

## Disclaimer

This script is intended for educational purposes only. Unauthorized use of this script to log keystrokes and capture information without consent is illegal and unethical. Use this tool responsibly and only with proper authorization.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
