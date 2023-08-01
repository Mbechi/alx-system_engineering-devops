#!/usr/bin/env ruby

# Check if the script is provided with an argument
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <log_file>"
  exit 1
end

# Regular expression to extract the required information from the log line
regex = /\[from:([\w\s+:]+?)\] \[to:([\+\d]+?)\] \[flags:(.*?)\]/

# Get the log file name from the command line argument
log_file = ARGV[0]

# Read the log file line by line
File.foreach(log_file) do |line|
  match_result = line.match(regex)
  if match_result
    sender = match_result[1]
    receiver = match_result[2]
    flags = match_result[3]
    puts "#{sender},#{receiver},#{flags}"
  end
end
