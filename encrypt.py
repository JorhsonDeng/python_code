class Caesar:
    """ class for doing encryption an decryption using a Caesae ciper!!! """

    def __init__(self,shift):
        """construct the encrption and decryption array"""
        encode = [None]*26          #temp array
        decode = [None]*26          #temp array
        for i in range(26):
            encode[i] = chr((i+shift)%26 + ord('A'))
            decode[i] = chr((i-shift)%26 + ord('A'))
        self._forward = ''.join(encode)
        self._backward = ''.join(decode)

    def encrypt(self,message):
        """encryption function!!!"""
        return self._transform(message,self._forward)

    def decrypt(self,encrypt_msg):
        """decryption function!!!"""
        return self._transform(encrypt_msg,self._backward)

    def _transform(self,message,code):
        msg = list(message)
        for k in range(len(message)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)


if __name__ == "__main__":
    ciper = Caesar(3)
    msg1 = "THIS IS A TEST EXAMPLE"
    enmsg = ciper.encrypt(msg1)
    print('Encrypt:',enmsg)
    demsg = ciper.decrypt(enmsg)
    print('Decrypt:',demsg)