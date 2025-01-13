import sys
from utils.qr_generator import generate_qr_code

def main():
    link = input("QRコードに変換するリンクを入力してください: ")
    if link:
        generate_qr_code(link)
        print("QRコードが生成されました。")
    else:
        print("リンクが入力されていません。")

if __name__ == "__main__":
    main()