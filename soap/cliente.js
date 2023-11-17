const soap = require('soap');

const url = 'http://localhost:8000/?wsdl';

soap.createClient(url, (err, client) => {
  if (err) {
    console.error(err);
    return;
  }

  // Função 1 com dois argumentos
  const f1Args = { a: 'Ola ', b: 'Mundo' };
  client.concat(f1Args, (err, result) => {
    if (err) {
      console.error('Erro:', err);
      return;
    }
  console.log('Resultado:', result.concatResult);

  // Função 2 com um argumento
  const f2Args = {n: 10};
  client.contagem_regressiva(f2Args, (err, result) => {
    if (err) {
      console.error('Erro:', err);
      return;
    }
  console.log('Resultado:', result.contagem_regressivaResult);

  // Função 3 sem argumentos
  client.ping({}, (err, result) => {
    if (err) {
      console.error('Erro:', err);
      return;
    }
  console.log('Resultado:', result.pingResult);

  // Lista todos os métodos disponíveis
  const methods = [];

  for (const method in client) {
    if (typeof client[method] === 'function') {
      methods.push(method);
    }
  }

  // Imprime a lista de métodos
  console.log("Métodos disponíveis:");
  methods.forEach(method => {
  console.log(`- ${method}`);
        });
      });
    });
  });
});
