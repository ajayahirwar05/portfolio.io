document.addEventListener('DOMContentLoaded', () => {
  const menuButton = document.querySelector('.menu-toggle');
  const menu = document.querySelector('.nav-menu');
  const themeButton = document.querySelector('.theme-toggle');
  const filters = document.querySelectorAll('.filter');
  const cards = document.querySelectorAll('.project-card');
  const noResults = document.querySelector('.no-results');
  const form = document.querySelector('#contact-form');
  const themeColors = { ink: '#eff5f0', muted: '#aab9b0', paper: '#13201b', surface: '#1a2b24', line: '#36473e', green: '#2a8465' };

  document.querySelector('#year').textContent = new Date().getFullYear();
  menuButton.addEventListener('click', () => { const open = menu.classList.toggle('open'); menuButton.setAttribute('aria-expanded', open); });
  menu.querySelectorAll('a').forEach(link => link.addEventListener('click', () => { menu.classList.remove('open'); menuButton.setAttribute('aria-expanded', 'false'); }));
  themeButton.addEventListener('click', () => { const dark = document.body.classList.toggle('dark'); Object.entries(themeColors).forEach(([name, value]) => document.body.style.setProperty(`--${name}`, dark ? value : '')); themeButton.querySelector('span').textContent = dark ? '☾' : '☼'; });
  filters.forEach(button => button.addEventListener('click', () => { const filter = button.dataset.filter; filters.forEach(item => item.classList.toggle('active', item === button)); let visible = 0; cards.forEach(card => { const show = filter === 'all' || card.dataset.category.includes(filter); card.hidden = !show; if (show) visible += 1; }); noResults.hidden = visible !== 0; }));
  form.addEventListener('submit', event => { event.preventDefault(); const fields = ['name', 'email', 'message']; let valid = true; fields.forEach(id => { const input = document.querySelector('#' + id); const error = document.querySelector('#' + id + '-error'); let message = ''; if (!input.value.trim()) message = `Please enter ${id === 'message' ? 'a message' : 'your ' + id}.`; else if (id === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.value.trim())) message = 'Please enter a valid email address.'; error.textContent = message; input.setAttribute('aria-invalid', Boolean(message)); if (message) valid = false; }); if (valid) { const name = document.querySelector('#name').value.trim(); document.querySelector('#form-status').textContent = `Thanks, ${name}! Your message is ready to send.`; form.reset(); } });
});
