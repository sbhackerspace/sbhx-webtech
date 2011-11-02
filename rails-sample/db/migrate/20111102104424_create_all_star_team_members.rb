class CreateAllStarTeamMembers < ActiveRecord::Migration
  def self.up
    create_table :all_star_team_members do |t|

      t.timestamps
    end
  end

  def self.down
    drop_table :all_star_team_members
  end
end
