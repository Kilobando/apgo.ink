(function(){
  const stored = localStorage.getItem('theme');
  if(stored === 'light') document.body.classList.add('light');
  document.addEventListener('DOMContentLoaded', () => {
    const btn = document.querySelector('.theme-toggle');
    if(btn){
      btn.addEventListener('click', () => {
        document.body.classList.toggle('light');
        const mode = document.body.classList.contains('light') ? 'light' : 'dark';
        localStorage.setItem('theme', mode);
      });
    }
  });
})();
