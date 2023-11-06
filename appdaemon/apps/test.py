from appdaemon.plugins.hass.hassapi import Hass

class Location(Hass):
    def initialize(self):
        trackers = self.get_trackers()
        for tracker in trackers:
            if tracker == 'device_tracker.gabriella_martin':
                self.g_home = True if self.get_state(tracker) == 'home' else False
            elif tracker == 'device_tracker.lorenzo_speariett':
                self.l_home = True if self.get_state(tracker) == 'home' else False
    
    def everyone_home(self):
        return self.g_home and self.l_home
    
    def l_home_g_away(self):
        return self.l_home and not self.g_home
    
    def g_home_l_away(self):
        return self.g_home and not self.l_home
    
    def everyone_away(self):
        return not (self.g_home and self.l_home)

