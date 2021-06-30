require_relative "translate.rb"

def input 
    print "Passe a sigla do idioma: "
    @language=gets.chomp
    print "Passe o texto que deseja traduzir: "
    @text=gets.chomp
end

input 

tradutor=Translate.new(@text,@language)
puts tradutor.text_language