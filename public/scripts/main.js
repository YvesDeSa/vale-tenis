document.addEventListener('DOMContentLoaded', async function() {

  function formatarGenero(genero) {
    let partes = [];
    if (genero.adulto) partes.push(`Adulto - ${genero.adulto}`);
    if (genero.infantil) partes.push(`Infantil - ${genero.infantil}`);
    return partes.join(", ");
  }

  async function renderizarProdutos() {

    const response = await axios.get('http://localhost:8000/produtos');
    const produtos = response.data; //Armazenando na variável animais
    
    const listaProdutosEl = document.getElementById('listaProdutos');
    listaProdutosEl.innerHTML = '';

    produtos.forEach(produto => {
      const tr = document.createElement('tr');
      tr.classList.add('produto');
      tr.innerHTML = `
              <td>${produto.modelo}</td>
              <td>${produto.marca}</td>
              <td>${produto.tamanhos.join(', ')}</td>
              <td>${produto.detalhe}</td>
              <td>${formatarGenero(produto.genero)}</td>
              <td>
                    <a href="produto.html?id=${produto.id}" class="btn btn-outline-primary btn-sm me-2">
                        <i class="bi bi-pencil"></i>
                    </a>
                    <button onclick="excluirProduto(${produto.id})" class="btn btn-outline-danger btn-sm">
                        <i class="bi bi-trash"></i>
                    </button>
              </td>
            `;
      listaProdutosEl.appendChild(tr);
    });
  }

  async function excluirProduto(idDoProduto) {
    try {
      await axios.delete(`http://localhost:8000/produtos/${idDoProduto}`);
      alert('Produto apagado com sucesso.');

    } catch (error) {
      console.error('Erro ao apagar produto:', error);
      alert('Erro ao apagar produto');
    }
    renderizarProdutos();

  }

  window.excluirProduto = excluirProduto;

  renderizarProdutos();
});
