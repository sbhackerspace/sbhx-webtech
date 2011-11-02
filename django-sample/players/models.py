from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=40, blank=True)
    player_id = models.TextField(blank=True)
    weight = models.IntegerField(null=True)
    birth_year = models.IntegerField(null=True)

    def __unicode__(self):
        return self.name

class AllStarTeamMember(models.Model):
    player = models.ForeignKey(Player, related_name='teams')
    year = models.IntegerField()
    league = models.CharField(max_length=2, blank=True)

    def __unicode__(self):
        return "{0}-{1}".format(self.player.name, self.year)

    def age_on_team(self):
        return self.year - self.player.birth_year
