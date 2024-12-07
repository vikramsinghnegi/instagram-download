import instaloader

# Create an Instaloader instance
loader = instaloader.Instaloader()

# Function to download all posts from your Instagram profile
def download_instagram_posts():
    try:
        print("\n==== Instagram Post Downloader ====")
        username = input("Enter your Instagram username: ")

        # Log in to Instagram
        loader.login(username, input("Enter your password: "))
        print("\nLogged in successfully!")

        # Load profile
        print("\nDownloading your posts...\n")
        profile = instaloader.Profile.from_username(loader.context, username)

        # Download all posts
        for post in profile.get_posts():
            loader.download_post(post, target=f"{username}_posts")

        print("\nAll posts have been downloaded successfully!")

    except Exception as e:
        print(f"\nAn error occurred: {e}")

# Run the program
download_instagram_posts()
