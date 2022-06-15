import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('/home/sysaddy/GitRepos/SpotifyAutomation/serviceAccountKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://spotifyautomation-352722-default-rtdb.firebaseio.com'
})

# As an admin, the app has access to read and write all data, regardless of Security Rules
ref = db.reference('restricted_access/secret_document')
print(ref.get())