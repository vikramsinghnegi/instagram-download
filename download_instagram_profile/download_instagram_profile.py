import instaloader

def download_all_posts(username):
    # Create an instaloader instance
    loader = instaloader.Instaloader()

    # Optional: Login if you want to download posts from a private account
    # Uncomment the following lines and replace with your Instagram credentials
    print("Logging in...")
    loader.login('_capture__crews', '7111999@@')

    try:
        # Download profile picture and metadata
        print(f"Downloading profile '{username}'...")
        loader.download_profile(username, profile_pic=True)

        # Get the profile instance
        print(f"Downloading posts from '{username}'...")
        profile = instaloader.Profile.from_username(loader.context, username)

        # Iterate through all posts and download them
        for post in profile.get_posts():
            loader.download_post(post, target=f"{username}_posts")
        
        print(f"All posts from '{username}' have been downloaded.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("=== Instagram Profile Downloader ===")
    user = input("Enter the Instagram username: ")
    download_all_posts(user)
