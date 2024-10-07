user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}
print("\n")
print("Original Dictionary:")
print(user_preferences)

def update_preferences(user_pref):
    new_user_preferences = {}
    for key in user_pref:
    #for key, value in user_pref.items():     
        if user_pref[key] != None:
        #if value is not None:
            new_user_preferences[key] = user_pref[key]
            
    return new_user_preferences

print("\n")
print("Updated Dictionary:")
print(update_preferences(user_preferences))
print("\n")
