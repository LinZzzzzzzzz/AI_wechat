#-*- coding:utf-8 –*-

import itchat

boss='Zcy' #start organizer
GOD='Paco'  #creator

#original file
f =  open("booking_content.txt", "w+")
f.close()

#微信中的数据类型：
#   文本 itchat.content.TEXT
#   图片 itchat.content.PICTURE
#   语音 itchat.content.RECORDING
#   名片 itchat.content.CARD

#communication between creator and AI
@itchat.msg_register(itchat.content.TEXT, isFriendChat=True, isGroupChat=False)
def apple_content(msg):
    if msg['User']['NickName'] == GOD:
        f =  open("booking_content.txt", "w+")
        f.write(msg['Text'])
        f.close()


#communication between AI and start organizer
@itchat.msg_register(itchat.content.TEXT, isFriendChat=False, isGroupChat=True)
def booking(msg):
    if msg['Text'] == u'约系统' and msg['ActualNickName'] == boss:
        f = open("booking_content.txt", "r+")
        apple = f.readline()
        f.close()
        f =  open("booking_content.txt", "w+")
        f.close()
        if apple != '':
            #在字符串前加‘u’前缀可直接声明unicode字符串
            return apple


itchat.auto_login(hotReload=True)
itchat.run()
