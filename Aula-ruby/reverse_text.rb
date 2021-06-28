module Decoration

    def inverter text 
        decoration="-" * 100
        sleep 0.2
        puts "\nTexto Invertido"
        puts decoration
        puts text
        puts decoration
    end

    def no_inverter text 
        decoration="-" * 100
        sleep 0.2
        puts "\nTexto Certo"
        puts decoration
        puts text
        puts decoration
        back
    end 

end


module Reverseword

    include Decoration
    
    def self.text text
        inverter "#{text.reverse.to_s}" 
        no_inverter "#{text}"
    end
end


def question 
    include Decoration
    sleep 0.2
    print "Passe o texto para reverter: "
    question=gets.chomp
    reverse=Reverseword::text "#{question}"
end

def back
    print "Deseja reverter mais alguma palavra? s/n \n>> "
    question_one=gets.chomp
    if question_one == 's'
        sleep 0.2
        question
    elsif question_one == 'Sim'
        sleep 0.2
        question
    elsif question_one == 'n'
        puts "Script By : Exodus236(silva)"
        sleep 0.2
        puts "Saindo..."
        exit
    elsif question_one == 'Nao'
        puts "Script By : Exodus236(silva)"
        sleep 0.2
        puts "Saindo..."
        exit
    else
        puts ">> s (Sim) /n (nao) <<"
        back
    end
end

question 
