


from btpy.src.btpy.Btpy import*
from chat_bot.ChatBot import ChatBot
from View import View

def main():
    r = ""
    #--------------------------------------


    view = View()
    chat_bot = ChatBot()
    view.receive(
            chat_bot.request())
    def user_action(e):
        chat_bot.receibe(view.request())
        print(chat_bot.write())
        chat_bot.update()
        view.receive(
            chat_bot.request())
    view.input.add_enter_listener(
        user_action)
    view.start()

    #--------------------------------------
    print(r)

main()