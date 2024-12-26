import os
import asyncio
from watchfiles import awatch

async def monitor_directory(path: str):
    if not os.path.exists(path):  # Check if the directory exists
        raise FileNotFoundError(f"Directory does not exist: {path}")

    print(f"Monitoring directory: {path}")
    async for changes in awatch(path):  # Start monitoring
        for change, file_path in changes:
            print(f"Change detected: {change}, {file_path}")

async def main():
    directory_path = "./videos"
    if not os.path.exists(directory_path):  # Ensure directory exists
        print(f"Creating directory: {directory_path}")
        os.makedirs(directory_path)

    await asyncio.gather(monitor_directory(directory_path))

if __name__ == "__main__":
    asyncio.run(main())

