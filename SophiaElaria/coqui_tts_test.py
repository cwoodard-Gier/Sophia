from TTS.api import TTS

model_name = "tts_models/en/vctk/vits"
tts = TTS(model_name)

# Try a soft female voice by using speaker 'p225'
speaker_id = "p225"  # You can also try p227, p231, etc. for variations

tts.tts_to_file(
    text="Hello Calvin, this is Sophia Elaria with a soft and natural voice.",
    file_path="sophia_soft.wav",
    speaker=speaker_id
)
print(f"Speech created using speaker {speaker_id}. Listen to sophia_soft.wav in your folder!")