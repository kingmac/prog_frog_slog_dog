class Monster:
  def__init__(Self, **kwargs):
    self.hit_points = kwargs.get('hit_points', 1)
    self.weapon = kwargs.get('weapon', 'sword')
    self.color = kwargs.get('color', 'red')
    self.sound = kwargs.get('sound', 'roar')
  def battlecry(self):
    return self.sound.upper()
