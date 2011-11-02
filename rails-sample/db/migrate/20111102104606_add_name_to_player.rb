class AddNameToPlayer < ActiveRecord::Migration
  def self.up
    add_column :players, :name, :string
  end

  def self.down
    remove_column :players, :name
  end
end
