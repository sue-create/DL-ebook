#pip install googletrans==4.0.0-rc1
import googletrans
translator = googletrans.Translator()

words = {}
def registration():
    s = input('등록할 단어: ')
    if s in words:
        print('등록된 단어임')
    else:
        words[s]= translator.translate(s,dest='en').text
def quiz():
    for key, value in words.items():
        ans = input(key+' 영어 이름은? ')
        if ans == value:
            print('O')
        else:
            print('X')
while True:
    sel = int(input('1.등록 2.퀴즈 3.종료:'))
    if sel==3:
        print('종료')
        break
    elif sel==1:
        registration()
    elif sel==2:
        quiz()
    else:
        print('잘못 입력')
