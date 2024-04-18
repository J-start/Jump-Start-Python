# Documentação Selic
## O retorno da api tem o seguinte formato:
### `{'data': 'XX/XX/XXXX', 'valor': '0.XXXX'}`
## Explicação
`resp[0]['data'] => data selic`<br>
`resp[0]['valor'] => valor da selic da selic na ['data']`
## Dependendo do horário a data pode ser do dia anterior, então é preciso agendar uma atualização do banco à partir do horário que a api é atualizada.