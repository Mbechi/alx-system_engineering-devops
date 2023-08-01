#!/usr/bin/env ruby

# Check if the script is provided with an argument
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

# Regular expression to match "hbtn" with "t" repeated between 2 and 5 times
regex = /hbt+t+n/

# Get the argument from the command line
input_string = ARGV[0]

# Match the regular expression against the input string
match_result = input_string.scan(regex)

# Print the matched substrings if found
match_result.each do |match|
  puts match
end
