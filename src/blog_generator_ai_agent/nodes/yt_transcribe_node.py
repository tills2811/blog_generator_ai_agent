from src.blog_generator_ai_agent.state.state import State
from youtube_transcript_api import YouTubeTranscriptApi


class YTTranscription:
    """
   Get Youtube transcription
    """

    def process(self, state: State) -> dict:
        """Fetches transcript from a given YouTube URL"""
  
    
        video_id = state['yt_url'].replace('https://www.youtube.com/watch?v=', '')

        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            output = '\n'.join([x['text'] for x in transcript])
            print("✅ Transcription fetched successfully.")
        except Exception as e:
            print(f"❌ Error fetching transcript: {e}")
            output = ""

        return {"yt_transcription": output}

