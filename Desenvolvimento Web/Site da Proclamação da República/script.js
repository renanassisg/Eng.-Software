// script.js - JS leve para acessibilidade e galeria modal


document.addEventListener('DOMContentLoaded', function(){
// Modal de galeria
const modal = document.getElementById('modal');
const modalImg = document.getElementById('modal-image');
const modalCaption = document.getElementById('modal-caption');
const closeBtn = document.getElementById('modal-close');


document.querySelectorAll('.gallery-item').forEach(btn => {
btn.addEventListener('click', () => {
const src = btn.getAttribute('data-src');
modalImg.src = src;
modalImg.alt = btn.querySelector('img').alt || 'Imagem da galeria';
modalCaption.textContent = btn.querySelector('img').alt || '';
modal.setAttribute('aria-hidden','fa