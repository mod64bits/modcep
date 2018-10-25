############################################
# Marcio O. de Deus                        #
#Busca Por cep 1.0                         #
############################################
import requests

def main():


    print("####################")
    print("### Consulta cep ###")
    print("####################")
    print()

    cep = input("Digite o CEP: ")

    if len(cep) != 8:
        print("Quantidade de Digito Inválido!")
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

    cep_data = request.json()

    if 'erro' not in cep_data:
        print('CEP: {}'.format(cep_data['cep']))
        print('UF: {}'.format(cep_data['uf']))
        print('LOCALIDADE: {}'.format(cep_data['localidade']))
        print('LOGRADOURO: {}'.format(cep_data['logradouro']))
        print('BAIRRO: {}'.format(cep_data['bairro']))
        print('COMPLEMENTO: {}'.format(cep_data['complemento']))
        print("===============> Fim <========================")
    else:
        print("O CEP {} não Existe!".format(cep))

    option = int(input("Deseja uma realizar nova Consulta?\n1. Sim\n2. Não\n "))
    if option == 1:
        main()
    else:
        print("===> Saindo <===")

if __name__ == '__main__':
    main()



