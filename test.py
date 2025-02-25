from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# 載入環境變數
load_dotenv()

def transcribe_audio(filename, include_timestamps=False):
    # 初始化 Gemini 客戶端
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    # 讀取檔案為 bytes
    with open(filename, 'rb') as f:
        audio_bytes = f.read()

    # 根據檔案副檔名判斷 MIME type
    file_ext = os.path.splitext(filename)[1].lower()
    if file_ext == '.mp3':
        mime_type = 'audio/mpeg'
    elif file_ext == '.m4a':
        mime_type = 'audio/x-m4a'
    else:
        mime_type = 'audio/mpeg'  # 預設值

    print(f"Processing file: {filename}, Extension: {file_ext}, MIME type: {mime_type}")

    # 設定時間戳記格式
    timestamp_format = "[MM:SS]" if include_timestamps else ""
    
    # 建立 prompt
    prompt = f"""Please provide two transcriptions for this audio:
1. A origin transcript {timestamp_format} 
2. An English translation {timestamp_format}

Please format your response as follows:
[ORIGINAL]
(Original language transcription here)

[ENGLISH]
(English translation here)

Note1: Make sure to include line breaks between each section of the transcript, but don't be too trivial
"""

    # 呼叫 Gemini API 生成內容
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=[
            prompt,
            types.Part.from_bytes(
                data=audio_bytes,
                mime_type=mime_type
            )
        ]
    )
    return response

if __name__ == '__main__':
    # 範例：處理 tmp.mp3 並包含時間戳記
    result = transcribe_audio("tmp.mp3", include_timestamps=True)
    
    # 將結果儲存成 txt 檔案
    output_filename = "transcription.txt"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(str(result))
    
    print(f"Transcription saved to {output_filename}")
