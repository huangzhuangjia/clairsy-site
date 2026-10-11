// EN | 中文 toggle: remember explicit choice. Language URLs (/en/, /zh/) are stable and never auto-redirect.
document.querySelectorAll('.lang a').forEach(function(a){a.addEventListener('click',function(){try{localStorage.setItem('clairsy-lang',a.dataset.lang)}catch(e){}})});
