# app-enviaramal-prod
App feito para enviar uma lista de ramais via API para o banco de dados Sankhya, foi usado para ja deixar definido como padrão o ramal de cada loja

Inicialmente é adquirido o token, apos isso o token é guardado pois vai ser usado em todas as req. Então é feita a requisição para adquirir os ramais existentes, e então é feita o for para mandar cara ramal, conforme é informado no input. Mas para cada requisição que é feita, é verificado no array se o Ramal ja existe, se sim ele não é inserido. 

Os dados importantes foram tirados por questões de segurança
