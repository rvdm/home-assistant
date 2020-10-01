import hassapi as hass
from datetime import datetime

#- switch on espresso machine when waking up
#- switch on espresso machine at configured time when home working
#- don't switch on when
#    - working in the office (i.e. woke up before threshold)
#    - holiday
#    - weekend

class Espresso(hass.Hass):

    def initialize(self):
        # get sensors to use
        self.sleep_sensor = self.args['sleep_sensor']
        self.waketime_sensor = self.args['waketime_sensor']
        self.log("Sensor: %s and %s" % (self.sleep_sensor,self.waketime_sensor))
        # get espresso switch and time
        self.espresso_switch = self.args['espresso_switch']
        self.espresso_time = self.args['espresso_time']
        self.wfh_threshold = self.parse_datetime(self.args['wfh_threshold'])
        self.log("Will use %s to switch on espresso machine at %s" % (self.espresso_switch, self.espresso_time))

        self.listen_state(self.alarm_event,self.sleep_sensor)
        self.run_daily(self.maybe_espresso,self.espresso_time)
        self.log("Espresso initialized")

    def alarm_event(self, entity, attribute, old, new, kwargs):
        self.log("{} changed to {}".format(self.friendly_name(entity), new))
        # if the entity switched off, state is sleeping, else state is awake
        now = datetime.now()
        if (new == "on"):
            self.log("Wake-up triggered by alarm, switching %s to on" % self.espresso_switch)
            self.set_state(self.espresso_switch, state="on")

    def maybe_espresso(self):
        # decision time!
        # wake-up time before configured threshold? Probably not wfh today.
        self.waketime = self.get_state(self.waketime_sensor,attribute="changed")
        workday = self.get_state("binary_sensor.workday_sensor")

        if (self.waketime < self.wfh_threshold):
            self.log("Woke up too early, not switching on espresso machine")
        else:
            if (workday == "on"):
                self.log("Time is right and we're working, switching on espresso machine")
                self.set_state(self.espresso_switch, state="on")
