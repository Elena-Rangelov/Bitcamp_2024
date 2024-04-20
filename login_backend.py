from flask import Flask, request

app = Flask(__name__)

@app.route("/oauth/callback")
def oauth_callback():
  auth_code = request.args.get("code")
  # Use the auth code to exchange for access token (see next step)
  return "You have been authorized!"