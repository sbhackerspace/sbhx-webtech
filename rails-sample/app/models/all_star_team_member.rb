class AllStarTeamMember < ActiveRecord::Base
  has_one :player


  def age_on_team
      self.year - self.player.birth_year
  end

end
