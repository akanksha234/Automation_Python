class LawFirm:
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers

  def __len__(self):
    return len(self.lawyers)

  def __contains__(self, lawyer):
    if lawyer in self.lawyers:
      return True
    else:
      return False

  def __append__(self, lawyer):
      self.lawyers.append(lawyer)


d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])
d_and_p.append("Akanksha")