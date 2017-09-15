import base64


def encode_base64(image):

    return base64.encode_base64(image)


def decode_base64(encoded_string):

    # decoded_string = encoded_string.decode('utf-8').replace('\n', '')

    return base64.decode_base64(encode_base64)