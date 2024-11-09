import os

import googlemaps
from dotenv import load_dotenv

# .envから環境変数読み出し
load_dotenv()

# APIキーを設定
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")  # set api key
gmaps = googlemaps.Client(key=API_KEY)

# 出発地点の緯度経度を設定
# origin = (35.6895, 139.6917)  # 例: 東京駅の座標
origin = (36.530694822504074, 136.62787431862674)  # 金沢工業大学の緯度経度

# Distance Matrix APIを使用して、周辺のコンビニを検索
places_result = gmaps.places_nearby(
    location=origin, radius=1000, type="convenience_store"
)

# 最も近いコンビニの情報を取得
if places_result["results"]:
    nearest_store = places_result["results"][0]
    destination = nearest_store["geometry"]["location"]
    store_name = nearest_store["name"]

    # Distance Matrix APIを使用して、距離と所要時間を取得
    distance_result = gmaps.distance_matrix(
        origins=[origin],
        destinations=[(destination["lat"], destination["lng"])],
        mode="walking",
    )

    if distance_result["rows"][0]["elements"][0]["status"] == "OK":
        distance = distance_result["rows"][0]["elements"][0]["distance"]["text"]
        duration = distance_result["rows"][0]["elements"][0]["duration"]["text"]
        print(f"最寄りのコンビニ: {store_name}")
        print(f"距離: {distance}")
        print(f"徒歩での所要時間: {duration}")
    else:
        print("距離情報を取得できませんでした。")
else:
    print("周辺にコンビニが見つかりませんでした。")
