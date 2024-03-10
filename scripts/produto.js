document.addEventListener('DOMContentLoaded', function() {
  function marcarBotaoAtivo(seletorGrupo, classeAtiva, valor) {
    document.querySelectorAll(seletorGrupo).forEach(btn => {
      if (btn.getAttribute('data-tipo') === valor || btn.getAttribute('data-genero') === valor) {
        btn.classList.add(classeAtiva);
      } else {
        btn.classList.remove(classeAtiva);
      }
    });
  }
  // Evento de clique para botões de tipo
  document.querySelectorAll('.tipo-btn').forEach(btn => {
    btn.addEventListener('click', function() {
      document.querySelectorAll('.tipo-btn').forEach(btn => btn.classList.remove('active'));
      this.classList.add('active');
      document.getElementById('tipoGenero').value = this.getAttribute('data-tipo');
    });
  });

  document.querySelectorAll('.genero-btn').forEach(btn => {
    btn.addEventListener('click', function() {
      document.querySelectorAll('.genero-btn').forEach(btn => btn.classList.remove('active'));
      this.classList.add('active');
      document.getElementById('genero').value = this.getAttribute('data-genero');
    });
  });
  let produtos = JSON.parse(localStorage.getItem('produtos')) || [];

  const urlParams = new URLSearchParams(window.location.search);
  const productId = urlParams.get('id');
  const form = document.getElementById('productForm');
  const pageTitle = document.getElementById('pageTitle');

  if (productId) {
    const produto = produtos.find(p => p.id == productId);
    if (produto) {
      document.getElementById('productId').value = produto.id;
      document.getElementById('modelo').value = produto.modelo;
      document.getElementById('marca').value = produto.marca;
      document.getElementById('detalhe').value = produto.detalhe;
      document.getElementById('tamanho').value = produto.tamanhos.join(', ');
      const tipo = produto.genero.adulto ? 'adulto' : 'infantil';
      marcarBotaoAtivo('.tipo-btn', 'active', tipo);
      const generoValor = produto.genero.adulto || produto.genero.infantil;
      marcarBotaoAtivo('.genero-btn', 'active', generoValor);

      document.getElementById('tipoGenero').value = tipo;
      document.getElementById('genero').value = generoValor;

      pageTitle.innerText = 'Editar Produto';
      form.setAttribute('data-id', produto.id);
    }
  }

  form.addEventListener('submit', function(e) {
    e.preventDefault();

    const id = document.getElementById('productId').value;
    const modelo = document.getElementById('modelo').value;
    const marca = document.getElementById('marca').value;
    const detalhe = document.getElementById('detalhe').value;
    const tamanhos = document.getElementById('tamanho').value.split(',').map(t => t.trim());
    const tipoGenero = document.getElementById('tipoGenero').value;
    const genero = document.getElementById('genero').value;

    const produtoData = {
      id: id,
      modelo: modelo,
      marca: marca,
      detalhe: detalhe,
      tamanhos: tamanhos,
      genero: {
        adulto: tipoGenero === 'adulto' ? genero : null,
        infantil: tipoGenero === 'infantil' ? genero : null
      }
    };

    if (id) {
      const index = produtos.findIndex(p => p.id == id);
      produtos[index] = { ...produtoData, id: Number(id) };
    } else {
      const novoId = produtos.length > 0 ? Math.max(...produtos.map(p => p.id)) + 1 : 1;
      produtos.push({ ...produtoData, id: novoId });
    }

    localStorage.setItem('produtos', JSON.stringify(produtos));
    alert('Produto salvo com sucesso!');
    window.location.href = 'index.html'; // Ou a URL da sua lista de produtos
  });
});
