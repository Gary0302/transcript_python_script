# Audio Transcription and Translation with Gemini API

This Python script transcribes audio files and translates the content into English using Google's Gemini API. The transcription includes optional timestamps.

## Dependencies / 依賴

- `google-genai`: For working with the Gemini API.
- `python-dotenv`: For loading environment variables from a `.env` file.

You can install the necessary dependencies with:

```bash
pip install google-genai python-dotenv
```

## Usage / 用法

1. Create a `.env` file and add your `GEMINI_API_KEY`.

2. Run the script with your audio file (supports `.mp3`, `.m4a`).

3. The script will generate the original transcript along with its English translation, optionally including timestamps.

### Example / 範例:

```bash
python test.py
```

The result will be saved as `transcription.txt` in the same directory.

## Code Explanation / 代碼解釋

### Steps:
1. **Load environment variables**: The `.env` file is loaded to access your API key.
2. **Transcribe audio**: The audio file is read as bytes, and the MIME type is determined based on the file extension (`.mp3` or `.m4a`) remember to name your autio as "tmp.mp3" or "tmp.m4a".
3. **Generate transcription and translation**: A prompt is sent to Gemini API to generate both the original transcription and its English translation. Timestamps can be included.
4. **Save the result**: The transcriptions are saved into a `.txt` file.

### Features:
- Option to include timestamps in the transcription.
- Automatically detects the file type based on extension.
- Generates both original and translated text.
