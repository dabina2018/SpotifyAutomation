import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth





cred = credentials.Certificate("/home/sysaddy/GitRepos/SpotifyAutomation/creds/serviceAccountKey.json")
firebase_admin.initialize_app(cred)


config = {
  "apiKey": "AIzaSyCkaZ5-GD-Db2m4Wyry2d5Xl0IDkXov00s",
  "authDomain": "spotifyautomation-352722.firebaseapp.com",
  "databaseURL": "https://spotifyautomation-352722-default-rtdb.firebaseio.com",
  "projectId": "spotifyautomation-352722",
  "storageBucket": "spotifyautomation-352722.appspot.com",
  "messagingSenderId": "79755140115",
  "appId": "1:79755140115:web:483463b2c01f862d80f3e6",
  "measurementId": "G-M8SBNT7QJP"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
 
email = input('Please enter your e-mail address: ')
password = input('Please enter your password: ')

user = auth.create_user_with_email_and_password(email, password)
print('User login successfully created: (0)'.format(user.get('uid')))

