import speech_recognition as sr
import moviepy.editor as mp

""""
@author Prem
"""

clip = mp.VideoFileClip(r"video_recording.mov")
clip.audio.write_audiofile(r"converted.wav")

"""[summary]
I recommend converting it to wav format. It works great with the speech recognition library, which will be covered in the next step.
"""

r = sr.Recognizer()
audio = sr.AudioFile("converted.wav")

"""[summary]
The recognizer will try to understand the speech and convert it to a text format.
"""

with audio as source:
    audio_file = r.record(source)

result = r.recognize_google(audio_file)

"""sumary_line
Exporting the result into a text file.
"""

with open('recognized.txt', mode='w') as file:
    file.write("Recognized Speech :")
    file.write("\n")
    file.write(result)
    print("ready!")
