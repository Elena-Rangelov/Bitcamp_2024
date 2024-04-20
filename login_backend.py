from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    client_id = '1083267012795-ibvu42c1pndrf99burjop50rajtcj447.apps.googleusercontent.com'
    redirect_uri = 'http://localhost:5000/oauth2callback'  # Replace with your actual redirect URI
    scope = 'https://www.googleapis.com/auth/calendar'
    oauth_link = f"https://accounts.google.com/o/oauth2/auth?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={scope}&access_type=offline&prompt=consent"
    return render_template('login.html', oauth_link=oauth_link)

@app.route('/oauth2callback')
def callback():
    code = request.args.get('code')
    return f"Authorization code received: {code}"

if __name__ == '__main__':
    app.run(debug=True)
