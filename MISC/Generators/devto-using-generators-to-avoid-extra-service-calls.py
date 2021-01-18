def has_facebook_account(user_email):
    print("calling Facebook service")
    return False


def has_github_account(user_email):
    print("calling Github service")
    return True


def has_twitter_account(user_email):
    print("calling Twitter service")
    return True


def has_social_account(user_email):
    calls = [
        has_facebook_account,
        has_github_account,
        has_twitter_account,
    ]
    return any((call(user_email) for call in calls))


if __name__ == "__main__":
    print("Checking social media apps...")
    has_social_account("fake@email.com")
    print("Done!")
