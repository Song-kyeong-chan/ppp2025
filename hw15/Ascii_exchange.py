class Acsii:
    low_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lower_ascii = dict(zip(low_alphabet,range(97,123)))
    upper_ascii = dict(zip(low_alphabet.upper(),range(65,91)))
    def __init__(self):
        pass
    
    def upper_to_lower(self,text):
        if text in self.upper_ascii:
            lower_ascii_val = self.upper_ascii[text]+32
            for key,val in self.lower_ascii.items():
                if lower_ascii_val == val:
                    text = key
            return text
        else:
            return ''

    def lower_to_upper(self,text):
        if text in self.lower_ascii:
            upper_ascii_val = self.lower_ascii[text]-32
            for key,val in self.upper_ascii.items():
                if upper_ascii_val == val:
                    text = key
            return text
        else:
            return ''

    def toggle_text(self,text: str)->str:
        
        full_text = []
        for i in text:
            full_text.append(self.upper_to_lower(i))
            full_text.append(self.lower_to_upper(i))
            if not i in self.lower_ascii and i not in self.upper_ascii:
                print(f"영문자외의 문자열을 입력하였습니다. {i}")
                full_text.append(i)
        full_text = ''.join(full_text)
        return full_text
'''
def print_code(ch):
    print(f"{ch} => {ord(ch)}")
    return ord(ch)
def print_char(ch):
    print(f"{ch} => {chr(ch)}")
    return chr(ch)
def to_upper(ch):
    if 97 <= ord(ch) <= 122:
        upper_code = print_char(print_code(ch)-32)
        print(f"{ch} => {upper_code}")
    return upper_code
def caesar_encode_ch(text,shift):
    return chr(ord(text) + shift)

def caesar_decode_ch(text,shift):
    return chr(ord(text) - shift)

def caesar_decode(text: str, shift: int = 3):
    full_text = []
    for i in text:
        caesar_code = caesar_decode_ch(i,shift)
        full_text.append(caesar_code)
    return "".join(full_text)

def caesar_encode(text: str, shift: int = 3):
    full_text = []
    for i in text:
        caesar_code = caesar_encode_ch(i,shift)
        full_text.append(caesar_code)
    return "".join(full_text)

def to_chosung(text):
    full_text = []
    for i in text:
        t = ord(i) - ord('가')
        k = t// (21 * 28)
        a = chr(k)
        print(t,k,a)
    return 
'''
def main():
    # text = input("문자열을 입력하시오.: ")
    # to_upper('a')
    # print(toggle_text(text))
    # print(caesar_encode('dsad'))
    a = Acsii()
    text = input("문자열을 입력하세요.: ")
    print(a.toggle_text(text)) # 과제 1번문제
    print(a.caesar_encode('dsad')) # 과제 2번문제
    print(a.caesar_decode('dsad')) # 과제 2번문제

    
if __name__ == "__main__":
    main()
