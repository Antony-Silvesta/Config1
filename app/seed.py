from db import connect_db
def seed_database():
    """Create a collection and insert seed data."""
    db = connect_db()
    try:
        collection = db["users"]
        collection.insert_many([
            {
            "username": "demo",
            "first_name": "admin",
            "last_name": "admin",
            "password": "",
            "mode_2fa": "Off",
            "groups": ["Admin"],
            "rights": "Admin",
            "notes": {"info": "this 'notes' field exists only for this default admin user", "p": "donttrustyou"},
            "vec_2fa": None,  # Corrected null to None
            "baseurl": "https://demo.filebrowser.org/login?redirect=/files/",
            "is_valid": False,
            "expected_error": "Wrong credentials",
        },
        {
            "username": "demo",
            "first_name": "admin",
            "last_name": "admin",
            "password": "demo",
            "mode_2fa": "Off",
            "groups": ["Admin"],
            "rights": "Admin",
            "notes": {
                "info": "this 'notes' field exists only for this default admin user",
                "p": "donttrustyou"
            },
            "vec_2fa": None,  # Corrected null to None
            "baseurl": "https://demo.filebrowser.org/login?redirect=/files/",
            "is_valid": True,
            "expected_error": "success",
        }

           
        ])
        print("Seed data inserted successfully.")
    except Exception as e:
        print(f"Error seeding database: {e}")
if __name__ == "__main__":
    seed_database()