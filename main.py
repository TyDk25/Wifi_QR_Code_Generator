import wifi_qrcode_generator.generator


def qr_code_generator(ssid: str, hidden: bool, auth_type: str, password: str):
    """
    :param ssid: Name of Wi-Fi.
    :param hidden: Indicates whether Wi-FI is hidden or not.
    :param auth_type: Security type of your Wi-Fi.
    :param password: Password of Wi-Fi.
    :return: QR code for Wi-Fi.
    """
    qr = wifi_qrcode_generator.generator.wifi_qrcode(ssid, hidden, auth_type, password)

    return qr.make_image().save('WIFI Code.png')



