import instaloader

# Instagram credentials
username = 'username'
password = 'password'

try:
    # Step 1: Create an instance of Instaloader
    loader = instaloader.Instaloader()

    # Step 2: Login with your Instagram account
    loader.login(username, password)

    # Step 3: Get the profile of your Instagram account
    profile = instaloader.Profile.from_username(loader.context, username)

    # Step 4: Get the list of users you follow
    following = set(profile.get_followees())

    # Step 5: Get the list of users who follow you
    followers = set(profile.get_followers())

    # Step 6: Find users who are not following you back
    not_following_back = following - followers

    # Step 7: Print the list of users who are not following you back
    print("Users who are not following you back:")
    for user in not_following_back:
        print(user.username)

except instaloader.exceptions.TwoFactorAuthRequiredException:
    # Two-factor authentication is required
    verification_code = input("Enter the verification code: ")
    loader.two_factor_login(verification_code)

    # Continue with the remaining steps after successful authentication
    profile = instaloader.Profile.from_username(loader.context, username)
    following = set(profile.get_followees())
    followers = set(profile.get_followers())
    not_following_back = following - followers

    print("Users who are not following you back:")
    for user in not_following_back:
        print(user.username)

except Exception as e:
    print(f"An error occurred: {e}")