// ============================================================
// FUNÇÃO PARA PLAY/MUDO NO VÍDEO DE FUNDO
// ============================================================
// da seção video 'onclick="play(event)"'
function play(event) {
  // 1. Impede que o link '#' recarregue a página ou pule para o topo
  event.preventDefault();

  // 2. Seleciona o vídeo usando o ID
  const video = document.getElementById("play-video");

  // 3. Pega o elemento que foi clicado (o próprio link <a>)
  const botao = event.currentTarget;

  // 4. Lógica para ATIVAR ou DESATIVAR o som
  if (video.muted) {
    // Se ESTIVER mudo, tira o mudo
    video.muted = false;
    botao.textContent = "DESATIVAR SOM"; // Muda o texto do botão
  } else {
    // Se NÃO ESTIVER mudo, coloca o mudo
    video.muted = true;
    botao.textContent = "OUÇA AGORA"; // Volta o texto original
  }
}

// ============================================================
// SCRIPT PARA PASSAR O CARROSSEL AUTOMATICAMENTE
// ============================================================

let slideAtual = 0; // Começa no primeiro slide (índice 0)
const radios = document.querySelectorAll('input[name="carousel"]');
const totalSlides = radios.length;
const tempoDeTroca = 4000; // 4000ms = 4 segundos

// Função que será chamada repetidamente
function proximoSlideAutomatico() {
  // O operador '%' (módulo) faz com que, após o último slide (2),
  // ele volte para o primeiro (0).
  slideAtual = (slideAtual + 1) % totalSlides;

  // 2. Marca o input de rádio desse próximo slide como "checked"
  radios[slideAtual].checked = true;
}

// Diz ao navegador para rodar a função
// 'proximoSlideAutomatico' a cada 'tempoDeTroca' milissegundos.
setInterval(proximoSlideAutomatico, tempoDeTroca);

// ============================================================
// MENU MOBILE (HAMBURGER)
// ============================================================
function ToggleMenu(event) {
  // 1. Log para testar se o clique funcionou
  console.log("Clique detectado!");

  // 2. Seleciona o NAV principal (o pai de todos)
  const nav = document.getElementById("menu");

  if (nav) {
    nav.classList.toggle("active");
    console.log("Classe 'active' alternada!");
  } else {
    console.error("Erro: Não encontrei o elemento com ID 'menu'");
  }
}
