from computersandcoding.battlegames import index
from computersandcoding.helpers import clear

if __name__ == '__main__':
    try:
        index.run()
    except KeyboardInterrupt:
        clear()
        print('THANKS FOR PLAYING')
