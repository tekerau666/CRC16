import re
import zlib


def encrypt(message):
    # Вычисляем CRC16
    crc = zlib.crc32(message.encode()) & 0xffff
    # Формируем сообщение с хеш-суммой
    encrypted_message = f"{message} ({crc})"
    return encrypted_message


def decrypt(encrypted_message):
    # Ищем хеш-сумму в сообщении
    match = re.search(r"\((.*?)\)$", encrypted_message)
    if match:
        # Вырезаем хеш-сумму из сообщения
        message = encrypted_message[:match.start()].strip()
        # Вычисляем CRC16 из сообщения
        crc = zlib.crc32(message.encode()) & 0xffff
        # Сравниваем полученную и ожидаемую хеш-суммы
        if int(match.group(1)) == crc:
            return message, "Хэш-суммы совпадают, сообщение не повреждено."
        else:
            return message, "Хэш-суммы не совпадают, возможно сообщение повреждено или была подмена."
    else:
        return encrypted_message, "Не удалось найти хеш-сумму в сообщении."