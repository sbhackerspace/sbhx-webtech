class AddWeightToPlayer < ActiveRecord::Migration
  def self.up
    add_column :players, :weight, :integer
  end

  def self.down
    remove_column :players, :weight
  end
end
