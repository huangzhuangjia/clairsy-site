// Language toggle memory + menu + Apple-style motion (no libraries). Respects prefers-reduced-motion.
(function(){
document.querySelectorAll('.lang a').forEach(function(a){a.addEventListener('click',function(){try{localStorage.setItem('clairsy-lang',a.dataset.lang)}catch(e){}})});
var b=document.querySelector('.burger'),m=document.getElementById('menu');
if(b&&m){b.addEventListener('click',function(){var o=m.classList.toggle('open');b.setAttribute('aria-expanded',o)});m.addEventListener('click',function(e){if(e.target.tagName==='A'){m.classList.remove('open');b.setAttribute('aria-expanded','false')}})}
var top=document.querySelector('.top');
var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
var io='IntersectionObserver' in window;
// scroll reveal
var rv=document.querySelectorAll('.reveal');
if(!io||reduce){rv.forEach(function(e){e.classList.add('in')})}else{
 var ro=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){var el=e.target,sib=el.parentElement?Array.prototype.indexOf.call(el.parentElement.children,el):0;el.style.transitionDelay=Math.min(sib,4)*90+'ms';el.classList.add('in');ro.unobserve(el)}})},{threshold:.15,rootMargin:'0px 0px -8% 0px'});
 rv.forEach(function(e){ro.observe(e)})}
// sticky feature steps
var steps=document.querySelectorAll('.step'),frames=document.querySelectorAll('.frame'),dots=document.querySelectorAll('.dots i');
function act(k){steps.forEach(function(s,i){s.classList.toggle('on',i==k)});frames.forEach(function(f,i){f.classList.toggle('on',i==k)});dots.forEach(function(d,i){d.classList.toggle('on',i==k)})}
if(steps.length){if(io){var so=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)act(+e.target.dataset.step)})},{rootMargin:'-45% 0px -45% 0px'});steps.forEach(function(s){so.observe(s)})}else act(0)}
// FAQ slide
document.querySelectorAll('.faq details').forEach(function(d){var s=d.querySelector('summary');s.addEventListener('click',function(ev){if(reduce)return;ev.preventDefault();
 if(d.open){d.classList.add('closing');setTimeout(function(){d.open=false;d.classList.remove('closing')},300)}else{d.classList.add('opening');d.open=true;requestAnimationFrame(function(){requestAnimationFrame(function(){d.classList.remove('opening')})})}})});
// nav hairline + parallax
var px=document.querySelectorAll('[data-px]'),ticking=false;
function onScroll(){var y=window.scrollY;if(top)top.classList.toggle('scrolled',y>8);
 if(!reduce&&window.innerWidth>820){px.forEach(function(e){var f=+e.dataset.px,r=e.classList.contains('p1')?Math.min(4,y/120):0;e.style.transform='translateY('+(y*f).toFixed(1)+'px)'+(e.classList.contains('p1')?' rotate('+(-7+r).toFixed(2)+'deg)':'')})}
 ticking=false}
window.addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(onScroll)}},{passive:true});onScroll();

// Meet Qingqing — expression cycle (pause on hover/focus; static if reduced motion)
var meet=document.querySelector('.meetcard');
if(meet){
 var faces=meet.querySelectorAll('.meet-face'), moodBtns=meet.querySelectorAll('.mood'), mi=0, timer=null, paused=false;
 function showMood(i){mi=i;faces.forEach(function(f,k){f.classList.toggle('on',k===i)});moodBtns.forEach(function(b,k){var on=k===i;b.classList.toggle('on',on);b.setAttribute('aria-pressed',on?'true':'false')})}
 function next(){if(!paused)showMood((mi+1)%faces.length)}
 function start(){if(reduce||timer||faces.length<2)return;timer=setInterval(next,2800)}
 function stop(){if(timer){clearInterval(timer);timer=null}}
 moodBtns.forEach(function(b,i){b.addEventListener('click',function(){showMood(i);paused=true;stop()});b.addEventListener('mouseenter',function(){showMood(i);paused=true;stop()});b.addEventListener('focus',function(){showMood(i);paused=true;stop()})});
 meet.addEventListener('mouseleave',function(){paused=false;start()});
 if(!reduce){if(io){var mo=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)start();else stop()})},{threshold:.25});mo.observe(meet)}else start()}
}

})();
