import whisper
import os

#Load the model, chose medium for the combined accuracy and efficiency
model = whisper.load_model('large', 'cuda')

#Load the audio file
audio_file = 'audio_data/0211.aac'
#or audio_file = whisper.load_audio(), if wants to apply pre-process such as noise-reduction, but seems unnecessary now

#Setting the directory for the transcription text
dir = r'C:\Users\a1391\Documents\Whale-Project\transcriptions'

def transcribing(audio, lan):
    #Transcribing text
    result = model.transcribe(audio, verbose = True,  language = lan, task = 'transcribe')
    segments = result['segments']
    text = result['text']

    #Creating the transcribed file and store it in the transcribed_text folder
    audio_basename = os.path.basename(audio)
    audio_basename = os.path.splitext(audio_basename)[0]
    segments_output = os.path.join(dir, audio_basename + '.txt')
    
    #Writing the text in the transcribed text folder line by line
    with open(segments_output, 'w', encoding = 'utf-8') as file:
        for seg in segments:
            file.write(seg['text'].strip() + '\n')
    #strip() to omit all white spaces

    print(f'The transcripted text file is successfuly generated and stored at{segments_output}')
    return text

if __name__ == "__main__":
    transcribing(audio_file, 'zh')