import os
import requests
from serpapi import GoogleSearch

# Hàm tải ảnh từ url (bỏ qua SSL)
def download_image(url, folder_name, img_name):
    try:
        img_data = requests.get(url, verify=False).content  # Bỏ qua SSL
        with open(os.path.join(folder_name, img_name), 'wb') as handler:
            handler.write(img_data)
        print(f"Downloaded {img_name} from {url}")
    except Exception as e:
        print(f"Failed to download {img_name} from {url}. Error: {e}")

# Thiết lập API key từ SerpAPI
API_KEY = '327e2ec78c56b086336893a39c9158f081646e5b560e057b6c8a22ebb26d5d42'  # Thay bằng API key của bạn
search_queries = [
    "Discus fish"
]

# Tìm kiếm và tải hình ảnh cho mỗi loại cá
for query in search_queries:
    # Tạo thư mục riêng cho từng loại cá với tên gốc từ search_queries
    folder_name = query  # Giữ nguyên tên query làm tên thư mục
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    params = {
        "q": query,
        "tbm": "isch",  # image search
        "api_key": API_KEY
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    images = results['images_results']

    # Lưu 5 hình ảnh đầu tiên cho mỗi loại cá
    for index, image in enumerate(images[17:160]):  # Giới hạn số ảnh tải về
        img_url = image['original']
        img_name = f"{query}_{index + 1}.jpg"  # Đặt tên file giữ nguyên query
        download_image(img_url, folder_name, img_name)
    
    print(f"Downloaded images for {query}")
