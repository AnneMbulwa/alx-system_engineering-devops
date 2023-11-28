#!/usr/bin/env ruby
#should output sender, receiver and flags
puts ARGV[0].scan(?<=from:|to:|flags:)(.+?)(?=\])/).join(",")
