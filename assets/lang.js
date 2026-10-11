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
var featSec=document.getElementById('features'),devbox=document.querySelector('.devbox'),curStep=0;
function act(k){if(k===curStep&&steps[k]&&steps[k].classList.contains('on'))return;curStep=k;
 steps.forEach(function(s,i){s.classList.toggle('on',i===k)});
 frames.forEach(function(f,i){f.classList.toggle('on',i===k)});
 dots.forEach(function(d,i){d.classList.toggle('on',i===k);d.classList.toggle('past',i<k)})}
if(steps.length){if(io){var so=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)act(+e.target.dataset.step)})},{rootMargin:'-45% 0px -45% 0px'});steps.forEach(function(s){so.observe(s)})}else act(0)}

// features v2: scroll-linked progress (desktop)
var stepsBox=document.querySelector('.steps');
function featLink(){
 if(!featSec||!steps.length)return;
 if(reduce||window.innerWidth<=820){featSec.classList.remove('live');frames.forEach(function(f){f.style.opacity='';f.style.transform='';f.style.filter=''});return}
 featSec.classList.add('live');
 var vh=window.innerHeight,best=0,bc=9,n=steps.length;
 steps.forEach(function(s,i){var r=s.getBoundingClientRect(),c=(r.top+r.height/2-vh/2)/r.height;c=Math.max(-1,Math.min(1,c));
  var a=1-Math.max(0,Math.min(1,(Math.abs(c)-.22)/.5));s.style.setProperty('--a',a.toFixed(3));s.style.setProperty('--c',c.toFixed(3));if(Math.abs(c)<Math.abs(bc)){bc=c;best=i}});
 var t=-bc,u=Math.max(0,Math.min(1,(Math.abs(t)-.2)/.3)),e=u*u*(3-2*u)*.5*(t<0?-1:1);var f=Math.max(0,Math.min(n-1,best+e));
 frames.forEach(function(fr,i){var k=i-f,ak=Math.abs(k),o=Math.max(0,1-ak*1.2);fr.style.opacity=o.toFixed(3);
  fr.style.transform=o>0?'translate3d(0,'+(k*46).toFixed(1)+'px,0) scale('+(1-Math.min(ak,1)*.06).toFixed(3)+')':'';
  fr.style.filter=(o>0&&o<.98)?'blur('+(ak*4).toFixed(1)+'px)':'none'});
 if(stepsBox)stepsBox.style.setProperty('--fp',(f/(n-1)).toFixed(4));
 act(best)}
var fTick=false;window.addEventListener('scroll',function(){if(!fTick){fTick=true;requestAnimationFrame(function(){featLink();fTick=false})}},{passive:true});
window.addEventListener('resize',featLink);featLink();
// FAQ slide
document.querySelectorAll('.faq details').forEach(function(d){var s=d.querySelector('summary');s.addEventListener('click',function(ev){if(reduce)return;ev.preventDefault();
 if(d.open){d.classList.add('closing');setTimeout(function(){d.open=false;d.classList.remove('closing')},300)}else{d.classList.add('opening');d.open=true;requestAnimationFrame(function(){requestAnimationFrame(function(){d.classList.remove('opening')})})}})});
// nav hairline + parallax
var px=document.querySelectorAll('[data-px]'),ticking=false;
function onScroll(){var y=window.scrollY;if(top)top.classList.toggle('scrolled',y>8);
 if(!reduce&&window.innerWidth>820){px.forEach(function(e){var f=+e.dataset.px,r=e.classList.contains('p1')?Math.min(4,y/120):0;e.style.transform='translateY('+(y*f).toFixed(1)+'px)'+(e.classList.contains('p1')?' rotate('+(-7+r).toFixed(2)+'deg)':'')});
  if(featSec&&devbox){var fr=featSec.getBoundingClientRect(),vh=window.innerHeight,span=fr.height-vh;if(span>0){var p=Math.min(1,Math.max(0,-fr.top/span));devbox.style.transform='translateY('+((p-.5)*28).toFixed(1)+'px)'}else devbox.style.transform=''}}
 else if(devbox)devbox.style.transform='';
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
