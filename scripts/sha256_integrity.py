import hashlib


def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()

    with open(file_path, 'rb') as file:
        for block in iter(lambda: file.read(4096), b''):
            sha256_hash.update(block)

    return sha256_hash.hexdigest()


if __name__ == '__main__':
    file_path = 'sample.jpg'
    print('SHA256:', calculate_sha256(file_path))
