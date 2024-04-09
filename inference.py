import os
import sys

# project_root = os.path.abspath('.')
# sys.path.append(project_root)

from get_tts_wav import GPT_SoVITS_TTS_inference

inference = GPT_SoVITS_TTS_inference()

prompt_text = """
but when the entire family,reunite once again his chair his bowl
"""

text = """
This is a RoBERTa-base model trained on ~124M tweets from January 2018 to December 2021, and finetuned for sentiment analysis with the TweetEval benchmark. The original Twitter-based RoBERTa model can be found here and the original reference paper is TweetEval. This model is suitable for English. As I sit here, the memories of us flood my mind like a river bursting its banks. I miss you with an ache that consumes every fiber of my being. The days without you stretch into eternity, each moment passing like a slow, painful sigh. Your absence is a shadow that lingers, darkening even the brightest corners of my world. I yearn for your laughter, the way your eyes sparkled when you spoke of your dreams. How I long to feel your touch, a gentle caress that once felt like the promise of forever. In the quiet of the night, I find myself whispering your name into the darkness, hoping against hope that somehow, you'll hear my heart calling out to yours. The silence mocks me, echoing back your silence, a void where your voice once resided. I hold onto the fragments of our past, fragile pieces of a beautiful mosaic we once created together. Yet they slip through my fingers like grains of sand, leaving me grasping at memories that seem to fade with each passing day. Come back to me, my love. Let us mend what is broken, breathe life into what has withered. For in your absence, I am but a hollow vessel, waiting to be filled once more with the warmth of your presence. Until then, I will carry you in my heart, where the embers of our love still burn brightly amidst the darkness. Know that you are missed beyond words, and that my arms ache to hold you close once more.
"""
inference.get_tts_wav(text, prompt_text)
