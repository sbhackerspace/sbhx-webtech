class AddYearToAllStarTeamMember < ActiveRecord::Migration
  def self.up
    add_column :all_star_team_members, :year, :integer
  end

  def self.down
    remove_column :all_star_team_members, :year
  end
end
