class AddBirthYearToPlayer < ActiveRecord::Migration
  def self.up
    add_column :players, :birth_year, :integer
  end

  def self.down
    remove_column :players, :birth_year
  end
end
