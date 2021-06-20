require "cpf_cnpj"
def validador cpf
    if CPF.valid?(cpf) == true
        puts "O cpf -> #{cpf} é valido"
    else 
        puts "Cpf invalido"
        print "Deseja gerar 1 cpf? 1(sim)/0(nao)>> "
        opcao=gets.chomp.to_i
        if opcao == 1
            gerar
        else
            puts "Saindo..."
            puts "Script By: Exodus236(Silva)"
        end
    end
end

def gerar
        puts "Gerando..."
        cpf = CPF.generate
        puts cpf
        print "Deseja checar se estar válido? 1(sim)/0(nao)>>  "
        opcao=gets.chomp.to_i
        if opcao == 1
            validador cpf
        else 
            puts "Okay saindo..."
            puts "Script By: Exodus236(Silva)"
        end
end

print "Passe o cpf: "
cpfzinho=gets.chomp.to_i
validador cpfzinho
