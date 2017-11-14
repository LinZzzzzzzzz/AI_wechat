
import itchat
import time


GOD='Paco'  #creator
chatroom_name='约系统'    #chatroom name


#target_time[0] is hour; target_time[1] is minute; target_time[2] is second;
target_time = [13,0,0]


#log in WeChat
itchat.auto_login(hotReload=True)
itchat.get_chatrooms(update=True)
chatroom_name_number = itchat.search_chatrooms(name=chatroom_name)[0]['UserName']
#f =  open("chatroom_name_number.txt", "a+")
#.write(chatroom_name_number+'\n')
#f.close()


#communication between creator and AI
@itchat.msg_register(itchat.content.TEXT, isFriendChat=True, isGroupChat=False)
def apple_content(msg):
    if msg['User']['NickName'] == GOD:
        #main program
        Timer(target_time) #activate Timer
        itchat.send(msg['Text'], toUserName=chatroom_name_number)


#Timer
def Timer(target_time):
    target_time_value = 60*60*target_time[0] + 60*target_time[1] + target_time[2]
    while True:
        now = time.localtime()
        now_value = 60*60*now[3] + 60*now[4] + now[5]
        difference_value = target_time_value - now_value
        if difference_value < 0:
            time.sleep(24*60*60 - now_value + 1)
            pass
        elif difference_value > 2:
            time.sleep(difference_value//2)
            pass
        else:
            if difference_value == 0:
                break


itchat.run()
