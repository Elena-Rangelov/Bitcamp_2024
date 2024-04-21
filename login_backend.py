

def generate_oauth_link():
    client_id = '1083267012795-ibvu42c1pndrf99burjop50rajtcj447.apps.googleusercontent.com'
    redirect_uri = 'https://elena-rangelov.github.io/Bitcamp_2024/login.html'  # Replace with your actual redirect URI
    scope = 'https://www.googleapis.com/auth/calendar'
    oauth_link = f"https://accounts.google.com/o/oauth2/auth?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={scope}&access_type=offline&prompt=consent"
    return oauth_link

if __name__ == "__main__":
    print(generate_oauth_link())
