from time import sleep
import emoji
amp = emoji.emojize(':party_popper:')
for c in range(10, -1, -1):
    print(amp, c, amp)
    sleep(1)
jo = emoji.emojize(':collision:')
print('BUM! {}'.format(jo))