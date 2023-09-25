import binascii
from gmssl import sm2

# sm2的公私钥
# SM2_PRIVATE_KEY = '00B9AB0B828FF68872F21A837FC303668428DEA11DCD1B24429D0C99E24EED83D5'
# SM2_PUBLIC_KEY = 'B9C9A6E04E9C91F7BA880429273747D7EF5DDEB0BB2FF6317EB00BEF331A83081A6994B8993F3F5D6EADDDB81872266C87C018FB4162F5AF347B483E24620207'
SM2_PRIVATE_KEY = '548cd3e5cd91c80e61502f53a6ab0ecab5b8a79ad0f6cb7c18a4d333b45235c5'
SM2_PUBLIC_KEY = 'f27c74ece2b486031abd6685830924a7cc6cc8dc78880b3cefca70504874565e8da9b1f91f4b9566ab59b18b74fae1e070175073ab2cf54c9bba317814aa2327'


# 加密
def encrypt(info, pk):
    sm2_encryptor = sm2.CryptSM2(public_key=pk, private_key="")
    e_info = sm2_encryptor.encrypt(info.encode(encoding="utf-8"))
    return e_info.hex()


# 解密
def decrypt(info, sk):
    if info.startswith("04"):
        info = info[2:]
    bytes_info = binascii.a2b_hex(info)
    sm2_decryptor = sm2.CryptSM2(private_key=sk, public_key="")
    raw_info = sm2_decryptor.decrypt(bytes_info).decode(encoding="utf-8")
    return raw_info


if __name__ == "__main__":
    contact_info = "test123"
    encrypted_contact_info = encrypt(contact_info, SM2_PUBLIC_KEY)
    print(encrypted_contact_info)
    m = "0429d9d8b6e433d39c8d4f1cb58bd92b5fc066ccd15fa6311981070f9909b3836f0108ce4cfb7e5465ee94d73ac8cb81b607e153bc365eb65f4a550768c223455ecfa6b04342ade46379587af2c123b134f35e4ce5c76ecdd60895c814615fdd5987f747"

    # decrypted_contact_info = decrypt(encrypted_contact_info, SM2_PRIVATE_KEY)
    decrypted_contact_info = decrypt(m, SM2_PRIVATE_KEY)
    print(decrypted_contact_info)
