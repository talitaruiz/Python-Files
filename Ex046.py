from time import sleep
import emoji
for count in range(10,-1,-1):
    print(count)
    sleep(0.5)
print('\033[31;43m Muitos fogos !!\033[m')
print(emoji.emojize('FOGOS :boom:', use_aliases=True))