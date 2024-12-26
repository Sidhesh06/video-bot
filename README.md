# Video Search and Upload Bot

## Setup Instructions
1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`.
3. Install dependencies: `pip install -r requirements.txt`.
4. Run the bot: `python main.py`.

## Usage
- Place `.mp4` video files in the `videos/` directory.
- The bot will monitor this directory and upload videos when new files are added.

## API Endpoints
- **Get Upload URL**: `GET https://api.socialverseapp.com/posts/generate-upload-url`
- **Upload Video**: `PUT <upload_url>`
- **Create Post**: `POST https://api.socialverseapp.com/posts`
