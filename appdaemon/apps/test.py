from appdaemon.plugins.hass.hassapi import Hass

LIFE_360_TRACKERS = ['device_tracker.gabriella_martin', 
                     'device_tracker.lorenzo_speariett']

class Location(Hass):
    def initialize(self):
        trackers = self.get_trackers()
        for tracker in trackers:
            if tracker == 'device_tracker.gabriella_martin':
                g_home = True if self.get_state(tracker) == 'home' else False
            elif tracker == 'device_tracker.lorenzo_speariett':
                l_home = True if self.get_state(tracker) == 'home' else False
 
