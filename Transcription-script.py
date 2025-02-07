import whisper
import os

model = whisper.load_model('medium', 'cuda')
audio_file = whisper.load_audio('audio_data/1017.aac')

def transcribing(audio_array, lan):
    #Transcribing text
    result = model.transcribe(audio_array, verbose = True,  language = lan, task = 'transcribe')
    segments = result['segments']
    text = result['text']

    #Creating the transcribed file and store it in the transcribed_text folder, same for the transcribed segments
    audio_basename = os.path.basename(audio_path)[0]
    audio_basename = os.path.splitext(audio_basename)
    text_output = os.path.join('transcribed_text/', audio_basename + '.txt')
    segments_output = os.path.join('transcribed-segments', audio_basename + 'segments.txt')
    
    #Writing the text into the transcribed text folder
    with open(text_output, 'w', 'utf-8') as file:
        file.write(text)

    #Writing the segments in the transcribed segments folder
    with open(segments_output, 'w', 'utf-8') as file:
        for seg in segments:
            file.write(seg['start'])
            file.write(seg['end'])
            file.write(seg['text'])

    return text

if __name__ == "__main__":
    transcribing(audio_file, 'zh')