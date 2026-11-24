for (const card of document.querySelectorAll('.testimonial-card')) {
  const quote = card.querySelector('.testimonial-quote');
  const button = card.querySelector('.testimonial-toggle');

  const update = () => {
    if (button.getAttribute('aria-expanded') === 'true') return;

    quote.setAttribute('data-collapsed', '');
    button.hidden = quote.scrollHeight <= quote.clientHeight;
    if (button.hidden) quote.removeAttribute('data-collapsed');
  };

  button.addEventListener('click', () => {
    const expanded = button.getAttribute('aria-expanded') === 'true';
    button.setAttribute('aria-expanded', String(!expanded));
    button.textContent = expanded ? 'Read more' : 'Read less';

    if (expanded) update();
    else quote.removeAttribute('data-collapsed');
  });

  window.addEventListener('resize', update);
  document.fonts?.ready.then(update);
  update();
}
