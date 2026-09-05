import json, os, random

with open(r"C:\Users\subhahalder\Pages\gunu_photos.json") as f:
    photos = json.load(f)

notes_map = {
    "20241228_165150.jpg":     "The last days of that year — you made them golden.",
    "20250810_173514.jpg":     "Summer afternoons never felt this good.",
    "20251102_163917.jpg":     "You make even November feel warm.",
    "20251102_164341.jpg":     "Same day. Still my favourite frame.",
    "20251207_190703.jpg":     "December magic — found right here.",
    "20251207_190739.jpg":     "Two minutes later. Still breathtaking.",
    "20260102_164718.jpg":     "The new year started perfectly.",
    "20260103_081145.jpg":     "8am and you already made the whole day.",
    "20260104_093029.jpg":     "Three days in, already a favourite memory.",
    "20260104_093123.jpg":     "I could look at this forever.",
    "20260104_132828.jpg":     "Same afternoon. Different kind of beautiful.",
    "20260105_101129.jpg":     "Last morning of the trip — kept close ever since.",
    "20260105_191509.jpg":     "One last evening together. Never enough.",
    "20260402_193812.jpg":     "April, and my whole world in one frame.",
    "20260621_183521.jpg":     "The longest day of the year — spent perfectly.",
    "20260621_184211.jpg":     "Golden hour was just showing off for you.",
    "20260727_114054.jpg":     "Midsummer. Every second counts.",
    "20260728_101121.jpg":     "Another morning, another reason to smile.",
    "20260801_162910.jpg":     "August arrived, and so did this moment.",
    "20260831_114026.jpg":     "Last day of August — saved it forever.",
    "IMG-20251002-WA0020.jpg": "You sent this to me. I never deleted it.",
    "IMG_1152.jpg":            "My favourite on the whole camera roll.",
}

pairs = [{"src": p["b64"], "note": notes_map.get(p["name"], "Every moment with you.")} for p in photos]
random.shuffle(pairs)

photos_js = "[\n" + ",\n".join(
    f'  {{"src":"data:image/jpeg;base64,{p["src"]}","note":{json.dumps(p["note"])}}}'
    for p in pairs
) + "\n]"

TEMPLATE = r"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<meta name="theme-color" content="#09050F"/>
<title>Happy Birthday Gunu ♡</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500&display=swap" rel="stylesheet"/>
<style>
/* ════ DARK THEME (default) ════ */
:root {
  --bg:       #07040D;
  --text:     #F6E8D8;
  --dim:      rgba(246,232,216,.52);
  --rose:     #C25070;
  --rose-lt:  #F0B8CA;
  --gold:     #C9955A;
  --gold-lt:  #EDD080;
  --blush:    #F5C8D4;
  --glass:    rgba(255,255,255,.035);
  --glass-b:  rgba(255,255,255,.07);
  --pol-bg1:  #FAF0E2;
  --pol-bg2:  #F5E8D4;
  --pol-text: #3A2214;
  --lb-bg:    rgba(4,2,8,.97);
  --toggle-bg:rgba(255,255,255,.1);
  --toggle-b: rgba(255,255,255,.2);
  --toggle-c: #EDD080;
  --foot-bg:  #040208;
  --foot-t:   rgba(246,232,216,.25);
  --scroll-c: #EDD080;
}

/* ════ LIGHT THEME ════ */
[data-theme="light"] {
  --bg:       #FAF0E6;
  --text:     #2A1810;
  --dim:      rgba(42,24,16,.6);
  --rose:     #B84060;
  --rose-lt:  #A03050;
  --gold:     #8A5C18;
  --gold-lt:  #9A6C28;
  --blush:    #7A2840;
  --glass:    rgba(255,255,255,.65);
  --glass-b:  rgba(42,24,16,.1);
  --pol-bg1:  #FFFAF5;
  --pol-bg2:  #FFF5EE;
  --pol-text: #3A2214;
  --lb-bg:    rgba(250,240,230,.97);
  --toggle-bg:rgba(42,24,16,.08);
  --toggle-b: rgba(42,24,16,.18);
  --toggle-c: #8A5C18;
  --foot-bg:  #EDE0D4;
  --foot-t:   rgba(42,24,16,.4);
  --scroll-c: #9A6C28;
}

/* ════ RESET ════ */
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html{scroll-behavior:smooth}
body{
  background:var(--bg);color:var(--text);
  font-family:'Cormorant Garamond',Georgia,serif;
  overflow-x:hidden;
  transition:background .5s ease, color .4s ease;
}

/* ════ THEME TOGGLE ════ */
.theme-toggle{
  position:fixed;top:18px;right:18px;z-index:900;
  width:46px;height:46px;border-radius:50%;
  background:var(--toggle-bg);
  border:1px solid var(--toggle-b);
  color:var(--toggle-c);
  font-size:20px;cursor:pointer;
  display:flex;align-items:center;justify-content:center;
  backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);
  transition:background .3s,border-color .3s,transform .25s;
  touch-action:manipulation;
}
.theme-toggle:hover,.theme-toggle:active{transform:scale(1.1)}

/* ════ AURORA ════ */
.aurora{position:fixed;border-radius:50%;pointer-events:none;z-index:0;will-change:transform;transition:opacity .5s}
.aurora-1{
  width:min(70vw,600px);height:min(70vw,600px);
  top:-15%;right:-10%;
  animation:drift1 28s ease-in-out infinite;
}
.aurora-2{
  width:min(60vw,500px);height:min(60vw,500px);
  bottom:15%;left:-12%;
  animation:drift2 34s ease-in-out infinite;
}
.aurora-3{
  width:min(50vw,420px);height:min(50vw,420px);
  top:42%;right:8%;
  animation:drift3 22s ease-in-out infinite;
}
/* dark aurora colours */
[data-theme="dark"] .aurora-1{background:radial-gradient(circle,rgba(190,70,105,.18) 0%,transparent 70%)}
[data-theme="dark"] .aurora-2{background:radial-gradient(circle,rgba(180,120,50,.14) 0%,transparent 70%)}
[data-theme="dark"] .aurora-3{background:radial-gradient(circle,rgba(90,40,160,.12) 0%,transparent 70%)}
/* light aurora colours — very soft */
[data-theme="light"] .aurora-1{background:radial-gradient(circle,rgba(190,80,110,.1) 0%,transparent 70%)}
[data-theme="light"] .aurora-2{background:radial-gradient(circle,rgba(200,140,60,.08) 0%,transparent 70%)}
[data-theme="light"] .aurora-3{background:radial-gradient(circle,rgba(140,90,180,.07) 0%,transparent 70%)}
@keyframes drift1{0%,100%{transform:translate(0,0) scale(1)}33%{transform:translate(-4%,9%) scale(1.08)}66%{transform:translate(5%,-4%) scale(.94)}}
@keyframes drift2{0%,100%{transform:translate(0,0) scale(1)}40%{transform:translate(7%,-6%) scale(1.06)}75%{transform:translate(-4%,7%) scale(.92)}}
@keyframes drift3{0%,100%{transform:translate(0,0) scale(1)}50%{transform:translate(-7%,4%) scale(1.1)}}

/* ════ HERO ════ */
.hero{
  position:relative;width:100%;height:100svh;min-height:600px;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  overflow:hidden;z-index:1;
}
[data-theme="dark"]  .hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 85% 70% at 50% 44%,#280D38 0%,#130828 50%,transparent 100%)}
[data-theme="light"] .hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 90% 80% at 50% 44%,rgba(255,230,195,.9) 0%,rgba(250,240,230,.6) 55%,transparent 100%)}
#petals-canvas,#confetti-canvas,#stars-canvas{
  position:fixed;inset:0;width:100%;height:100%;pointer-events:none;
}
#stars-canvas{z-index:0}
#petals-canvas{z-index:1}
#confetti-canvas{z-index:10}
.hero-content{position:relative;z-index:2;text-align:center;padding:0 24px;animation:fadeUp 2s cubic-bezier(.22,1,.36,1) both;animation-delay:.3s}
.eyebrow{font-size:clamp(9px,3vw,13px);letter-spacing:.45em;text-transform:uppercase;font-weight:300;color:var(--gold-lt);margin-bottom:20px;opacity:.8}

/* hero name — dark shimmer */
[data-theme="dark"] .hero-name{
  background:linear-gradient(115deg,var(--text) 30%,#EDD080 48%,#F0B8CA 54%,var(--text) 70%);
  background-size:250% 100%;
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;
  filter:drop-shadow(0 0 40px rgba(190,70,105,.35));
}
/* hero name — light shimmer (dark tones) */
[data-theme="light"] .hero-name{
  background:linear-gradient(115deg,#2A1810 28%,#8A5C18 46%,#B84060 54%,#2A1810 72%);
  background-size:250% 100%;
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;
  filter:drop-shadow(0 0 24px rgba(184,64,96,.2));
}
.hero-name{
  font-size:clamp(80px,24vw,210px);font-weight:300;line-height:.85;
  letter-spacing:-.02em;cursor:pointer;user-select:none;
  animation:shimmer 5s linear infinite;
}
@keyframes shimmer{0%{background-position:200% center}100%{background-position:-200% center}}
.hero-ornament{display:flex;align-items:center;gap:16px;justify-content:center;margin:20px 0}
.hero-ornament::before,.hero-ornament::after{content:'';flex:1;max-width:80px;height:1px;background:linear-gradient(90deg,transparent,rgba(201,149,90,.5))}
.hero-ornament::after{background:linear-gradient(90deg,rgba(201,149,90,.5),transparent)}
.hero-ornament span{font-size:16px;color:var(--rose);opacity:.7;animation:heartbeat 2.4s ease-in-out infinite}
.hero-date{font-size:clamp(12px,3.2vw,18px);font-weight:300;letter-spacing:.22em;color:var(--gold-lt);font-style:italic;opacity:.8}
.tap-hint{font-size:clamp(8px,2.4vw,11px);letter-spacing:.22em;text-transform:uppercase;font-weight:300;color:rgba(180,150,80,.45);margin-top:16px;transition:color .3s,opacity .5s}
[data-theme="light"] .tap-hint{color:rgba(138,92,24,.4)}
.scroll-cue{position:absolute;bottom:30px;left:50%;transform:translateX(-50%);z-index:3;display:flex;flex-direction:column;align-items:center;gap:8px;opacity:.4;animation:bounce 2.8s ease-in-out infinite}
.scroll-cue span{font-size:8px;letter-spacing:.3em;text-transform:uppercase;font-weight:300;color:var(--scroll-c)}

/* ════ SECTION LABEL ════ */
.sec-label{text-align:center;padding:72px 20px 40px;position:relative;z-index:1}
.sec-label h2{
  font-size:clamp(26px,7vw,56px);font-weight:300;
  background:linear-gradient(135deg,var(--text),var(--gold));
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;
}
.sec-label p{margin-top:10px;font-size:clamp(13px,3.5vw,16px);color:var(--dim);font-style:italic;font-weight:300}
.rose-line{width:60px;height:1px;background:linear-gradient(90deg,transparent,var(--rose),transparent);margin:14px auto 0}

/* ════ PLAY BUTTON ════ */
.play-row{display:flex;justify-content:center;padding:0 20px 32px;position:relative;z-index:1}
.play-btn{
  display:flex;align-items:center;gap:12px;
  background:rgba(194,80,112,.1);border:1px solid rgba(194,80,112,.3);
  color:var(--rose);
  font-family:'Cormorant Garamond',Georgia,serif;
  font-size:clamp(13px,3.5vw,16px);font-style:italic;letter-spacing:.12em;
  padding:14px 28px;border-radius:40px;cursor:pointer;
  transition:background .3s,border-color .3s,transform .2s;touch-action:manipulation;
}
[data-theme="light"] .play-btn{background:rgba(184,64,96,.08);border-color:rgba(184,64,96,.25)}
.play-btn:hover,.play-btn:active{background:rgba(194,80,112,.2);transform:scale(1.03)}

/* ════ POLAROID BOARD ════ */
.pol-board{display:grid;grid-template-columns:repeat(2,1fr);gap:clamp(10px,3vw,18px);padding:clamp(10px,3vw,18px);max-width:1320px;margin:0 auto;position:relative;z-index:1}
@media(min-width:520px){.pol-board{grid-template-columns:repeat(3,1fr)}}
@media(min-width:820px){.pol-board{grid-template-columns:repeat(4,1fr)}}
.pol-wrap{display:flex;align-items:center;justify-content:center}
.polaroid{
  background:linear-gradient(160deg,var(--pol-bg1),var(--pol-bg2));
  padding:clamp(6px,1.8vw,10px) clamp(6px,1.8vw,10px) 0;
  box-shadow:0 8px 28px rgba(0,0,0,.45),0 2px 6px rgba(0,0,0,.25),inset 0 0 0 1px rgba(0,0,0,.08);
  cursor:pointer;width:100%;
  transform:rotate(var(--rot,0deg));
  transition:transform .38s cubic-bezier(.34,1.56,.64,1),box-shadow .38s ease;
  animation:tossIn .7s cubic-bezier(.34,1.4,.64,1) both;
  animation-delay:var(--delay,0ms);will-change:transform;
}
[data-theme="light"] .polaroid{box-shadow:0 6px 24px rgba(60,30,10,.18),0 2px 8px rgba(60,30,10,.12),inset 0 0 0 1px rgba(0,0,0,.06)}
.polaroid:hover,.polaroid:active{
  transform:rotate(0deg) scale(1.07) translateY(-8px);
  box-shadow:0 24px 64px rgba(0,0,0,.55),0 0 36px rgba(194,80,112,.22),0 6px 12px rgba(0,0,0,.3);
}
[data-theme="light"] .polaroid:hover{box-shadow:0 20px 48px rgba(60,30,10,.2),0 0 32px rgba(184,64,96,.18)}
.polaroid img{width:100%;aspect-ratio:1/1;object-fit:cover;display:block}
.pol-caption{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;font-weight:300;font-size:clamp(9px,2.4vw,12px);color:var(--pol-text);line-height:1.4;text-align:center;padding:clamp(6px,1.8vw,9px) 6px clamp(8px,2.2vw,12px);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}

/* ════ CINEMATIC LIGHTBOX ════ */
.lightbox{position:fixed;inset:0;z-index:1000;background:var(--lb-bg);display:flex;flex-direction:column;align-items:center;justify-content:center;opacity:0;pointer-events:none;transition:opacity .4s ease,background .4s}
.lightbox.open{opacity:1;pointer-events:all}
.lb-frame{position:relative;width:min(88vw,88vh);height:min(88vw,88vh);overflow:hidden;border-radius:3px;box-shadow:0 0 0 1px rgba(0,0,0,.1),0 40px 100px rgba(0,0,0,.5)}
[data-theme="dark"] .lb-frame{box-shadow:0 0 0 1px rgba(255,255,255,.05),0 40px 100px rgba(0,0,0,.9)}
.lb-frame img{position:absolute;inset:-8%;width:116%;height:116%;object-fit:cover;animation:var(--kb-anim,kb0) 9s ease-in-out infinite alternate}
.lb-caption{max-width:min(88vw,88vh);padding:14px 20px 0;text-align:center;font-size:clamp(13px,3.8vw,17px);font-style:italic;font-weight:300;color:var(--dim);line-height:1.6;letter-spacing:.03em;animation:fadeUp .7s ease both;animation-delay:.35s}
.lb-story-progress{position:absolute;top:0;left:0;right:0;height:2px;background:rgba(128,64,64,.15)}
.lb-story-progress-bar{height:100%;background:linear-gradient(90deg,var(--rose),var(--gold));width:0%;transition:width linear}
.lb-close{position:absolute;top:14px;right:16px;background:none;border:none;cursor:pointer;color:var(--dim);font-size:24px;min-width:44px;min-height:44px;display:flex;align-items:center;justify-content:center;transition:color .2s;font-family:sans-serif}
.lb-close:hover{color:var(--text)}
.lb-arrow{position:absolute;top:50%;transform:translateY(-50%);background:rgba(194,80,112,.08);border:1px solid rgba(194,80,112,.2);color:var(--rose);font-size:28px;width:52px;height:52px;border-radius:50%;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:background .2s;min-width:52px;min-height:52px;font-family:sans-serif}
.lb-arrow:hover,.lb-arrow:active{background:rgba(194,80,112,.22)}
.lb-prev{left:10px}.lb-next{right:10px}
.lb-counter{position:absolute;top:14px;left:50%;transform:translateX(-50%);color:var(--dim);font-size:11px;letter-spacing:.2em;font-family:sans-serif}

/* Ken Burns */
@keyframes kb0{from{transform:scale(1)   translate(0,0)}    to{transform:scale(1.12) translate(-3%,-2%)}}
@keyframes kb1{from{transform:scale(1.12) translate(-3%,2%)} to{transform:scale(1)    translate(2%,-2%)}}
@keyframes kb2{from{transform:scale(1)   translate(2%,2%)}  to{transform:scale(1.12) translate(-2%,-3%)}}
@keyframes kb3{from{transform:scale(1.1) translate(2%,-2%)} to{transform:scale(1)    translate(-3%,2%)}}
@keyframes kb4{from{transform:scale(1)   translate(-2%,0)}  to{transform:scale(1.1)  translate(2%,2%)}}
@keyframes kb5{from{transform:scale(1.1) translate(0,2%)}   to{transform:scale(1)    translate(0,-2%)}}

/* ════ TIMELINE ════ */
.timeline-section{padding:72px 24px 80px;max-width:700px;margin:0 auto;position:relative;z-index:1}
.timeline-section>h2{font-size:clamp(26px,7vw,52px);font-weight:300;text-align:center;background:linear-gradient(135deg,var(--text),var(--gold));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.tl-divider{width:60px;height:1px;background:linear-gradient(90deg,transparent,var(--gold),transparent);margin:14px auto 56px}
.timeline{position:relative;padding-left:36px}
.timeline::before{content:'';position:absolute;left:8px;top:8px;bottom:8px;width:1px;background:linear-gradient(to bottom,transparent,rgba(194,80,112,.3) 10%,rgba(194,80,112,.3) 90%,transparent)}
.tl-item{position:relative;margin-bottom:32px;background:var(--glass);border:1px solid var(--glass-b);border-radius:14px;padding:20px 20px 20px 24px;backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);opacity:0;transform:translateX(-16px);transition:opacity .65s ease,transform .65s ease,background .4s,border-color .4s}
.tl-item.visible{opacity:1;transform:translateX(0)}
.tl-dot{position:absolute;left:-44px;top:22px;width:18px;height:18px;border-radius:50%;background:linear-gradient(135deg,var(--rose),var(--gold));box-shadow:0 0 14px rgba(194,80,112,.4);border:2px solid var(--bg);transition:border-color .4s}
.tl-date{font-size:clamp(9px,2.5vw,11px);letter-spacing:.28em;text-transform:uppercase;font-weight:300;color:var(--gold);margin-bottom:7px;opacity:.85}
.tl-title{font-size:clamp(17px,5vw,24px);font-weight:400;color:var(--text);margin-bottom:5px}
.tl-caption{font-size:clamp(13px,3.8vw,16px);font-style:italic;font-weight:300;color:var(--dim);line-height:1.65}
.tl-item.highlight{border-color:rgba(201,149,90,.25)}
[data-theme="light"] .tl-item.highlight{border-color:rgba(138,92,24,.2);background:rgba(255,255,255,.8)}
.tl-item.highlight .tl-dot{background:linear-gradient(135deg,var(--gold-lt),var(--gold));box-shadow:0 0 20px rgba(201,149,90,.5);width:22px;height:22px;left:-46px;top:20px}
.tl-item.highlight .tl-title{color:var(--gold)}

/* ════ MESSAGE ════ */
.message-outer{max-width:700px;margin:0 auto;padding:20px 20px 80px;position:relative;z-index:1}
.message-card{background:var(--glass);border:1px solid var(--glass-b);border-radius:20px;padding:52px clamp(24px,6vw,56px);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);text-align:center;transition:background .4s,border-color .4s}
.heart-row{display:flex;align-items:center;gap:14px;justify-content:center;margin-bottom:36px;color:var(--rose);font-size:14px;opacity:.5}
.heart-row::before{content:'';flex:1;max-width:70px;height:1px;background:linear-gradient(90deg,transparent,var(--rose))}
.heart-row::after{content:'';flex:1;max-width:70px;height:1px;background:linear-gradient(90deg,var(--rose),transparent)}
.quote-mark{font-size:clamp(80px,20vw,120px);line-height:.55;color:var(--rose);opacity:.18;display:block;margin-bottom:10px}
.message-card h3{font-size:clamp(22px,6vw,40px);font-weight:300;color:var(--text);margin-bottom:26px}
.message-card p{font-size:clamp(15px,4vw,19px);font-weight:300;line-height:1.95;color:var(--dim);margin-bottom:18px}
.message-card p em{color:var(--rose);font-style:italic}
.sig{margin-top:38px;font-size:clamp(12px,3vw,14px);letter-spacing:.2em;text-transform:uppercase;font-weight:300;color:var(--gold)}

/* ════ FOOTER ════ */
footer{position:relative;z-index:1;background:var(--foot-bg);text-align:center;padding:30px 16px;font-size:11px;font-weight:300;letter-spacing:.18em;color:var(--foot-t);border-top:1px solid rgba(128,64,64,.1);transition:background .4s,color .4s}

/* ════ SECRET MODAL ════ */
.secret-overlay{position:fixed;inset:0;z-index:2000;background:var(--lb-bg);display:flex;align-items:center;justify-content:center;padding:24px;opacity:0;pointer-events:none;transition:opacity .6s,background .4s;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.secret-overlay.open{opacity:1;pointer-events:all}
.secret-box{max-width:500px;width:100%;text-align:center;background:var(--glass);border:1px solid var(--glass-b);border-radius:24px;padding:clamp(32px,8vw,56px) clamp(24px,6vw,48px);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);animation:secretReveal .9s cubic-bezier(.22,1,.36,1) both;transition:background .4s}
.secret-heart{font-size:clamp(48px,12vw,72px);display:block;margin-bottom:20px;animation:heartbeat 2s ease-in-out infinite;filter:drop-shadow(0 0 24px rgba(194,80,112,.55))}
.secret-box h2{font-size:clamp(24px,6vw,36px);font-weight:300;color:var(--text);margin-bottom:24px}
.secret-box p{font-size:clamp(14px,3.8vw,18px);font-weight:300;line-height:1.9;color:var(--dim);margin-bottom:14px}
.secret-box p em{color:var(--rose);font-style:italic}
.secret-sig{margin-top:28px;font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold)}
.secret-close{margin-top:32px;background:none;border:1px solid rgba(194,80,112,.3);color:var(--rose);font-family:'Cormorant Garamond',Georgia,serif;font-size:13px;letter-spacing:.2em;text-transform:uppercase;font-weight:300;padding:13px 36px;border-radius:40px;cursor:pointer;transition:background .2s;touch-action:manipulation}
.secret-close:hover,.secret-close:active{background:rgba(194,80,112,.1)}

/* ════ KEYFRAMES ════ */
@keyframes fadeUp{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:translateY(0)}}
@keyframes bounce{0%,100%{transform:translateX(-50%) translateY(0)}50%{transform:translateX(-50%) translateY(10px)}}
@keyframes heartbeat{0%,100%{transform:scale(1)}30%{transform:scale(1.22)}60%{transform:scale(1.1)}}
@keyframes secretReveal{from{opacity:0;transform:scale(.9) translateY(24px)}to{opacity:1;transform:scale(1) translateY(0)}}
@keyframes tossIn{0%{opacity:0;transform:rotate(var(--rot,0deg)) translateY(-180px) scale(.6)}70%{opacity:1}100%{opacity:1;transform:rotate(var(--rot,0deg)) translateY(0) scale(1)}}
.reveal{opacity:0;transform:translateY(22px);transition:opacity .75s ease,transform .75s ease}
.reveal.visible{opacity:1;transform:translateY(0)}
</style>
</head>
<body>

<!-- THEME TOGGLE -->
<button class="theme-toggle" id="theme-toggle" aria-label="Toggle theme" title="Switch theme">
  <span id="theme-icon">☀️</span>
</button>

<!-- AURORA -->
<div class="aurora aurora-1"></div>
<div class="aurora aurora-2"></div>
<div class="aurora aurora-3"></div>

<!-- CANVASES -->
<canvas id="stars-canvas"></canvas>
<canvas id="petals-canvas"></canvas>
<canvas id="confetti-canvas"></canvas>

<!-- HERO -->
<section class="hero">
  <div class="hero-content">
    <p class="eyebrow">Happy 23rd Birthday</p>
    <h1 class="hero-name" id="hero-name">Gunu</h1>
    <div class="hero-ornament"><span>♡</span></div>
    <p class="hero-date">September 6 &nbsp;·&nbsp; Forever in my heart</p>
    <p class="tap-hint" id="tap-hint">♡ tap my name for a secret ♡</p>
  </div>
  <div class="scroll-cue">
    <span>scroll</span>
    <svg width="16" height="9" viewBox="0 0 16 9" fill="none">
      <path d="M1 1L8 8L15 1" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" style="color:var(--scroll-c)"/>
    </svg>
  </div>
</section>

<!-- GALLERY -->
<div class="sec-label reveal">
  <h2>22 memories</h2>
  <div class="rose-line"></div>
  <p>Every one worth keeping &nbsp;♡</p>
</div>
<div class="play-row reveal">
  <button class="play-btn" id="play-btn">
    <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
      <circle cx="9" cy="9" r="8.5" stroke="currentColor" stroke-width="1" opacity=".6"/>
      <path d="M7 6l6 3-6 3V6z" fill="currentColor" opacity=".85"/>
    </svg>
    Play our story
  </button>
</div>
<div class="pol-board" id="gallery"></div>

<!-- LIGHTBOX -->
<div class="lightbox" id="lb" role="dialog">
  <div class="lb-story-progress"><div class="lb-story-progress-bar" id="lb-bar"></div></div>
  <button class="lb-close" id="lb-close">✕</button>
  <button class="lb-arrow lb-prev" id="lb-prev">&#8249;</button>
  <div class="lb-frame"><img id="lb-img" src="" alt=""/></div>
  <p class="lb-caption" id="lb-caption"></p>
  <button class="lb-arrow lb-next" id="lb-next">&#8250;</button>
  <span class="lb-counter" id="lb-counter"></span>
</div>

<!-- TIMELINE -->
<section class="timeline-section">
  <h2 class="reveal">Our story so far</h2>
  <div class="tl-divider"></div>
  <div class="timeline">
    <div class="tl-item"><div class="tl-dot"></div><p class="tl-date">December 2024</p><h3 class="tl-title">Where it began</h3><p class="tl-caption">The last days of that year — the first pages of this one.</p></div>
    <div class="tl-item"><div class="tl-dot"></div><p class="tl-date">August 2025</p><h3 class="tl-title">That summer</h3><p class="tl-caption">Some summers stay with you forever. This one did.</p></div>
    <div class="tl-item"><div class="tl-dot"></div><p class="tl-date">October · November 2025</p><h3 class="tl-title">Autumn together</h3><p class="tl-caption">Every season is better with you in it.</p></div>
    <div class="tl-item"><div class="tl-dot"></div><p class="tl-date">December 2025</p><h3 class="tl-title">December magic</h3><p class="tl-caption">Colder outside. Warmer somehow.</p></div>
    <div class="tl-item highlight"><div class="tl-dot"></div><p class="tl-date">January 2026 ✈</p><h3 class="tl-title">The trip</h3><p class="tl-caption">Five days. A hundred memories. All of them mine to keep.</p></div>
    <div class="tl-item"><div class="tl-dot"></div><p class="tl-date">April 2026</p><h3 class="tl-title">Springtime</h3><p class="tl-caption">Everything blooming — including us.</p></div>
    <div class="tl-item"><div class="tl-dot"></div><p class="tl-date">June · July · August 2026</p><h3 class="tl-title">This summer</h3><p class="tl-caption">Still my favourite person to share it all with.</p></div>
    <div class="tl-item highlight"><div class="tl-dot"></div><p class="tl-date">September 6, 2026 ♡</p><h3 class="tl-title">Today — 23</h3><p class="tl-caption">Happy Birthday, Gunu. Here's to every chapter still to come.</p></div>
  </div>
</section>

<!-- MESSAGE -->
<div class="message-outer">
  <div class="message-card reveal">
    <div class="heart-row">♡</div>
    <span class="quote-mark">"</span>
    <h3>For Gunu, on her 23rd</h3>
    <p>Twenty-three years ago the world got something irreplaceable right. And somehow, somewhere along the way, I got lucky enough to be part of your story.</p>
    <p>Thank you for the laughs that made my stomach hurt, the moments that made time stand still, and for being <em>exactly</em> who you are — every quiet, wonderful, radiant version of you.</p>
    <p>Here's to 23 — and every beautiful thing that's waiting for you on the other side.</p>
    <p class="sig">Always yours &nbsp;·&nbsp; Subham &nbsp;♡</p>
  </div>
</div>

<footer>Made with love &nbsp;·&nbsp; Happy Birthday Gunu &nbsp;·&nbsp; September 6, 2026 &nbsp;♡</footer>

<!-- SECRET -->
<div class="secret-overlay" id="secret-overlay">
  <div class="secret-box">
    <span class="secret-heart">♡</span>
    <h2>Hey Gunu.</h2>
    <p>You tapped my name enough times to deserve a secret. So here it is.</p>
    <p>You're my favourite person. The one I think of first when something good happens. The one I want beside me when it doesn't.</p>
    <p>You make ordinary days feel like something worth remembering. And I hope you know — <em>every single moment with you</em> is something I'd choose again and again.</p>
    <p>Happy 23rd. You deserve everything wonderful.</p>
    <p class="secret-sig">— S, always ♡</p>
    <button class="secret-close" id="secret-close">Close</button>
  </div>
</div>

<script>
/* ── THEME TOGGLE ── */
const html = document.documentElement;
const toggleBtn  = document.getElementById('theme-toggle');
const themeIcon  = document.getElementById('theme-icon');

function applyTheme(t) {
  html.setAttribute('data-theme', t);
  themeIcon.textContent = t === 'dark' ? '☀️' : '🌙';
  try { localStorage.setItem('gunu-theme', t); } catch(e){}
}
// restore saved preference
try {
  const saved = localStorage.getItem('gunu-theme');
  if (saved) applyTheme(saved);
} catch(e){}

toggleBtn.addEventListener('click', () => {
  const next = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
  applyTheme(next);
});

/* ── STARS ── */
(function(){
  const cv=document.getElementById('stars-canvas'),ctx=cv.getContext('2d');
  function resize(){cv.width=window.innerWidth;cv.height=window.innerHeight;}
  resize();window.addEventListener('resize',resize);
  const stars=Array.from({length:90},()=>({x:Math.random(),y:Math.random(),r:.4+Math.random()*.9,op:.08+Math.random()*.45,speed:.004+Math.random()*.012,phase:Math.random()*Math.PI*2}));
  let t=0;
  (function loop(){
    ctx.clearRect(0,0,cv.width,cv.height);
    const isDark=html.getAttribute('data-theme')==='dark';
    if(!isDark){t++;requestAnimationFrame(loop);return;} // hide stars in light mode
    stars.forEach(s=>{
      const a=s.op*(0.5+0.5*Math.sin(t*s.speed+s.phase));
      ctx.beginPath();ctx.arc(s.x*cv.width,s.y*cv.height,s.r,0,Math.PI*2);
      ctx.fillStyle=`rgba(255,248,235,${a})`;ctx.fill();
    });
    t++;requestAnimationFrame(loop);
  })();
})();

/* ── CONFETTI ── */
(function(){
  const c=document.getElementById('confetti-canvas'),ctx=c.getContext('2d');
  c.width=window.innerWidth;c.height=window.innerHeight;
  const cols=['#C9955A','#F0B8CA','#C25070','#F6E8D8','#EDD080','#F5C8D4','#fff'];
  const ps=Array.from({length:130},()=>({x:Math.random()*c.width,y:-Math.random()*c.height*.5,w:3+Math.random()*7,h:7+Math.random()*10,r:Math.random()*Math.PI*2,vx:(Math.random()-.5)*3,vy:2.2+Math.random()*3.5,vr:(Math.random()-.5)*.15,col:cols[Math.floor(Math.random()*cols.length)],a:1}));
  let fr=0;
  function draw(){ctx.clearRect(0,0,c.width,c.height);let alive=false;ps.forEach(p=>{p.x+=p.vx;p.y+=p.vy;p.r+=p.vr;if(fr>110)p.a-=.013;if(p.a<=0)return;alive=true;ctx.save();ctx.globalAlpha=Math.max(0,p.a);ctx.translate(p.x,p.y);ctx.rotate(p.r);ctx.fillStyle=p.col;ctx.fillRect(-p.w/2,-p.h/2,p.w,p.h);ctx.restore();});fr++;if(alive||fr<120)requestAnimationFrame(draw);else ctx.clearRect(0,0,c.width,c.height);}
  setTimeout(draw,500);
})();

/* ── HEARTS ── */
(function(){
  const cv=document.getElementById('petals-canvas'),ctx=cv.getContext('2d');
  let W,H;
  function resize(){W=cv.width=cv.offsetWidth;H=cv.height=cv.offsetHeight;}
  resize();window.addEventListener('resize',resize);
  const hs=Array.from({length:40},()=>{const s={};s.reset=function(init){s.x=Math.random()*W;s.y=init?Math.random()*H:H+24;s.sz=5+Math.random()*15;s.vy=.22+Math.random()*.6;s.vx=(Math.random()-.5)*.4;s.op=.05+Math.random()*.18;s.w=Math.random()*Math.PI*2;s.ws=.01+Math.random()*.018;};s.reset(true);s.draw=function(){const sc=s.sz/20;ctx.save();ctx.globalAlpha=s.op;ctx.translate(s.x,s.y);ctx.scale(sc,sc);ctx.beginPath();ctx.moveTo(0,-4);ctx.bezierCurveTo(5,-13,15,-13,15,-2);ctx.bezierCurveTo(15,6,7,13,0,19);ctx.bezierCurveTo(-7,13,-15,6,-15,-2);ctx.bezierCurveTo(-15,-13,-5,-13,0,-4);ctx.closePath();const g=ctx.createLinearGradient(0,-13,0,19);g.addColorStop(0,'#F0B8CA');g.addColorStop(1,'#C25070');ctx.fillStyle=g;ctx.fill();ctx.restore();};s.update=function(){s.w+=s.ws;s.y-=s.vy;s.x+=Math.sin(s.w)*.4+s.vx;if(s.y<-24)s.reset(false);};return s;});
  (function loop(){ctx.clearRect(0,0,W,H);hs.forEach(h=>{h.update();h.draw();});requestAnimationFrame(loop);})();
})();

/* ── GALLERY ── */
const photos=PHOTOS_PLACEHOLDER;
let current=0,storyTimer=null,storyPlaying=false;
const gallery=document.getElementById('gallery');
const lb=document.getElementById('lb');
const lbImg=document.getElementById('lb-img');
const lbCap=document.getElementById('lb-caption');
const lbCtr=document.getElementById('lb-counter');
const lbBar=document.getElementById('lb-bar');
const kbAnims=['kb0','kb1','kb2','kb3','kb4','kb5'];
const rots=[-4,3,-6,5,-2,7,-3,4,-7,2,6,-5,3,-4,7,-3,5,-6,4,-2,6,-4];
const STORY_DUR=4200;

photos.forEach((p,i)=>{
  const wrap=document.createElement('div');wrap.className='pol-wrap';
  const pol=document.createElement('div');pol.className='polaroid';
  pol.style.setProperty('--rot',rots[i%rots.length]+'deg');
  pol.style.setProperty('--delay',(i*55)+'ms');
  const img=document.createElement('img');img.src=p.src;img.alt='Memory '+(i+1);img.loading='lazy';
  const cap=document.createElement('p');cap.className='pol-caption';cap.textContent=p.note;
  pol.appendChild(img);pol.appendChild(cap);wrap.appendChild(pol);
  pol.addEventListener('click',()=>openLB(i));
  gallery.appendChild(wrap);
});

function openLB(i,story){
  current=i;storyPlaying=!!story;
  lbImg.style.animation='none';void lbImg.offsetWidth;
  lbImg.src=photos[i].src;
  lbImg.style.animation=kbAnims[i%kbAnims.length]+' 9s ease-in-out infinite alternate';
  lbCap.style.animation='none';void lbCap.offsetWidth;
  lbCap.textContent=photos[i].note;
  lbCap.style.animation='fadeUp .7s ease both';
  lbCtr.textContent=(i+1)+' / '+photos.length;
  lb.classList.add('open');document.body.style.overflow='hidden';
  lbBar.style.transition='none';lbBar.style.width='0%';void lbBar.offsetWidth;
  if(story){
    lbBar.style.transition='width '+STORY_DUR+'ms linear';lbBar.style.width='100%';
    clearTimeout(storyTimer);
    storyTimer=setTimeout(()=>{if(i+1<photos.length)openLB(i+1,true);else{storyPlaying=false;closeLB();}},STORY_DUR);
  }
}
function closeLB(){lb.classList.remove('open');document.body.style.overflow='';clearTimeout(storyTimer);storyPlaying=false;lbBar.style.width='0%';}
function showNext(){clearTimeout(storyTimer);openLB((current+1)%photos.length,storyPlaying);}
function showPrev(){clearTimeout(storyTimer);openLB((current-1+photos.length)%photos.length,storyPlaying);}
document.getElementById('lb-close').addEventListener('click',closeLB);
document.getElementById('lb-next').addEventListener('click',showNext);
document.getElementById('lb-prev').addEventListener('click',showPrev);
lb.addEventListener('click',e=>{if(e.target===lb)closeLB();});
document.addEventListener('keydown',e=>{if(!lb.classList.contains('open'))return;if(e.key==='Escape')closeLB();if(e.key==='ArrowRight')showNext();if(e.key==='ArrowLeft')showPrev();});
let tx=0;
lb.addEventListener('touchstart',e=>{tx=e.touches[0].clientX;},{passive:true});
lb.addEventListener('touchend',e=>{const dx=e.changedTouches[0].clientX-tx;if(Math.abs(dx)>48)dx<0?showNext():showPrev();});
document.getElementById('play-btn').addEventListener('click',()=>openLB(0,true));

/* ── SECRET ── */
let taps=0,tapTimer=null;
const hint=document.getElementById('tap-hint');
const overlay=document.getElementById('secret-overlay');
document.getElementById('hero-name').addEventListener('click',()=>{
  taps++;clearTimeout(tapTimer);
  if(taps>=5){taps=0;overlay.classList.add('open');document.body.style.overflow='hidden';hint.style.opacity='0';}
  else{hint.style.color='rgba(194,80,112,.8)';tapTimer=setTimeout(()=>{taps=0;hint.style.color='';},2500);}
});
document.getElementById('secret-close').addEventListener('click',()=>{overlay.classList.remove('open');document.body.style.overflow='';});
overlay.addEventListener('click',e=>{if(e.target===overlay){overlay.classList.remove('open');document.body.style.overflow='';}});

/* ── SCROLL REVEAL ── */
const obs=new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting)e.target.classList.add('visible');});},{threshold:.1});
document.querySelectorAll('.reveal,.tl-item').forEach(el=>obs.observe(el));
</script>
</body>
</html>"""

html = TEMPLATE.replace("PHOTOS_PLACEHOLDER", photos_js)
with open(r"C:\Users\subhahalder\Pages\gunu.html","w",encoding="utf-8") as f:
    f.write(html)
mb=os.path.getsize(r"C:\Users\subhahalder\Pages\gunu.html")/1024/1024
print(f"Done — {mb:.2f} MB")
