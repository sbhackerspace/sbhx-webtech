class AddLeagueToAllStarTeamMember < ActiveRecord::Migration
  def self.up
    add_column :all_star_team_members, :league, :string
  end

  def self.down
    remove_column :all_star_team_members, :league
  end
end
