#!/usr/bin/env ruby
# Steve Phillips / elimisteve
# 2011.11.02

require 'csv'    

task :import_players => :environment do

  csv_text = CSV.read('lahman58-csv/Master.csv')
  csv_text.each do |row|

    name = "#{row[16]} #{row[17]}"
    player_id = row[1]
    birth_year = row[4]
    weight = row[21]

    #puts name, player_id, birth_year, weight

    Player.create!(:name => name, :player_id => player_id,
                   :birth_year => birth_year, :weight => weight)
  end
end

task :import_allstars => :environment do

  csv_text = CSV.read('lahman58-csv/Allstar.csv')
  csv_text.each do |row|

    player = Player.where(:player_id => row[0]).first
    year = row[1]
    league = row[2]

    #puts player, year, league

    AllStarTeamMember.create!(:player => player, :year => year, :league => league)
  end
end
