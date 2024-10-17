# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
#
# import whisper
#
# # Load the pre-trained Whisper model
# model = whisper.load_model("base")
#
# # Transcribe the recorded audio
# result = model.transcribe("output.wav")
#
# # Print the transcription
# print("Transcription:")
# print(result["text"])

import whisper


def transcribe_audio(file_path):
    # Load the pre-trained Whisper model
    model = whisper.load_model("base")

    # Transcribe the audio file
    result = model.transcribe(file_path)

    # Return the transcription
    return result['text']


if __name__ == "__main__":
    transcription = transcribe_audio('.venv/output.wav')  # Path to the recorded audio
    print("Transcription:", transcription)
