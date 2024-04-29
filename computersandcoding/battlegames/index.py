from computersandcoding.helpers import clear, is_int
import computersandcoding.battlegames.vitalmessage as vital_message


def run() -> None:
    clear()

    print('''$;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;+$
$.................................................................................................:X
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
$.......................................................................................:+xxx++:...x
$.................................................................................................:X''')

    print('\n\n')
    print('WHICH GAME WOULD YOU LIKE TO PLAY?\n')
    print('1. VITAL MESSAGE')

    selected_game = 0
    while not 1 <= selected_game <= 1:
        selected_game_input = input('> ')
        if is_int(selected_game_input):
            selected_game = int(selected_game_input)

    if selected_game == 1:
        vital_message.run()


if __name__ == '__main__':
    run()