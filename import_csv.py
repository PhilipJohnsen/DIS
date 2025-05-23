import pandas as pd
from app import app, conn
from app.models import ClothingItem, insert_clothing_item

# Læs CSV
df = pd.read_csv("Data/Clothing_Items_Final.csv")  # eller "Data/Clothing_Items_Final.csv" hvis den ligger i en undermappe

# Tilføj til databasen i Flask-app kontekst
with app.app_context():
    for _, row in df.iterrows():
        item = ClothingItem(
            id = row.get("number","Unknown"),
            image_url = row.get("image","No Image"),
            size = row.get("size", "Other"),
            color = row.get("color","Other"),
            name=row.get("name", "Unknown"),
            type_=row.get("label", "Other"),
            price=float(row.get("price", 0.0))
        )

        insert_clothing_item(
            name=item.name,
            type_=item.type,
            size=item.size,
            color=item.color,
            price=item.price,
            image_url=item.image_url
        )

    conn.commit()
    print("✅ Data importeret!")
