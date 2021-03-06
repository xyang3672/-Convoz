import webvtt

for caption in webvtt.read('97807885687_audio_transcript.vtt'):
    print(caption.start)
    print(caption.end)
    print(caption.text)