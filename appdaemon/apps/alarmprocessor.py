import hassapi as hass
from datetime import datetime

class AlarmProcessor(hass.Hass):

  def initialize(self):
     self.sleep_sensor = self.args['sleep_sensor']
     self.waketime_sensor = self.args['waketime_sensor']
     self.log("Sensors: %s and %s" % (self.sleep_sensor,self.waketime_sensor))

     self.listen_state(self.alarm_event,self.sleep_sensor)

     self.log("AlarmProcessor initialized")

  def alarm_event(self, entity, attribute, old, new, kwargs):
      self.log("{} changed to {}".format(self.friendly_name(entity), new))
      # if the entity switched off, state is sleeping, else state is awake
      now = datetime.now()
      if(new == "off"):
          self.set_state(self.waketime_sensor, state="sleeping", attributes = {"changed": now})
      if(new == "on"):
          self.set_state(self.waketime_sensor, state="awake", attributes = {"changed": now})
