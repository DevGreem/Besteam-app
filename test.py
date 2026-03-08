from src import SteamClient
import json

client = SteamClient()

#user_stats = client.apps.get_user_stats("76561199219165937", 262060)
app_details = client.apps.get_app_details(262060)

print(app_details)