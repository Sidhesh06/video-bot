from watchfiles import awatch

async def monitor_directory(path: str):
    async for changes in awatch(path):
        for change, file_path in changes:
            if file_path.endswith('.mp4'):  # Ensure the block under 'if' is indented
                print(f"MP4 file detected: {file_path}")  # Indented block under 'if'
