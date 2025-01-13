def generate_qr_code(link: str) -> None:
    import qrcode

    # QRコードを生成
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    # 画像を作成
    img = qr.make_image(fill_color="black", back_color="white")

    # 画像を保存
    img.save("qr_code.png")