#!/usr/bin/env ruby

# Check if the script is provided with an argument
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

# Regular expression to match a string that starts with 'h', ends with 'n',
# and can have any single character in between
regex = /^h.n$/

# Get the argument from the command line
input_string = ARGV[0]

# Match the regular expression against the input string
match_result = input_string.match(regex)

# Print the matched substring if found
if match_result
  puts match_result[0]
else
  puts ''
end
