require 'rest-client'
require 'json'
class Translate
    attr_accessor :text

    def initialize(text,idioma)
        @url='https://translate.yandex.net/api/v1.5/tr.json/translate'
        @api=#Passe aqui sua key
        @texto=text 
        @idioma='pt-' + idioma
        @text_language=translate
    end

    def write 
        time=Time.new
        archive=Time.strftime("%d-%m-%y_%H:%M") + ".txt"
        File.open(archive, 'w') do |line_ya|
            line_ya.puts @texto
            line_ya print @text_language
        end
    end


    private 

    def translate
        response=RestClient.get(@url, {key:@api, text:@texto, lang:@idioma})
        JSON.parse(response).values.flatten.last
    end
end