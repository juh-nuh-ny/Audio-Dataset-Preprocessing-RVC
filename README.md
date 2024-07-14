# Audio-Dataset-Preprocessing-RVC
Pre-processing data for Retrieval Based Voice Conversion input dataset

MANUAL 
Step 1 :  Collect audio files of target voice subject. Audio can be sourced into mp3 or wav files
Step 2 : Download Audacity, UVR
Step 3 : Use UVR to reduce the background music and sounds that come with original audio, ensure the output in wav form
Step 4 : Use Audacity or any other audio editing tool to cut out other voices, intro/outro music, recommended that the overlapping of voices, clapping, footsteps and any non-voice audio is removed. Ensure that the audio when being split there are no segments that abruptly start or end mid syllable when the subject is speaking
Step 5 : Update all the preprocessed audio files in wav form to a single folder, named for easy reference, copy and paste path in the audio_split.py file in line number X and the target folder path in line number Y and run code

Note on Using Raw String Literals for Paths:
--------------------------------------------
When specifying file paths as arguments (e.g., `audio_path` and `output_dir`), 
it's recommended to use raw string literals (prefix the string with 'r') to ensure that backslashes are treated literally and not as escape characters.
This is particularly important on Windows, where file paths use backslashes.

For example:
audio_path = r"C:\Users\Admin\Desktop\12\subject1"
output_dir = r"C:\Users\Admin\Desktop\12\sub1-final"

If you encounter issues with file paths not being recognized correctly, 
ensure you're using raw string literals or replace backslashes with forward slashes in your file paths.

Changing the Audio Segment Length:
----------------------------------
The `duration_sec` parameter in the `split_audio` function controls the length of each audio segment. By default, it is set to 10 seconds. To change the segment length, pass a different value for `duration_sec` when calling the `split_audio` function.

For example, to split the audio into segments of 20 seconds each, call the function as follows:
split_audio(audio_path, output_dir, duration_sec=20)

Adjust `duration_sec` according to your requirements for the length of the audio segments.

Dataset is set
A total of 6+ minutes of data trained to 500+ epochs is good for a flat note voice conversion, usable for documentaries and monotone voice-overs

AUTOMATED 
If you have a lot of data and multiple voices in the unprocessed data:
https://github.com/JarodMica/audiosplitter_whisper
youtube link in the mentioned repo explains the whole process
Pre-requisites
•	Python 3.10 installation
•	git installation
•	vscode installation (highly recommended)
•	ffmpeg installation
•	Cuda Capable Nvidia GPU (highly recommended)
