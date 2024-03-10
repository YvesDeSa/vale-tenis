document.addEventListener('DOMContentLoaded', function() {
  // Inicializa produtos a partir do localStorage ou usa array padrão se não houver dados salvos
  let produtos = JSON.parse(localStorage.getItem('produtos')) || [];

  function salvarProdutos() {
    localStorage.setItem('produtos', JSON.stringify(produtos));
  }

  function formatarGenero(genero) {
    let partes = [];
    if (genero.adulto) partes.push(`Adulto - ${genero.adulto}`);
    if (genero.infantil) partes.push(`Infantil - ${genero.infantil}`);
    return partes.join(", ");
  }

  function renderizarProdutos() {
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

  function excluirProduto(idDoProduto) {
    const produtoIndex = produtos.findIndex(produto => produto.id === idDoProduto);
    if (produtoIndex !== -1) {
      produtos.splice(produtoIndex, 1);
      salvarProdutos();
      renderizarProdutos();
    }
  }

  window.excluirProduto = excluirProduto;

  renderizarProdutos();
});
