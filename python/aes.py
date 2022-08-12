#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Time : 2021/7/22 14:46 
# FileName : aes.py
# Author : Gecko
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
from binascii import b2a_hex

class AES_encrypt():
    def __init__(self, key, iv=''):
        self.block_size = 16
        self.key = key.encode()
        if len(iv) == 16:
            iv = iv.encode()
        elif len(iv) < 16:
            add = 16 - (len(iv) % 16)
            iv = iv.encode() + ('\0' * add).encode('utf-8')
        else:
            raise Exception("IV length error")
        self.iv = iv
    def unpad(self, string):
        """
        去除尾部多余填充
        :param string: 需要去除填充的内容
        :return:
        """
        return string[:-ord(string[len(string) - 1:])]

    def ecb_encrypt(self, text):
        """
        AES_ECB模式加密函数
        :param text:需要加密的内容
        :return:加密结果
        """
        str_encrypt = text.encode('utf-8')
        cryptos = AES.new(self.key, AES.MODE_ECB)
        plain_text = cryptos.encrypt(pad(str_encrypt, self.block_size))
        result = str(base64.b64encode(plain_text).decode("utf-8"))
        print(f'ECB moudle [{text}] encrypt is [{result}]')
        return result

    def ecb_decrypt(self, text):
        """
        AES_ECB模式解密函数
        :param text: 需要解密的内容
        :return: 解密结果
        """
        base64_decrypted = base64.b64decode(text.encode('utf-8'))
        cryptos = AES.new(self.key, AES.MODE_ECB)
        result = str(self.unpad(cryptos.decrypt(base64_decrypted)), encoding='utf-8').strip()
        print(f'ECB moudle [{text}] decrypt is [{result}]')
        return result

    def cbc_encrypt(self, text):
        """
        AES_CBC模式加密函数
        :param text: 需要加密的内容
        :return: 加密结果
        """
        str_encrypt = text.encode('utf-8')
        cryptos = AES.new(self.key, AES.MODE_CBC, self.iv)
        plain_text = cryptos.encrypt(pad(str_encrypt, self.block_size))
        result = str(base64.b64encode(plain_text).decode("utf-8"))
        print(f'CBC moudle [{text}] encrypt base64 is [{result}]')
        print(f'CBC moudle [{text}] encrypt hex is [{b2a_hex(plain_text).decode()}]')
        return result

    def cbc_decrypt(self, text):
        """
        AES_CBC模式解密函数
        :param text: 需要解密的内容
        :return: 解密结果
        """
        base64_decrypted = base64.b64decode(text.encode('utf-8'))
        cryptos = AES.new(self.key, AES.MODE_CBC, self.iv)
        result = str(self.unpad(cryptos.decrypt(base64_decrypted)), encoding='utf-8').strip()
        print(f'CBC moudle [{text}] decrypt is [{result}]')
        return result

    def cfb_encrypt(self, text):
        """
        AES_CFB模式加密函数
        :param text: 需要加密的内容
        :return: 加密结果
        """
        str_encrypt = text.encode('utf-8')
        cryptos = AES.new(key=self.key, mode=AES.MODE_CFB, IV=self.iv, segment_size=128)
        plain_text = cryptos.encrypt(pad(str_encrypt, self.block_size))
        result = str(base64.b64encode(plain_text).decode('utf-8'))
        print(f'CFB moudle [{text}] encrypt is [{result}]')
        return result

    def cfb_decrypt(self, text):
        """
        AES_CFB模式解密函数
        :param text: 需要解密的内容
        :return: 解密结果
        """
        base64_decrypted = base64.b64decode(text.encode('utf-8'))
        cryptos = AES.new(key=self.key, mode=AES.MODE_CFB, IV=self.iv, segment_size=128)
        result = str(self.unpad(cryptos.decrypt(base64_decrypted)), encoding='utf-8').strip()
        print(f'CFB moudle [{text}] decrypt is [{result}]')
        return result


if __name__ == '__main__':
    string = '今天是个开心的日子！'
    key = '7c6e1257d0e81ff55bda80cc904365ae'
    iv = 'f4cf5e4620455cd7'

    aes = AES_encrypt(key=key, iv=iv)
    enctypy_str = aes.cfb_encrypt(string)
    aes.cfb_decrypt(enctypy_str)
