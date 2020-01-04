class MyError(Exception):
    pass

def say_nick(nick):
    if nick == 'fool':
        raise MyError()
    print(nick)

try:
    say_nick("angel")
    say_nick("fool")
except MyError:
    print("Don't use that nickname")
# except MyError as e:  오류메세지
#    print(e)