require "requests/sugar"
require 'uri'

def painel
    print "1(http)\n2(https)\n3(Erros)\n>> "
    pergunta=gets.chomp
    if pergunta == '1'
        http
    elsif pergunta == '2'
        https
    elsif pergunta == '3'
        erros
    end
end

def erros
    puts "Moved Permanently = 301 !"
    sleep(0.4)
    puts "OpenSSL::SSL::SSLError = https ou http ?? "
    puts "Connection refused = Conexao recusada !"
    sleep(0.5)
    puts "Vou tratar os erros ainda!"
    sleep(0.3)
    puts "Voltando..."
    painel
end

def back
    print "Deseja continuar o request s/n\n>> "
    pergunta=gets.chomp
    if pergunta == 's'
        sleep(0.5)
        painel
    elsif pergunta == 'n'
        sleep(0.3)
        exit
    end
end

def http 
    print "Alvo para Request \n>> "
    alvo=gets.chomp
    res=Requests.get("http://#{alvo}")
    puts "Status -> #{res.status}"
    criararquivo
end

def https
    print "Alvo para Request \n>> "
    alvo=gets.chomp
    res=Requests.get("https://#{alvo}")
    puts "Status -> #{res.status}"
    back
end

def criararquivo
    print "Deseja salva o diretorio? s/n"
    pergunta=gets.chomp
    if pergunta == 's'
        arquivo=File.new("arquivo.txt", "w")
        arquivo.puts "Salvo"
        back
    elsif pergunta == 'n'
        back
    end
end

painel

