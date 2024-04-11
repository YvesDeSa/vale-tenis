document.querySelectorAll('.tipo-btn').forEach(btn => {
  btn.addEventListener('click', function() {
    const tipo = this.getAttribute('data-tipo');
    // Esconde todos os botões de tamanho
    document.querySelectorAll('.tamanho-btn').forEach(btn => {
      btn.classList.add('d-none');
      btn.classList.remove('btn-secondary');
      btn.classList.add('btn-outline-secondary');
    });

    // Mostra botões de tamanho baseados na seleção de tipo
    document.querySelectorAll(`.tamanho-${tipo}`).forEach(btn => {
      btn.classList.remove('d-none');
    });

    // Reseta a seleção de tamanhos
    document.getElementById('tamanhosSelecionados').value = '';
  });
});

document.querySelectorAll('.tamanho-btn').forEach(btn => {
  btn.addEventListener('click', function() {
    // Alterna a classe 'btn-secondary' para permitir múltiplas seleções
    this.classList.toggle('btn-secondary');
    this.classList.toggle('btn-outline-secondary');

    // Atualiza o campo oculto com os tamanhos selecionados
    const tamanhosSelecionados = Array.from(document.querySelectorAll('.tamanho-btn.btn-secondary'))
      .map(btn => btn.getAttribute('data-tamanho'));
    document.getElementById('tamanhosSelecionados').value = tamanhosSelecionados.join(',');
  });
});


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
  // let produtos = JSON.parse(localStorage.getItem('produtos')) || [];

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
      document.getElementById('tamanhosSelecionados').value = produto.tamanhos.join(', ');
      const tipo = produto.genero.adulto ? 'adulto' : 'infantil';
      marcarBotaoAtivo('.tipo-btn', 'active', tipo);
      const generoValor = produto.genero.adulto || produto.genero.infantil;
      marcarBotaoAtivo('.genero-btn', 'active', generoValor);

      if (tipo === 'adulto') {
        document.querySelectorAll('.tamanho-adulto').forEach(btn => btn.classList.remove('d-none'));
      } else if (tipo === 'infantil') {
        document.querySelectorAll('.tamanho-infantil').forEach(btn => btn.classList.remove('d-none'));
      }

      document.getElementById('tipoGenero').value = tipo;
      document.getElementById('genero').value = generoValor;

      produto.tamanhos.forEach(tamanho => {
        const btn = document.querySelector(`.tamanho-btn[data-tamanho="${tamanho}"]`);
        if (btn) {
          btn.classList.add('btn-secondary');
          btn.classList.remove('btn-outline-secondary');
        }
      });

      pageTitle.innerText = 'Editar Produto';
      form.setAttribute('data-id', produto.id);
    }
  }
 
  form.addEventListener('submit', async function(e) {
    e.preventDefault();

    const id = document.getElementById('productId').value;
    const modelo = document.getElementById('modelo').value;
    const marca = document.getElementById('marca').value;
    const detalhe = document.getElementById('detalhe').value;
    const tamanhosSelecionados = document.getElementById('tamanhosSelecionados').value.split(',');
    const tipoGenero = document.getElementById('tipoGenero').value;
    const genero = document.getElementById('genero').value;

    const produtoData = {
      id: 0,
      detalhe: detalhe,
      genero: {
        adulto: tipoGenero === 'adulto' ? genero : null,
        infantil: tipoGenero === 'infantil' ? genero : null
      },
      marca: marca,
      modelo: modelo,
      tamanhos: tamanhosSelecionados
    };

    await axios.post('http://127.0.0.1:8000/produtos', produtoData);
    alert('Produto cadastrado com sucesso.');
    window.location.href = 'produto.html';
  });
});
