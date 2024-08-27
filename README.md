# Voice Assistant

A Python-based voice assistant that can perform various tasks such as opening applications, performing mathematical operations, browsing websites, and more through voice commands.

## Features

- **Open Applications**: Launch various Windows applications like File Explorer, Control Panel, Task Manager, and others.
- **Mathematical Operations**: Perform basic arithmetic operations like addition, subtraction, multiplication, and division based on voice commands.
- **Web Browsing**: Open websites directly by speaking the name of the website.
- **Customizable Commands**: Easily extend the assistant's capabilities by adding new commands.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/nawedarshad/Voice-Assistant.git
   cd Voice-Assistant
   ```

2. **Install Dependencies:**

   Make sure you have Python 3.x installed. Then, install the required Python libraries using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Speech Recognition:**

   Ensure your microphone is set up correctly and functioning. You may need to install additional drivers or configure settings depending on your operating system.

## Usage

1. **Run the Voice Assistant:**

   ```bash
   python main.py
   ```

2. **Give Voice Commands:**
   - Example Commands:
     - "Open Google Chrome" → Opens Google Chrome browser.
     - "Play a song on YouTube" → Plays a song on YouTube.
     - "What is 5 plus 3?" → Calculates the sum of 5 and 3.
     - "Open File Explorer" → Opens File Explorer.

3. **Math Operations:**
   - The assistant can perform math operations by recognizing keywords like "add," "subtract," "multiply," and "divide."
   - Example: "What is 10 minus 4?" → The assistant will subtract 4 from 10 and give you the result.

## Project Structure

- `main.py`: The main script that runs the voice assistant.
- `commandProcess.py`: Contains the logic for processing voice commands.
- `data.py`: Holds data such as lists of math phrases and system commands.
- `requirements.txt`: Lists all dependencies required to run the project.
- `README.md`: Documentation for the project.

## Dependencies

Below is a list of all the Python packages used in the project, as specified in `requirements.txt`:

```plaintext
beautifulsoup4==4.12.3
blinker==1.8.2
certifi==2024.7.4
charset-normalizer==3.3.2
click==8.1.7
colorama==0.4.6
comtypes==1.4.6
Flask==3.0.3
idna==3.8
itsdangerous==2.2.0
Jinja2==3.1.4
MarkupSafe==2.1.5
MouseInfo==0.1.3
pillow==10.4.0
PyAudio==0.2.14
PyAutoGUI==0.9.54
PyGetWindow==0.0.9
PyMsgBox==1.0.9
pyperclip==1.9.0
pypiwin32==223
PyRect==0.2.0
PyScreeze==1.0.1
pyttsx3==2.91
pytweening==1.2.0
pywhatkit==5.4
pywin32==306
requests==2.32.3
setuptools==73.0.1
soupsieve==2.6
SpeechRecognition==3.10.4
typing_extensions==4.12.2
urllib3==2.2.2
Werkzeug==3.0.4
wikipedia==1.4.0
```

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to fork the repository, make changes, and submit a pull request. You can also open an issue for any bugs or feature requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) - Python library for performing speech recognition.
- [pyttsx3](https://pypi.org/project/pyttsx3/) - Text-to-speech conversion library in Python.
- [Flask](https://pypi.org/project/Flask/) - Micro web framework written in Python.
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/) - Cross-platform GUI automation Python module.
- [Pywhatkit](https://pypi.org/project/pywhatkit/) - Simple and powerful library for sending WhatsApp messages, playing YouTube videos, and more.

## Contact

For any inquiries or issues, feel free to contact the project maintainer at [nawedarshad25@gmail.com].

```

### Notes:
1. **Replace Placeholder Text**: Be sure to replace `https://github.com/nawedarshad/Voice-Assistant.git` with the actual URL of your GitHub repository, and update the email and other placeholder information with your details.
2. **License**: Make sure to include a `LICENSE` file in your repository if you specify a license in your README.
3. **Optional Sections**: Depending on your project, you might want to add sections like "Known Issues," "Future Enhancements," or "Troubleshooting."