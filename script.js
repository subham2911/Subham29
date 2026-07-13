const yesButton = document.getElementById('yes-btn');
const songButton = document.getElementById('song-btn');
const proposalText = document.getElementById('proposal-text');
const card = document.querySelector('.card');
const ring = document.querySelector('.ring');
const songPlayer = document.getElementById('song-player');

yesButton.addEventListener('click', () => {
  proposalText.textContent = yesButton.dataset.message;
  proposalText.style.color = '#b0206a';
  card.classList.add('celebrate');
  ring.classList.add('active');
});

songButton.addEventListener('click', () => {
  songPlayer.classList.remove('hidden');
  songButton.textContent = 'Tere Hawale Playing';
});
