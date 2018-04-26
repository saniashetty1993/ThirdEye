import boto3

import os

polly = boto3.client('polly')
spoken_text = polly.synthesize_speech(Text='Hi ,The staircase in your path, 98% accuracy.',
                                      OutputFormat='mp3',
                                      VoiceId='Emma')

with open('output7.mp3', 'wb') as f:
    f.write(spoken_text['AudioStream'].read())
    f.close()