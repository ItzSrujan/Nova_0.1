# Nova: An Voice Assistant

Nova is a Python-based voice assistant that performs tasks like opening websites, playing music, providing news, and more. Powered by speech recognition, text-to-speech, and OpenAI's GPT-3.5-turbo, Nova responds intelligently to your voice commands.

## Features

- **Voice Commands**: Recognizes and processes spoken commands.
- **Web Navigation**: Opens Google, GitHub, YouTube, and more.
- **Music Playback**: Plays songs from a predefined library.
- **News Updates**: Reads out the latest headlines.
- **AI Conversations**: Uses OpenAI to chat and answer questions.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/nova-assistant.git
    cd nova-assistant
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Replace `"YOUR openAI API KEY"` in the code with your actual OpenAI key.

4. Set up your `musiclibrary` dictionary with song names and URLs.

## Usage

Run the assistant:

```bash
python nova.py
