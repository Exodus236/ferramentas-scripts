require "cpf_cnpj"
def validador cpf
    if CPF.valid?(cpf) == true
        puts "O cpf -> #{cpf} e valido"
    else 
        puts "Cpf invalido"
        print "Deseja gerar 1 cpf? 1(sim)/0(nao)>> "
        opcao=gets.chomp.to_i
        if opcao == 1
            gerar
        else
            puts "Saindo..."
        end
    end
end

def gerar
        puts "Gerando..."
        cpf = CPF.generate
        puts cpf
        print "Deseja checar se estar valido? 1(sim)/0(nao)>>  "
        opcao=gets.chomp.to_i
        if opcao == 1
            validador cpf
        else 
            puts "Okay saindo..."
        end
end

print "Passe o cpf: "
cpfzinho=gets.chomp.to_i
validador cpfzinho
