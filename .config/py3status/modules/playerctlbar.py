# py3status module for playerctl

import subprocess

def run(*cmdlist):
    return subprocess.run(
            cmdlist,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL).stdout.decode()

def player_args(players):
    if not players:
        return 'playerctl',
    else:
        return 'playerctl', '-p', players

def get_status(players):
    status = run(*player_args(players), 'status')[:-1]
    if status in ('Playing', 'Paused'):
        return status
    return ''

def get_info(players, fmt):
    args = 'metadata', '--format', f'{fmt}'
    return run(*player_args(players), *args).strip()

class Py3status:
    players         = ''
    play_format     = '  {{ artist }} - {{ title }}'
    pause_format    = '  {{ artist }} - {{ title }}'

    def spotbar(self):
        text_format = "[[ {info} ]]|[ {status} ]"

        params = {'status': get_status(self.players)}

        if params['status'] == 'Playing': 
            params['info'] = get_info(self.players, self.play_format)
        else:
            params['info'] = get_info(self.players, self.pause_format)
            
        if params['info'] == '/ -':
            parmas['info'] = None

        return {
            'full_text': self.py3.safe_format(text_format, params),
            'cached_until': self.py3.time_in(seconds=0)
        }

    def on_click(self, event):
        if event['button'] == 1:
            run('playerctl', 'play-pause')
