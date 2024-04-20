# from flask import Flask, redirect, url_for, request

# app = Flask(__name__)

# @app.route('/')
# def home():
#     client_id = '1083267012795-ibvu42c1pndrf99burjop50rajtcj447.apps.googleusercontent.com'
#     redirect_uri = 'https://elena-rangelov.github.io/Bitcamp_2024/login.html'  # Replace with your actual redirect URI
#     scope = 'https://www.googleapis.com/auth/calendar'
#     oauth_link = f"https://accounts.google.com/o/oauth2/auth?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={scope}&access_type=offline&prompt=consent"
#     return f"<a href='{oauth_link}'>Click here to authorize with Google</a>"

# @app.route('/oauth2callback')
# def callback():
#     # This route will be called by Google after the user authorizes your app
#     code = request.args.get('code')
#     # You can now exchange this code for an access token and refresh token
#     # Implement the token exchange logic here
#     return f"Authorization code received: {code}"

# if __name__ == '__main__':
#     app.run(debug=True)

def generate_oauth_link():
    client_id = '1083267012795-ibvu42c1pndrf99burjop50rajtcj447.apps.googleusercontent.com'
    redirect_uri = 'https://elena-rangelov.github.io/Bitcamp_2024/login.html'  # Replace with your actual redirect URI
    scope = 'https://www.googleapis.com/auth/calendar'
    oauth_link = f"https://accounts.google.com/o/oauth2/auth?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={scope}&access_type=offline&prompt=consent"
    return oauth_link

if __name__ == "__main__":
    print(generate_oauth_link())
