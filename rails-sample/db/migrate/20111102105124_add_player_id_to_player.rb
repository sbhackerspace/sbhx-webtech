class AddPlayerIdToPlayer < ActiveRecord::Migration
  def self.up
    add_column :players, :player_id, :text
  end

  def self.down
    remove_column :players, :player_id
  end
end
