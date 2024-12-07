import os
import instaloader

# Function to download posts from a public Instagram account
def download_instagram_posts(username, download_path='./downloads'):
    # Initialize instaloader
    loader = instaloader.Instaloader()

    # Fetch profile information
    profile = instaloader.Profile.from_username(loader.context, username)
    
    print(f"Downloading posts from {username}...")
    
    # Create the download directory if it doesn't exist
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Iterate through the posts and download them
    for post in profile.get_posts():
        print(f"Downloading post: {post.url}")
        loader.download_post(post, target=f"{download_path}/{username}")
    
    print("Download complete.")

if __name__ == "__main__":
    username = input("Enter the Instagram username (public account): ")
    download_path = input("Enter the download directory path (default is './downloads'): ")

    if not download_path:
        download_path = './downloads'

    download_instagram_posts(username, download_path)
