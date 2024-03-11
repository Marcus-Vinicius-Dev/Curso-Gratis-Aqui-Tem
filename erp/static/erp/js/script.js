let carregarImagens = false;
// script.js
document.addEventListener('DOMContentLoaded', function () {
  const imagens = [
      'artes.jpg',
      'chiron.jpg',
      'danca.jpg',
      'esportes.jpg',
      'idiomas.jpg',
      'musica.jpg',
      'negocios.jpg',
      'relogio.jpg',
      'relogio2.jpg',
      'technology2.jpg',
      'technology2_dagua.jpg',
      'tecnologia.jpg'
  ];

  const container = document.getElementById('imagens-rolagem-infinita');

  imagens.forEach((imagem, index) => {
      const novaImagem = document.createElement('img');
      novaImagem.classList.add('imagem-post');
      novaImagem.src = `/static/erp/img/${imagem}`;
      novaImagem.alt = `Imagem ${index}`;
      container.appendChild(novaImagem);
  });
});
