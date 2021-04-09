# FireworkKeyBoard

## Installation

```

pip install -r requirements.txt

```

## How to run

```

python checkpoint_video.py

```

## Project Structure

- sample.mp4 is the video. This file is only for read frame not audio.

- sample.mp3 is the audio from sample.mp4. 

- sample.mp3 cannot be rendered due to high freq, so we had to use online tool to convert .mp3 to .mp3 again. That's how to have sample1.mp3. We use a Thread to run sample1.mp3 audio file in background.
