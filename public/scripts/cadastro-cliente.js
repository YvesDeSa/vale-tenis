

document.addEventListener('DOMContentLoaded', function() {
 
  // let produtos = JSON.parse(localStorage.getItem('produtos')) || [];

  const urlParams = new URLSearchParams(window.location.search);
  const clienteId = urlParams.get('id');
  const form = document.getElementById('clienteForm');
  const pageTitle = document.getElementById('pageTitle');

  if (clienteId) {
    const cliente = clientes.find(c => c.id == clienteId);
    if (cliente) {
      document.getElementById('clienteId').value = cliente.id;
      document.getElementById('nome').value = cliente.nome;
      document.getElementById('sobrenome').value = cliente.sobrenome;
      document.getElementById('sexo').value = cliente.sexo;
      document.getElementById('dataNascimento').value = cliente.dataNascimento;
      document.getElementById('cpf').value = cliente.cpf;
      document.getElementById('celular').value = cliente.celular;
      document.getElementById('email').value = cliente.email;
      document.getElementById('senha').value = cliente.senha;
      
      pageTitle.innerText = 'Editar Cliente';
      form.setAttribute('data-id', cliente.id);
    }
  }
 
  form.addEventListener('submit', async function(e) {
    e.preventDefault();


    const id = document.getElementById('clienteId').value;
    const nome = document.getElementById('nome').value;
    const sobrenome = document.getElementById('sobrenome').value;
    const sexo = document.getElementById('sexo').value;
    const dataNascimento = document.getElementById('dataNascimento').value;
    const cpf = document.getElementById('cpf').value;
    const celular = document.getElementById('celular').value;
    const email = document.getElementById('email').value;
    const senha = document.getElementById('senha').value;
    const confirmarSenha = document.getElementById('confirmarSenha').value;
    const confirmarSenhaInput = document.getElementById('confirmarSenha');
    
    if(confirmarSenha !== senha){
      confirmarSenhaInput.style.borderColor = 'red';
      let confirmarSenhaLabel = document.getElementById('confirmarSenhaLabel');
      if (!confirmarSenhaLabel) {
          confirmarSenhaLabel = document.createElement('label');
          confirmarSenhaLabel.setAttribute('id', 'confirmarSenhaLabel');
          confirmarSenhaLabel.style.color = 'red'; 
          confirmarSenhaLabel.innerText = 'A senha confirmada não está correta.';
          confirmarSenhaLabel.style.display = 'block'; 
          confirmarSenhaLabel.style.marginTop = '5px'; 
          confirmarSenhaLabel.style.textAlign = 'center'; 
          confirmarSenhaInput.parentNode.insertBefore(confirmarSenhaLabel, confirmarSenhaInput.nextSibling);
      }
      return;
  }

    const clienteData = {
      id: 0,
      nome:nome,
      sobrenome:sobrenome,
      sexo:sexo,
      dataNascimento:dataNascimento,
      cpf:cpf,
      celular:celular,
      email:email,
      senha:senha
    };

    await axios.post('http://127.0.0.1:8000/cliente', clienteData);
    alert('Cliente cadastrado com sucesso.');
    window.location.href = 'cliente.html';
  });
});
