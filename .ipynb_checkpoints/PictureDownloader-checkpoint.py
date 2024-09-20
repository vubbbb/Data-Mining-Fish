import os
import requests
from serpapi import GoogleSearch

# Hàm tải ảnh từ url
def download_image(url, folder_name, img_name):
    img_data = requests.get(url).content
    with open(os.path.join(folder_name, img_name), 'wb') as handler:
        handler.write(img_data)

# Thiết lập API key từ SerpAPI
API_KEY = 'your_serpapi_key'  # Thay bằng API key của bạn
search_queries = [
    "Goldfish fish", "Betta fish", "Discus fish", "Neon fish",
    "Guppy fish", "Koi fish", "Oscar fish", "Flowerhorn fish",
    "Platy fish", "Corydoras fish"
]

# Thư mục lưu ảnh
folder_name = "fish_images"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Tìm kiếm và tải hình ảnh
for query in search_queries:
    params = {
        "q": query,
        "tbm": "isch",  # image search
        "api_key": API_KEY
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    images = results['images_results']

    # Lưu 5 hình ảnh đầu tiên cho mỗi loại cá
    for index, image in enumerate(images[:5]):
        img_url = image['original']
        img_name = f"{query.replace(' ', '_')}_{index + 1}.jpg"
        download_image(img_url, folder_name, img_name)
        print(f"Downloaded {img_name} from {img_url}")
