from flask import Flask, render_template_string, url_for


app = Flask(__name__)


# --- CSS STYLES ---


# We'll share common styles to avoid repetition
COMMON_STYLES = """
:root{
   --bg:#1a0b00;
   --panel:#24110a;
   --accent:#ff9a3c;
   --accent-2:#ff6f00;
   --muted:#d8b79a;
   --support-accent:#32e3a6;
   --support-accent-2:#00b875;
   --radius:12px;
   --maxw:900px;
}
*{box-sizing:border-box}
html,body{height:100%}
body{
   margin:0;
   font-family:Inter, system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
   background:linear-gradient(180deg,#120700 0%, #1a0b00 60%);
   color:#fff6ee;
   display:flex;
   align-items:flex-start;
   justify-content:center;
   padding:40px 20px;
   position:relative;
   overflow-x:hidden;
   min-height:100vh;
   /* Current padding-top to push content even further down */
   padding-top: 180px;
}
.moon-img{
   position:fixed;
   top:18px;
   right:18px;
   width:44px;
   height:44px;
   border-radius:50%;
   object-fit:cover;
   box-shadow: 0 6px 20px rgba(0,0,0,0.4), 0 0 20px rgba(255,140,0,0.06);
   border:1px solid rgba(255,255,255,0.03);
   background:#000;
   z-index: 1000;
}
.wrap{
   width:100%;
   max-width:var(--maxw);
   text-align:center;
}
.sr-only{position:absolute;left:-10000px;top:auto;width:1px;height:1px;overflow:hidden;}


/* --- FIXED HEADER CONTAINER --- */
.fixed-nav-header {
   position: fixed;
   top: 0;
   left: 0;
   width: 100%;
   z-index: 50;
   background: var(--bg);
   box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
   padding: 12px 0;
   border-bottom: 1px solid rgba(255,255,255,0.02);
}


/* --- TABS NAVIGATION --- */
.nav-tabs {
   display: flex;
   justify-content: center;
   gap: 8px;
   padding: 0;
   background: transparent;
   border-radius: 0;
   border: none;
   max-width: 550px; /* Increased max width to fit 4 tabs */
   margin: 0 auto;
}
.nav-tab {
   display: block;
   text-decoration: none;
   color: var(--muted);
   font-weight: 700;
   font-size: 14px;
   padding: 10px 20px;
   border-radius: 100px;
   transition: background-color 0.2s ease, color 0.2s ease;
   flex: 1;
   text-align: center;
   white-space: nowrap;
}
.nav-tab:hover {
   background-color: rgba(255,255,255,0.05);
   color: #fff;
}
.nav-tab.active {
   background: linear-gradient(180deg,var(--accent),var(--accent-2));
   color: #2b0f00;
   box-shadow: 0 4px 15px rgba(255,140,0,0.1);
}
.nav-tab.active.support-tab {
   --accent: var(--support-accent);
   --accent-2: var(--support-accent-2);
   box-shadow:0 4px 15px rgba(50,227,166,0.12);
}
/* --- END TABS NAVIGATION --- */


.cta{
   display:inline-block;
   text-decoration:none;
   background:linear-gradient(180deg,var(--accent),var(--accent-2));
   color:#2b0f00;
   padding:14px 22px;
   border-radius:12px;
   font-weight:800;
   box-shadow:0 8px 30px rgba(255,140,0,0.08);
   transition:transform .14s ease, box-shadow .14s ease;
   white-space: nowrap;
}
.cta:hover{transform:translateY(-3px); box-shadow:0 18px 50px rgba(255,140,0,0.12)}


@media (max-width:540px){
   .moon-img{width:36px;height:36px;top:12px;right:12px}
   /* Mobile padding remains the same */
   body { padding-top: 120px; }
   .nav-tabs {
       max-width: 100%;
       gap: 4px;
       padding: 0 8px; /* Added horizontal padding for small screens */
   }
   .nav-tab {
       font-size: 11px; /* Smaller font for more tabs on mobile */
       padding: 8px 6px; /* Reduced padding for more tabs on mobile */
   }
}
"""


# --- HTML TEMPLATES ---


# Main Index Page (Home)
INDEX_HTML = """<!doctype html>
<html lang="en">
<head>
   <meta charset="utf-8" />
   <meta name="viewport" content="width=device-width,initial-scale=1" />
   <title>Melee at Night | Home</title>
   <style>
       /* --- COMMON STYLES --- */
       {{ COMMON_STYLES|safe }}
       /* --- PAGE-SPECIFIC STYLES --- */
       header.content-header{
           padding:48px 24px;
           background:linear-gradient(180deg, rgba(255,255,255,0.02), transparent);
           border-radius:16px;
           border:1px solid rgba(255,255,255,0.03);
           box-shadow:0 12px 40px rgba(30,10,0,0.6);
           margin-bottom: 22px;
       }
       h1{
           margin:0 0 8px 0;
           font-size:48px;
           letter-spacing:-1px;
           line-height:1;
           font-weight:800;
           color:var(--accent);
           text-shadow:0 6px 24px rgba(255,140,0,0.06);
       }
       p.lead{
           margin:0 0 0 0;
           color:var(--muted);
           font-size:15px;
       }
       .cta-group {
           display: flex;
           justify-content: center;
           gap: 12px;
           flex-wrap: wrap;
           margin-top: 20px;
       }
       main{
           background:transparent;
           text-align:left;
           padding:24px;
           border-radius:12px;
       }
       .about{
           background:rgba(255,255,255,0.01);
           padding:18px;
           border-radius:10px;
           border:1px solid rgba(255,255,255,0.02);
           color:var(--muted);
           font-size:15px;
           line-height:1.5;
       }
       footer{
           margin-top:18px;
           display:flex;
           gap:12px;
           justify-content:center;
           align-items:center;
           padding-top:18px;
       }
       .icon-link{
           width:44px;
           height:44px;
           display:inline-flex;
           align-items:center;
           justify-content:center;
           border-radius:10px;
           background:rgba(255,255,255,0.02);
           color:var(--accent);
           text-decoration:none;
           border:1px solid rgba(255,255,255,0.03);
           transition:transform .12s ease, background .12s ease;
       }
       .icon-link:hover{transform:translateY(-4px); background:rgba(255,160,80,0.06)}


       @media (max-width:540px){
           h1{font-size:34px}
           .cta{padding:12px 18px}
       }
   </style>
</head>
<body>
   <img class="moon-img" src="{{ url_for('static', filename='moon.png') }}" alt="Melee at Night logo">


   <div class="fixed-nav-header">
       <nav class="nav-tabs" aria-label="Main navigation">
           <a class="nav-tab active" href="/">Home</a>
           <a class="nav-tab" href="/schedule">Schedule</a>
           <a class="nav-tab" href="/rankings">Rankings</a>
           <a class="nav-tab support-tab" href="/support">Support Us</a>
       </nav>
   </div>


   <div class="wrap" role="main">
       <header class="content-header">
           <h1>Melee at Night</h1>
           <p class="lead">Daily online Super Smash Bros. Melee tournaments every night.</p>


           <div class="cta-group">
               <a class="cta" href="https://www.start.gg/hub/melee-at-night/details" rel="noopener" target="_blank">Sign Up Here</a>
           </div>
       </header>


       <main>
           <section class="about" aria-labelledby="about-title">
               <h2 id="about-title" style="margin:0 0 8px 0; color:#ffe8cc; font-size:18px;">About Melee at Night</h2>
               <p style="margin:0;">
                   We are a daily online Super Smash Bros. Melee tournament that takes place every night. We also run a weekly Noobs-only tournament, a Monthly tournament, and many more special events. Join our Discord to get started!
               </p>
           </section>


           <footer>
               <a class="icon-link" href="https://discord.gg/SG2X4ESNXz" rel="noopener" target="_blank" aria-label="Discord">
                   <svg width="20" height="20" viewBox="0 0 71 55" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                       <path d="M60.104 4.41A58.99 58.99 0 0044.64.1a41.21 41.21 0 00-1.94 4.03 55.7 55.7 0 00-12.52 0 41.1 41.1 0 00-1.93-4.03C26.36.1 10.9 4.41 10.9 4.41c-6.37 11.23-7.12 21.07-6.32 30.7 0 0 7.04 5.03 12.9 8.3 0 0 3.63-4.37 6.6-8.02 0 0-2.09-.62-3.03-1.06 5.7-1.63 11.16-1.63 16.1 0-.94.44-3.03 1.06-3.03 1.06 2.97 3.65 6.6 8.02 6.6 8.02 5.86-3.27 12.9-8.3 12.9-8.3.8-9.63.05-19.47-6.32-30.7z" fill="currentColor"/>
                       <path d="M23.76 33.1c-2.08 0-3.77-1.9-3.77-4.23 0-2.33 1.69-4.23 3.77-4.23 2.09 0 3.78 1.9 3.77 4.23 0 2.33-1.68 4.23-3.77 4.23zM47.24 33.1c-2.08 0-3.77-1.9-3.77-4.23 0-2.33 1.69-4.23 3.77-4.23 2.09 0 3.78 1.9 3.77 4.23 0 2.33-1.68 4.23-3.77 4.23z" fill="#021018"/>
                   </svg>
               </a>
               <a class="icon-link" href="https://www.youtube.com/channel/UCZv8Bu0yyJ4M3q8ypZJTeaA" rel="noopener" target="_blank" aria-label="YouTube">
                   <svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
                       <path d="M23.498 6.186a2.99 2.99 0 0 0-2.106-2.117C19.42 3.5 12 3.5 12 3.5s-7.42 0-9.392.569A2.99 2.99 0 0 0 .502 6.186C0 8.186 0 12 0 12s0 3.814.502 5.814a2.99 2.99 0 0 0 2.106 2.117C4.58 20.5 12 20.5 12 20.5s7.42 0 9.392-.569a2.99 2.99 0 0 0 2.106-2.117C24 15.814 24 12 24 12s0-3.814-.502-5.814zM9.75 15.02V8.98L15.5 12l-5.75 3.02z" fill="currentColor"/>
                   </svg>
               </a>
               <a class="icon-link" href="https://www.twitch.tv/melee_at_night" rel="noopener" target="_blank" aria-label="Twitch">
                   <svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
                       <path d="M4 2v14l3 3h4l3 3v-3h2l3-3V2H4zm15 10h-3v3h-2v-3H8V4h11v8zM10 7h2v4h-2zM14 7h2v4h-2z" fill="currentColor"/>
                   </svg>
               </a>
               <a class="icon-link" href="https://twitter.com/MeleeAtNight" rel="noopener" target="_blank" aria-label="X">
                   <svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
                       <path d="M5.636 4.222a1 1 0 0 1 1.414 0L12 9.172l4.95-4.95a1 1 0 1 1 1.414 1.415L13.414 10.586l4.95 4.95a1 1 0 0 1-1.414 1.414L12 12l-4.95 4.95a1 1 0 1 1-1.414-1.414l4.95-4.95-4.95-4.95a1 1 0 0 1 0-1.414z" fill="currentColor"/>
                   </svg>
               </a>
           </footer>
       </main>
   </div>
</body>
</html>
"""


# Schedule Page HTML
SCHEDULE_HTML = """<!doctype html>
<html lang="en">
<head>
   <meta charset="utf-8" />
   <meta name="viewport" content="width=device-width,initial-scale=1" />
   <title>Melee at Night | Schedule</title>
   <style>
       /* --- COMMON STYLES --- */
       {{ COMMON_STYLES|safe }}
       /* --- PAGE-SPECIFIC STYLES --- */
       .content-box{
           width:100%;
           max-width:550px;
           text-align:center;
           padding: 30px;
           background:rgba(255,255,255,0.01);
           border-radius:16px;
           border:1px solid rgba(255,255,255,0.03);
           box-shadow:0 12px 40px rgba(30,10,0,0.6);
           margin: 0 auto;
       }
       h2{
           margin:0 0 12px 0;
           font-size:32px;
           color:var(--accent);
           text-align:center;
       }
       .schedule-list {
           list-style: none;
           padding: 0;
           margin: 20px 0 0 0;
       }
       .schedule-item {
           display: flex;
           justify-content: space-between;
           align-items: center;
           background: var(--panel);
           margin-bottom: 10px;
           padding: 15px 20px;
           border-radius: var(--radius);
           border-left: 5px solid var(--accent);
           text-align: left;
           transition: border-color 0.2s ease;
       }
       /* Style for weekly/special tournaments */
       .schedule-item.weekly {
            border-left-color: var(--support-accent);
       }
       .schedule-item.noobtube {
            border-left-color: #e33232; /* Red color for NoobTube */
       }
       .schedule-item strong {
           color: #fff;
           font-size: 16px;
           display: block;
           margin-bottom: 2px;
       }
       .schedule-item span {
           color: var(--muted);
           font-size: 14px;
       }
       .time {
           font-weight: 800;
           color: var(--accent);
           font-size: 18px;
           flex-shrink: 0;
           margin-left: 15px;
       }
       .time-weekly {
            color: var(--support-accent);
       }
       .time-noobtube {
           color: #e33232; /* Red color for NoobTube time */
       }
   </style>
</head>
<body>
   <img class="moon-img" src="{{ url_for('static', filename='moon.png') }}" alt="Melee at Night logo">


   <div class="fixed-nav-header">
       <nav class="nav-tabs" aria-label="Main navigation">
           <a class="nav-tab" href="/">Home</a>
           <a class="nav-tab active" href="/schedule">Schedule</a>
           <a class="nav-tab" href="/rankings">Rankings</a>
           <a class="nav-tab support-tab" href="/support">Support Us</a>
       </nav>
   </div>


   <div class="wrap" role="main">
       <div class="content-box">
           <h2>Tournament Schedule</h2>
           <p style="color:var(--accent); font-weight:700;">All times are in Eastern Time (ET)</p>


           <ul class="schedule-list">
               <li class="schedule-item">
                   <div>
                       <strong>Melee at Night (Daily)</strong>
                       <span>The main singles event, every day.</span>
                   </div>
                   <div class="time">10:00 PM</div>
               </li>
               <li class="schedule-item noobtube">
                   <div>
                       <strong>The NoobTube</strong>
                       <span>Singles tournament for newer players. Every Monday.</span>
                   </div>
                   <div class="time time-noobtube">8:00 PM</div>
               </li>
               <li class="schedule-item weekly">
                   <div>
                       <strong>Doubles Night</strong>
                       <span>2 vs 2 Melee action! Every Saturday.</span>
                   </div>
                   <div class="time time-weekly">8:00 PM</div>
               </li>
           </ul>


           <p style="text-align:center; margin-top:20px; font-weight: 700;">... and many more!</p>
           <p style="text-align:center; margin-top:10px; font-size:14px;">
               Please join the
               <a href="https://discord.gg/SG2X4ESNXz" style="color:var(--accent); text-decoration:underline; font-weight:700;">Discord</a>
               for up to date tournament announcements.
           </p>
       </div>
   </div>
</body>
</html>
"""


# Support Page HTML
SUPPORT_HTML = """<!doctype html>
<html lang="en">
<head>
   <meta charset="utf-8" />
   <meta name="viewport" content="width=device-width,initial-scale=1" />
   <title>Melee at Night | Support</title>
   <style>
       /* --- COMMON STYLES --- */
       {{ COMMON_STYLES|safe }}
       /* --- PAGE-SPECIFIC STYLES --- */
       .content-box{
           width:100%;
           max-width:450px;
           text-align:center;
           padding: 30px;
           background:rgba(255,255,255,0.01);
           border-radius:16px;
           border:1px solid rgba(255,255,255,0.03);
           box-shadow:0 12px 40px rgba(30,10,0,0.6);
           /* Centering applied to the content-box */
           margin: 0 auto;
       }
       h2{
           margin:0 0 30px 0;
           font-size:32px;
           color:var(--accent);
           text-align:center;
       }
       /* VIP Button Styles */
       .vip-cta {
           background: linear-gradient(180deg, #ffc700, #ff9a00); /* Gold/VIP color */
           color: #382500 !important;
           font-size: 1.2em;
           padding: 16px 30px;
           box-shadow: 0 10px 40px rgba(255, 199, 0, 0.2);
           border: none;
           cursor: pointer;
       }
       .or-text {
           margin: 25px 0 20px 0;
           font-size: 16px;
           font-weight: 600;
           color: var(--muted);
       }
       .bitcoin-box {
           padding: 20px;
           background: var(--panel);
           border-radius: var(--radius);
           border: 1px solid rgba(255, 255, 255, 0.05);
           display: inline-block;
           max-width: 90%;
           text-align: center;
       }
       .bitcoin-box p {
           margin: 0 0 8px 0;
           color: var(--muted);
       }
       .address-group {
           display: flex;
           align-items: center;
           justify-content: center;
           gap: 10px;
           background: #120700;
           padding: 8px 12px;
           border-radius: 8px;
           font-family: monospace;
           overflow-x: auto;
           max-width: 100%;
       }
       #bitcoin-address {
           color: #b3ffb3; /* Light green for Bitcoin address */
           font-size: 14px;
           user-select: all;
           word-break: break-all;
           text-align: left;
           flex-grow: 1;
       }
       .copy-btn {
           background: var(--accent);
           color: #2b0f00;
           padding: 8px 12px;
           border: none;
           border-radius: 6px;
           cursor: pointer;
           font-weight: 700;
           transition: background-color 0.1s, transform 0.1s;
           flex-shrink: 0;
       }
       .copy-btn:active {
           transform: scale(0.95);
       }
       .copy-btn:hover {
           background: var(--accent-2);
       }
       @media (max-width: 480px) {
           .content-box { padding: 20px; }
           #bitcoin-address { font-size: 12px; }
           .copy-btn { font-size: 12px; padding: 6px 10px; }
       }
   </style>
</head>
<body>
   <img class="moon-img" src="{{ url_for('static', filename='moon.png') }}" alt="Melee at Night logo">


   <div class="fixed-nav-header">
       <nav class="nav-tabs" aria-label="Main navigation">
           <a class="nav-tab" href="/">Home</a>
           <a class="nav-tab" href="/schedule">Schedule</a>
           <a class="nav-tab" href="/rankings">Rankings</a>
           <a class="nav-tab support-tab active" href="/support">Support Us</a>
       </nav>
   </div>


   <div class="wrap" role="main">
       <div class="content-box">
           <h2>Support Melee at Night</h2>


           <a class="cta vip-cta"
              href="https://patreon.com/MeleeatNight?utm_medium=unknown&utm_source=join_link&utm_campaign=creatorshare_creator&utm_content=copyLink"
              rel="noopener"
              target="_blank">
               V.I.P (Patreon)
           </a>


           <p class="or-text">OR</p>


           <div class="bitcoin-box">
               <p>Bitcoin Donation</p>
               <div class="address-group">
                   <span id="bitcoin-address">bc1qurhvvkyc5ys2rmj478l8r7hnyct65tzy0js38g</span>
                   <button class="copy-btn" onclick="copyAddress(this)">Copy</button>
               </div>
           </div>
       </div>
   </div>


   <script>
       function copyAddress(buttonElement) {
           const address = document.getElementById('bitcoin-address').textContent;
           const tempInput = document.createElement('textarea');
           tempInput.value = address;
           document.body.appendChild(tempInput);
           tempInput.select();
           let originalText = buttonElement.textContent;
           let success = false;
           try {
               success = document.execCommand('copy');
           } catch (err) {
               console.error('Copy failed: ', err);
           }
           document.body.removeChild(tempInput);
           if (success) {
               buttonElement.textContent = 'Copied!';
               setTimeout(() => {
                   buttonElement.textContent = originalText;
               }, 1500);
           } else {
                buttonElement.textContent = 'Failed';
                setTimeout(() => {
                   buttonElement.textContent = originalText;
                }, 1500);
           }
       }
   </script>
</body>
</html>
"""


# --- RANKINGS PAGE ---
RANKINGS_HTML = """<!doctype html>
<html lang="en">
<head>
   <meta charset="utf-8" />
   <meta name="viewport" content="width=device-width,initial-scale=1" />
   <title>Melee at Night | Rankings</title>
   <style>
       /* --- COMMON STYLES --- */
       {{ COMMON_STYLES|safe }}
       /* --- PAGE-SPECIFIC STYLES --- */
       .content-box{
           width:100%;
           text-align:center;
           padding: 40px 30px;
           background:rgba(255,255,255,0.01);
           border-radius:16px;
           border:1px solid rgba(255,255,255,0.03);
           box-shadow:0 12px 40px rgba(30,10,0,0.6);
       }
       h2{
           margin:0 0 12px 0;
           font-size:32px;
           color:var(--accent);
           text-align:center;
       }
       p {
           color: var(--muted);
           font-size: 16px;
           line-height: 1.6;
           margin: 0;
       }
   </style>
</head>
<body>
   <img class="moon-img" src="{{ url_for('static', filename='moon.png') }}" alt="Melee at Night logo">


   <div class="fixed-nav-header">
       <nav class="nav-tabs" aria-label="Main navigation">
           <a class="nav-tab" href="/">Home</a>
           <a class="nav-tab" href="/schedule">Schedule</a>
           <a class="nav-tab active" href="/rankings">Rankings</a>
           <a class="nav-tab support-tab" href="/support">Support Us</a>
       </nav>
   </div>


   <div class="wrap" role="main">
       <div class="content-box">
           <h2>Rankings</h2>
           <p>This page is under construction. Check back soon!</p>
           <br>
           <p>For now, please see the external rankings document:</p>
           <br>
           <a class="cta"
              href="https://docs.google.com/document/d/1tLmDPMMN1ocRrvV8Sj-9Ru2lFBkHMnHyj4rxaYmbujA/edit?tab=t.0"
              target="_blank"
              rel="noopener">
               View External Rankings
           </a>
       </div>
   </div>
</body>
</html>
"""




# --- FLASK ROUTES ---


@app.route("/")
def index():
   """Renders the main landing page."""
   return render_template_string(INDEX_HTML, COMMON_STYLES=COMMON_STYLES)




@app.route("/schedule")
def schedule():
   """Renders the new schedule page."""
   return render_template_string(SCHEDULE_HTML, COMMON_STYLES=COMMON_STYLES)




@app.route("/rankings")
def rankings():
   """Renders the rankings page."""
   return render_template_string(RANKINGS_HTML, COMMON_STYLES=COMMON_STYLES)




@app.route("/support")
def support():
   """Renders the custom support/donation page."""
   return render_template_string(SUPPORT_HTML, COMMON_STYLES=COMMON_STYLES)




if __name__ == "__main__":
   # For production use a real WSGI server; this is for local testing only
   app.run(host="0.0.0.0", port=5000, debug=True)



