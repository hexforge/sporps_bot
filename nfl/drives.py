from collections import namedtuple
from functools import partial

from nfl.common import mapping_parse, parse_dataset

#List of plays
#List of drives


#data['2015092400']['drives']['1']['result']
#u'Safety'
#(Pdb) data['2015092400']['drives']['1']['start']
#{u'yrdln': u'WAS 19', u'team': u'WAS', u'qtr': 1, u'time': u'15:00'}
#(Pdb) data['2015092400']['drives']['1']['end']
#{u'yrdln': u'WAS 17', u'team': u'WAS', u'qtr': 1, u'time': u'12:47'}
#
#(Pdb) data['2015092400']['drives']['1']['postime']
#u'2:13'
#data['2015092400']['drives']['1']['numplays']
#7
#
#data['2015092400']['drives']['1']['penyds']
#
## first downs?
#(Pdb) data['2015092400']['drives']['1']['fds']
#0
#data['2015092400']['drives']['1']['ydsgained']
#8
#data['2015092400']['drives']['1']['plays'].keys()
#[u'159', u'57', u'35', u'195', u'137', u'102', u'81']


#---
# Team sats
#---


    #game_flow:
    #    field_position
    #    time
    #    team in possesion
    #    possesion time
    #    game_clock
    #    a drive :)
    #    a play

    # percentage of drives that end in a td.
    # percentage of drives that get turned over
    # percentage of drives that that end in a punt
    # percentage of drives that end in kick

    # How many plays before the turned over.
    # Average number of plays to a 1st down.

    # Average throw targets long  (player targets too)
    # Average throw targets med
    # Average throw targets short

    # pass to rush percentage                               # And graph over time
    # pass to rush percentage when behind
    # pass to rush percentage when even first x mins.       # And graph over time

    # Per team and combined.

    # Want to predict the number of targets and length, predict the fantasy points.


#X vs Y in cat z.  Rate them both.  Just take an average.
    # What is the most likley




state_flds = ['yrdln', 'team', 'qtr', 'time']
state_nt = namedtuple('state_nt', state_flds)
parse_state = partial(parse_dataset, state_nt)


def parse_plays(plays_data):
    pass
    x = """
    for play_id, play_data in sorted(plays_data.items()):
        starting_field_position
        down
        time
        ydsnet
        ydstogo
        team_in_possesion
        desc
        note
        #sp??
        players
            player_id, player_data # sorted by sequence
                ['playerName', 'clubcode', 'yards', 'statId', 'sequence'}]


    import pdb; pdb.set_trace()
    """


drive_mapping = {
    'id': ('id', None),
    'team': ('posteam' , None),
    'start_state': ('start' , parse_state),
    'end_state': ('end' , parse_state),
    'time_delta': ('postime' , None),
    'first_downs_maybe': ('fds' , None),
    'result': ('result' , None),
    'plays': ('plays' , parse_plays),
    'num_plays': ('numplays' , None),
    'penalty_yards': ('penyds' , None),
    'yards_gained': ('ydsgained' , None),
}
drive_nt = namedtuple('drive_nt', drive_mapping.keys())

def parse_drives(drive_data):
    drives = []
    for drive_id, drive_data in sorted(drive_data.items()):
        if drive_id == 'crntdrv':
            continue

        drive_data['id'] = drive_id
        drive = mapping_parse(drive_mapping, drive_nt, drive_data)
        drives.append(drive)

    return drives