document.addEventListener('DOMContentLoaded', async function() {

    // function formatarGenero(genero) {
    //   let partes = [];
    //   if (genero.adulto) partes.push(`Adulto - ${genero.adulto}`);
    //   if (genero.infantil) partes.push(`Infantil - ${genero.infantil}`);
    //   return partes.join(", ");
    // }
  
    async function renderizarClientes() {
  
      const response = await axios.get('http://localhost:8000/clientes');
      const clientes = response.data; 
      
      const listaClientesEl = document.getElementById('listaClientes');
      listaClientesEl.innerHTML = '';
  
      clientes.forEach(cliente => {
        const tr = document.createElement('tr');
        tr.classList.add('cliente');
        tr.innerHTML = `
                <td>${cliente.nome}</td>
                <td>${cliente.sobrenome}</td>
                <td>${cliente.sexo}</td>
                <td>${cliente.dataNascimento}</td>
                <td>${cliente.cpf}</td>
                <td>${cliente.celular}</td>
                <td>${cliente.email}</td>
                
                <td>
                      <a href="cliente.html?id=${cliente.id}" class="btn btn-outline-primary btn-sm me-2">
                          <i class="bi bi-pencil"></i>
                      </a>
                      <button onclick="excluirCliente(${cliente.id})" class="btn btn-outline-danger btn-sm">
                          <i class="bi bi-trash"></i>
                      </button>
                </td>
              `;
        listaClientesEl.appendChild(tr);
      });
    }
  
    async function excluirCliente(idDoCliente) {
      try {
        await axios.delete(`http://localhost:8000/clientes/${idDoCliente}`);
        alert('Cliente apagado com sucesso.');
  
      } catch (error) {
        console.error('Erro ao apagar cliente:', error);
        alert('Erro ao apagar cliente');
      }
      renderizarClientes();
  
    }
  
    window.excluirCliente = excluirCliente;
  
    renderizarClientes();
  });
  