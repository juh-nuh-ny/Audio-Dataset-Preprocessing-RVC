import os
from pydub import AudioSegment

def split_audio(audio_path, output_dir, duration_sec=10):
    """
    Splits an audio file into segments of a specified duration and saves them to an output directory.

    Args:
    audio_path (str): Path to the input audio file.
    output_dir (str): Path to the output directory where segments will be saved.
    duration_sec (int, optional): Duration of each segment in seconds. Defaults to 10.
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Open the audio file
    audio = AudioSegment.from_wav(audio_path)

    # Get total audio duration in milliseconds
    total_duration_ms = len(audio)

    # Calculate the ideal number of segments based on desired duration
    num_segments = int(total_duration_ms / (duration_sec * 1000))

    # Check if there's a remaining leftover duration after ideal segment calculation
    remaining_duration_ms = total_duration_ms % (duration_sec * 1000)

    # Split the audio and save segments
    for i in range(num_segments):
        start_time = i * duration_sec * 1000
        end_time = start_time + duration_sec * 1000
        segment = audio[start_time:end_time]

        # Generate output filename with zero-padded index
        output_filename = f"segment_{i:03d}.wav"
        output_path = os.path.join(output_dir, output_filename)

        # Export the segment as a WAV file
        segment.export(output_path, format="wav")

    # Handle the last segment if there's remaining audio
    if remaining_duration_ms > 0:
        start_time = num_segments * duration_sec * 1000
        end_time = total_duration_ms
        segment = audio[start_time:end_time]
        output_filename = f"segment_{num_segments:03d}.wav"
        output_path = os.path.join(output_dir, output_filename)
        segment.export(output_path, format="wav")

    # Open the output directory in file explorer after process completion
    os.startfile(output_dir)

"""
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
"""

"""
Changing the Audio Segment Length:
----------------------------------
The `duration_sec` parameter in the `split_audio` function controls the length of each audio segment. By default, it is set to 10 seconds. To change the segment length, pass a different value for `duration_sec` when calling the `split_audio` function.

For example, to split the audio into segments of 20 seconds each, call the function as follows:
split_audio(audio_path, output_dir, duration_sec=20)

Adjust `duration_sec` according to your requirements for the length of the audio segments.
"""

audio_path = "input dirctory path"
output_dir = "output directory path"
split_audio(audio_path, output_dir)

print("Process completed, output directory opened.")
