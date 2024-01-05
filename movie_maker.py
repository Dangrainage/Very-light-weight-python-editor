import moviepy.editor

clip_1 = moviepy.editor.VideoFileClip("clip_1.mp4")
clip_1 = clip_1.subclip(0, 10.8) # Lenght of video to be adjusted, the first value is when the video starts, and the second Is where It should cut (These are example values)

clip_2 = moviepy.editor.VideoFileClip("clip_2.mp4")
clip_2 = clip_2.subclip(0, 8)

clip_3 = moviepy.editor.VideoFileClip("clip_3.mp4")
clip_3 = clip_3.subclip(0, 10)

audio_clip = moviepy.editor.AudioFileClip("audio.mp3") # This is the audio clip, the name that the audio has should be inputed here, (Example name as always)

new_audioclip = moviepy.editor.CompositeAudioClip([audio_clip])
final_output = moviepy.editor.concatenate_videoclips([clip_1, clip_2, clip_3]) # Video clip names, that you want added, make sure you typed these carefully. (These are example values)
final_output.audio = new_audioclip

final_output.write_videofile("final.mp4", codec='libx264', audio_codec='aac', remove_temp=True, temp_audiofile='temp-audio.m4a') #This is your final output, It will always spit out a final.mp4, name can be customised.
