import time

from computersandcoding.helpers import clear, is_int
import computersandcoding.battlegames.vitalmessage as vital_message
import computersandcoding.battlegames.robotmissile as robot_missile
import computersandcoding.battlegames.shootout as shootout
import computersandcoding.battlegames.deserttankbattle as desert_tank_battle


def run() -> None:
    while True:
        clear()

        print('''$;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;+$
$.................................................................................................:X
$....xXXXXx+:...:......................................................................:..:;+xxx:..x
$....xXXXXXXX;..+XXXx;;+;:.......:...:...............:......................:;;+:+xxxXXx.;XXXXXX:..x
$....xXXx+XXXx:.+XXXX++XXXXXX++XXXXXx+Xxx;..;;;;;;;....:::;..:+xx+..:xXXx:..xXX+.+XXXXXx:XXXXXXX:..x
$....xXX+:xXXx:.xXXXX++XxXXXX++XXXXXX;xXx...:XXXXXX:;XXXXXx..;XXX+...;XXx:.:XXX;.;XXx;xx;XXX:.;x:..x
$....xXX+;XXX+.:XXxXXx:.:XXX:::.+XX;;:xXx...:XX:.:+;XX;..:+..+XXXX:..:xXX+:xXXX;.;XXx..::XXX;......x
$...:XXXXXXX+..;Xx+XXx:.:XXX:...+XX:.:xXx...:XX;;;.xX+.......xX+XX;..;XXXXXXXXX;.;XXx.;..xXXx:.....x
$...:XXXXXXXX;.+Xx:XXX;.:XXX:...xXX:.:xXx...:XXXX+.xX+..+++.:X+:XXx..;Xx+XXxxXX;.;XXXXx..:xXXx:....x
$...:XXX+;XXXx:xXXXXXX;.:XXX:...xXX:.:xXx...:XX:...xX+..+X+.+XXXXXX:.;Xx.xx:xXX;.;XXXxx...;XXXx....x
$...:XXX+.+XXX;XXXXXXX+.:XXX....xXX:.:xXx.;x:XX:.;xxXX;.xX+.XX;:+XX;.;Xx.::.+XX;.;XXx......;XXX+...x
$...:XXX+.+XXX+XX;.;XXx.:XXX....xXX:.:xXXXXX:XXXXXX:xXXXXX+;Xx:.:XXX.;Xx....+XX;.;XXx..+:;..+XXX:..x
$...:XXX+;XXXxxXX:.:XXX;:XXX;...XXX+.;xxxxx++++++++..:;+++;+x+:.:XXX:;Xx....xXX;.;XXXxXx;X;.:xXX+..x
$...:XXXXXXXX;+Xx..;XXXx:+;;:..............................................:xXX+.xXXXXXx;XXXXXXX+..x
$...:XXXXXXx.;Xx+:......:........................................................:;xXXXx;XXXXXXX::.x
$...;XXx+:.............................................................................::;xXXX+:;..x
$....................(https://usborne.com/gb/books/computer-and-coding-books)...........:+xxx++:...x
$.................................................................................................:X''')

        print()
        print('WHICH GAME WOULD YOU LIKE TO PLAY?\n')
        print('0. EXIT')
        print('1. ROBOT MISSILE')
        print('2. VITAL MESSAGE')
        print('3. SHOOTOUT')
        print('4. DESERT TANK BATTLE')

        selected_game = -1
        while not 0 <= selected_game <= 4:
            selected_game_input = input('> ')
            if is_int(selected_game_input):
                selected_game = int(selected_game_input)

        if selected_game == 0:
            return
        elif selected_game == 1:
            robot_missile.run()
        elif selected_game == 2:
            vital_message.run()
        elif selected_game == 3:
            shootout.run()
        elif selected_game == 4:
            desert_tank_battle.run()

        time.sleep(3)


if __name__ == '__main__':
    run()
