import price
import subprocess
from pygame import mixer
from time import sleep

ERROR_MESSAGE = 'Something went wrong. Trying again...'


def play_and_popup(mes, track=None):
    """
    Allows to show pop-up notification and play audiotrack.
    """
    if track:
        mixer.music.load(f"/home/askhat/Downloads/{track}")
        mixer.music.play()
    subprocess.Popen(['notify-send', mes])


def notify():

    status = False
    # Try to fetch BTC currency to a successful conclusion.
    while not status:
        current_price, status = price.get_current_price()
        if status:
            play_and_popup(mes=f"Current price of BTC is {current_price}$")
        else:
            play_and_popup(mes=ERROR_MESSAGE)
        sleep(15)

    # After successful fetching initial value of currency:
    # Initialization "mixer" from "pygame" for playing audio
    mixer.init()
    # And start loop for check price
    while True:
        # Wait for 3 minutes and go on
        sleep(20)
        p, status = price.get_current_price()
        if status:
            if float(p) < float(current_price) - 1:
                # Play fragment from song 
                # "Heart Of A Coward - Shade" or from another
                # and show painfull pop-up notification.
                play_and_popup(
                    track='suffer_bitch.mp3', 
                    mes=f'BTC fell down to {p}$ from {current_price}$'
                )
                current_price = p
            elif float(p) > float(current_price) + 1:
                # Play fragment from song 
                # "The Tokens - The Lion Sleeps Tonight" or from another
                # and show cheer pop-up notification.
                play_and_popup(
                    track='the_lion_sleeps_tonight.mp3', 
                    mes=f'BTC took off to {p}$ from {current_price}$'
                )
                current_price = p
            else:
                print(p)
        else:
            play_and_popup(mes=ERROR_MESSAGE)


if __name__ == '__main__':
    notify()
