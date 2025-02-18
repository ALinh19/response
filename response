from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def get_users():
    url = "https://demo-rest-api-ewdl.onrender.com/users"  # API lấy danh sách user
    response = requests.get(url)

    if response.status_code == 200:
        users = response.json()
        if users:
            result = "\nDanh sách người dùng:\nSTT - Tên - Email\n"
            for idx, user in enumerate(users, start=1):
                result += f"{idx} - {user['name']} - {user['email']}\n"
        else:
            result = "\nChưa có dữ liệu nào được nhập!"
    else:
        result = f"\nLỗi khi lấy dữ liệu! Mã lỗi: {response.status_code}"

    return f"<pre>{result}</pre>"  # Hiển thị kết quả dưới dạng văn bản trên trình duyệt

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
