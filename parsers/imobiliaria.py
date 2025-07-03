import json
import xml.etree.ElementTree as ET

with open('parsers/imobiliaria.json') as json_file:
    parsed_data = json.load(json_file)

json_string = '{"imobiliaria": {"imovel": []}}'
parsed_from_string = json.loads(json_string)

imobiliaria = ET.Element('imobiliaria')

for imovel in parsed_data['imobiliaria']['imovel']:
    imovel_elem = ET.SubElement(imobiliaria, 'imovel')

    if imovel.get('id') is not None:
        imovel_elem.set('id', f"Imovel_{imovel['id']}")

    descricao = ET.SubElement(imovel_elem, 'descricao')
    descricao.text = imovel['descricao']

    proprietario = ET.SubElement(imovel_elem, 'proprietario')
    nome = ET.SubElement(proprietario, 'nome')
    nome.text = imovel['proprietario']['nome']

    prop = imovel['proprietario']

    if 'email' in prop:
        emails = prop['email']
        if isinstance(emails, list):
            for e in emails:
                email_elem = ET.SubElement(proprietario, 'email')
                email_elem.text = e
        else:
            email_elem = ET.SubElement(proprietario, 'email')
            email_elem.text = emails

    if 'telefone' in prop:
        telefones = prop['telefone']
        if isinstance(telefones, list):
            for t in telefones:
                tel_elem = ET.SubElement(proprietario, 'telefone')
                tel_elem.text = t
        else:
            tel_elem = ET.SubElement(proprietario, 'telefone')
            tel_elem.text = telefones

    endereco = ET.SubElement(imovel_elem, 'endereco')
    rua = ET.SubElement(endereco, 'rua')
    rua.text = imovel['endereco']['rua']
    bairro = ET.SubElement(endereco, 'bairro')
    bairro.text = imovel['endereco']['bairro']
    cidade = ET.SubElement(endereco, 'cidade')
    cidade.text = imovel['endereco']['cidade']

    if 'numero' in imovel['endereco']:
        numero = ET.SubElement(endereco, 'numero')
        numero.text = str(imovel['endereco']['numero'])

    caracteristicas = ET.SubElement(imovel_elem, 'caracteristicas')
    tamanho = ET.SubElement(caracteristicas, 'tamanho')
    tamanho.text = str(imovel['caracteristicas']['tamanho'])
    numQuartos = ET.SubElement(caracteristicas, 'numQuartos')
    numQuartos.text = str(imovel['caracteristicas']['numQuartos'])
    numBanheiros = ET.SubElement(caracteristicas, 'numBanheiros')
    numBanheiros.text = str(imovel['caracteristicas']['numBanheiros'])

    valor = ET.SubElement(imovel_elem, 'valor')
    valor.text = str(imovel['valor'])

xml_string = ET.tostring(imobiliaria, encoding='unicode')
print(xml_string)
