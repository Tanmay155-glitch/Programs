from pytube import YouTube

# Function to download YouTube video
def download_video(url):
    try:
        # Create YouTube object
        yt = YouTube(url)
        
        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()
        
        print(f"Downloading: {yt.title}")
        print(f"Resolution: {video_stream.resolution}")
        print(f"File size: {round(video_stream.filesize / (1024 * 1024), 2)} MB")
        
        # Download the video
        video_stream.download()
        print("Download completed successfully!")
    except Exception as e:
        print("An error occurred:", e)

# URL of the YouTube video
video_url = input("Enter the YouTube video URL: ")

# Call the function
download_video(video_url)
