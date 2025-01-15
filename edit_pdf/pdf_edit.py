import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
import re

def extract_specific_numbers_from_pdf_with_ocr(pdf_path, target_string):
    """
    PDFファイルからOCRを使って手書きの数字を含む特定の文字列に続く数字を抽出し、大きい順に並べる。

    Args:
        pdf_path (str): PDFファイルのパス。
        target_string (str): 抽出対象の文字列。

    Returns:
        list: 大きい順に並べた数字のリスト。
    """
    # PDFファイルを開く
    document = fitz.open(pdf_path)
    numbers = []

    # 各ページを処理
    for page_num in range(len(document)):
        page = document[page_num]

        # ページを画像として取得（OCR用）
        pix = page.get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes("png")))

        # OCRを使って画像からテキストを抽出
        text = pytesseract.image_to_string(img)

        # 正規表現で "特定の文字列+数字" を探す
        pattern = re.escape(target_string) + r"\s*(\d+\.?\d*)"
        matches = re.findall(pattern, text)

        # 抽出した数字をfloatに変換してリストに追加
        numbers.extend(map(float, matches))

    # 大きい順にソート
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers

# 使用例
if __name__ == "__main__":
    pdf_path = "cost_random.pdf"  # PDFファイルのパスを指定
    target_string = "cost:"  # 数字の前にある特定の文字列を指定
    sorted_numbers = extract_specific_numbers_from_pdf_with_ocr(pdf_path, target_string)
    print("抽出された数字（大きい順）:")
    print(sorted_numbers)
