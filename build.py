# Static page builder for the Absolute Septic concept. Run: python3 build.py
import json
BASE = 'https://absolute-septic-demo.vercel.app/'  # Vercel production URL
TEL, TEL_H = '+19196496044', '(919) 649&#8209;6044'
TEL2, TEL2_H = '+19198733925', '(919) 873&#8209;3925'
HA = 'https://www.homeadvisor.com/rated.AbsoluteSeptic.118185327.html'
WB = 'https://web.archive.org/web/20260607172828/https://absolute-septic.com/'
CERT = 'https://ncowcicb.info/certification-list/'
ORG = {"@context":"https://schema.org","@type":["LocalBusiness","Plumber"],"name":"Absolute Septic, LLC",
 "url":BASE,"telephone":"+1-919-649-6044","foundingDate":"2021-08-12",
 "founder":{"@type":"Person","name":"Cody Staricha"},
 "address":{"@type":"PostalAddress","addressLocality":"Clayton","addressRegion":"NC","postalCode":"27520","addressCountry":"US"},
 "areaServed":["Johnston County, NC","Wake County, NC"],
 "image":BASE+"img/tech-riser.webp","logo":BASE+"img/logo.webp"}
FONTS = 'https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800;900&family=Work+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap'

def K(t, cls=''): return f'<p class="kicker {cls}"><span class="elbow" aria-hidden="true"></span>{t}</p>'
def img(src, alt, w, h, eager=False, cls=''):
    load = ' fetchpriority="high"' if eager else ' loading="lazy" decoding="async"'
    return f'<img src="img/{src}" alt="{alt}" width="{w}" height="{h}"{load}' + (f' class="{cls}"' if cls else '') + '>'
# signature: the pipe. A thick hose green run with an elbow, drawn in on reveal
def PIPE(cls='', h=220):
    return (f'<svg class="pipe {cls}" viewBox="0 0 60 {h}" preserveAspectRatio="none" aria-hidden="true">'
            f'<path class="pipe-run" d="M30 0 V{h-40} q0 30 30 30" pathLength="1"/></svg>')

HEAD = '''<!doctype html><html lang="en" class="no-js"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="description" content="{d}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Absolute Septic (concept)"><meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:url" content="{url}"><meta property="og:image" content="{base}og.png">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{t}"><meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{base}og.png">
<meta name="robots" content="noindex, nofollow"><!-- concept demo, not for indexing -->
<meta name="theme-color" content="#0e100d">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="{fonts}"><link rel="stylesheet" href="{fonts}" media="print" onload="this.media='all'"><noscript><link rel="stylesheet" href="{fonts}"></noscript>
<link rel="stylesheet" href="css/design-system.css"><link rel="stylesheet" href="css/components.css"><link rel="stylesheet" href="css/pages.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%230e100d'/%3E%3Cpath d='M10 4v14q0 8 8 8h10' stroke='%232cbf10' stroke-width='5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E">
<script>document.documentElement.classList.replace('no-js','js-ready')</script><script type="application/ld+json">{ld}</script></head><body>
<a class="skip" href="#main">Skip to content</a>
<div class="demo-bar">Concept by <a href="https://luminarch.pro">LuminArch</a>. Not the official Absolute Septic site. Photos come from Absolute Septic&rsquo;s archived website; placeholders are labeled.</div>
<header class="top"><div class="wrap nav"><a class="mark" href="index.html"><img src="img/logo.webp" alt="Absolute Septic" width="160" height="51"></a>
<button class="menu-btn" aria-expanded="false" aria-controls="menu">Menu</button><ul id="menu">{nav}</ul><a class="btn btn--green btn--call" href="tel:{tel}"><span class="cl-full">{telh}</span><span class="cl-short">Call</span></a></div></header><main id="main">'''

FOOT = f'''</main><footer class="site-foot"><div class="wrap">
<div class="outlet">
 <div class="outlet-l">{PIPE('pipe--foot',160)}<p class="out-k">Tank full, alarm going, yard soggy?</p><p class="out-h">Call the truck.</p><a class="out-num" href="tel:{TEL}">{TEL_H}</a>
 <p class="out-alt">Also listed on Google: <a href="tel:{TEL2}">{TEL2_H}</a></p></div>
 <dl class="out-facts">
  <div><dt>Owner</dt><dd>Cody Staricha</dd></div>
  <div><dt>Yard</dt><dd>Clayton, NC</dd></div>
  <div><dt>Locations</dt><dd>Smithfield and Garner</dd></div>
  <div><dt>NC installer cert.</dt><dd>#9043, Level II</dd></div>
  <div><dt>Septage firm</dt><dd>NCS&#8209;01595</dd></div>
  <div><dt>Hours</dt><dd><span class="ph">Placeholder</span> confirm with Cody</dd></div>
 </dl>
</div>
<nav class="foot-links" aria-label="Footer"><a href="services.html">Services</a><a href="services.html#mulching">Forestry mulching</a><a href="reviews.html">Reviews</a><a href="about.html">About Cody</a><a href="contact.html">Get a quote</a></nav>
<div class="foot-row"><span>Absolute Septic, LLC &middot; Johnston and Wake County, North Carolina</span><span>Concept by <a href="https://luminarch.pro">LuminArch</a></span></div></div></footer>
<script src="js/main.js"></script></body></html>'''

NAV = [('services.html','Services'),('reviews.html','Reviews'),('about.html','About Cody'),('contact.html','Get a quote')]
def bc(*n): return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":a,"item":BASE+b} for i,(a,b) in enumerate(n)]}
def page(fn, t, d, body, ld=None):
    assert 50 <= len(t) <= 60, (fn, len(t), t)
    assert 140 <= len(d) <= 160, (fn, len(d), d)
    nav = ''.join(f'<li><a href="{h}"' + (' aria-current="page"' if h == fn else '') + f'>{n}</a></li>' for h, n in NAV)
    url = BASE + ('' if fn == 'index.html' else fn)
    open(fn,'w').write(HEAD.format(t=t,d=d,url=url,base=BASE,nav=nav,ld=json.dumps(ld or [ORG]),fonts=FONTS,tel=TEL,telh=TEL_H) + body + FOOT)

# Reviews. Google: from the review widget on Absolute Septic's own site, archived 8 Jun 2026. HomeAdvisor: live profile, Oct 2026.
REV = [
 ('Mar 2026','Google','Brooke S.','Cody and Michael were fantastic to work with! They were prompt, honest and friendly! Would definitely recommend them to anyone!',None),
 ('Nov 2025','Google','Brian S.','Cody and team showed up on a moments notice to troubleshoot and repair my system. 5 star experience all around!',None),
 ('Aug 2022','HomeAdvisor','Renee P.','Dante was out here shortly after calling for service. He explained every step of what he was doing. He did not try to sell services that weren&rsquo;t needed. He was very professional, courteous and knowledgeable.','$1,800'),
 ('Jun 2022','HomeAdvisor','Ben M.','Dante and Chris were awesome. Very professional, courteous and polite. I really enjoyed talking with them. I recommend them to everyone. Outstanding job.','$350'),
 ('Jan 2022','HomeAdvisor','Clark C.','Very quick response to my request for service. Came on time and did the job in spite of the rain/snow. My septic tank access was almost 3 feet down, so I got them to install a collar to raise access to just below surface level for future cleanouts.','$850'),
 ('Oct 2021','HomeAdvisor','Philip L.','I had a emergency I call absolute septic first thing in the morning. Cody showed up did an amazing job treated the septic ran through some other clear future problems I may have. Didn&rsquo;t feel pressured at all to fix these problems right away by him.',None),
 ('Dec 2021','HomeAdvisor','Cindee L.','From start to finish Cody and team were fabulous to deal with',None),
 ('Dec 2021','HomeAdvisor','Adrienne W.','Hometown company that provides hometown service!','$300'),
]
def rcard(r, cls=''):
    d,src,who,txt,amt = r
    return (f'<figure class="rcard rv {cls}"><div class="rc-top"><span class="stars" aria-label="5 out of 5">&#9733;&#9733;&#9733;&#9733;&#9733;</span><span>{d}</span></div>'
            f'<blockquote><p>{txt}</p></blockquote><figcaption><b>{who}</b> &middot; {src}' + (f' &middot; job total {amt}' if amt else '') + '</figcaption></figure>')

SERV = [
 ('pump','Septic pumping','Septic tank pump outs for homes and businesses.','tech-riser.webp','Absolute Septic technician working at a septic riser with the pump truck behind him',900,900),
 ('risers','Risers and lids','Deep tanks get risers so the next pump out does not start with a shovel. One customer&rsquo;s lid was almost three feet down.','riser-lids.webp','Green septic riser lids set level with a lawn',760,382),
 ('repair','Repairs, pumps and alarms','Baffles, lines, pump tanks, pump replacement and alarms. Lift stations too.','grease-trap.webp','Hose lowered into an open access lid during service',900,510),
 ('drainfield','Drain field replacement','When the field is saturated, it gets dug out and replaced to the county permit.','drainfield-trench.webp','Drain field trenches cut in red clay with new pipe laid in',720,837),
 ('install','New septic systems','Traditional systems with concrete or plastic tanks, permits handled.','tank-install.webp','A new concrete septic tank set in an excavated hole',900,384),
 ('grease','Grease traps','Pumping and repairs for restaurant grease traps.',None,None,0,0),
 ('dig','Excavation, grading and demolition','Site prep, French drains, sewer repairs, lot clearing, grading and small demolition: sheds, barns and mobile homes.','excavator-yard.webp','Mini excavator digging beside a brick house',760,570),
]

# ---------- HOME ----------
page('index.html','Absolute Septic | Septic Pumping and Repair, Clayton NC',
 'Absolute Septic pumps, repairs and installs septic systems across Johnston and Wake County. Owner Cody Staricha, NC installer #9043. Call (919) 649-6044.', f'''
<section class="hero"><div class="hero-grid">
 <div class="hero-copy rv-static">{K('Septic &middot; Johnston and Wake County','kicker--green')}
  <h1>Pump outs, repairs and new systems. <em>Ask for Cody.</em></h1>
  <p class="lede">Absolute Septic is Cody Staricha&rsquo;s septic company, running a green and white pump truck out of Clayton since 2021 for homes and businesses from Smithfield to Garner and Raleigh.</p>
  <div class="cta"><a class="btn btn--green" href="tel:{TEL}">Call {TEL_H}</a><a class="btn btn--ghost" href="contact.html">Get a quote</a></div>
  <ul class="creds"><li><b>#9043</b>NC onsite wastewater installer, Level II</li><li><b>NCS&#8209;01595</b>On the truck door</li><li><b>2</b>Locations: Smithfield and Garner</li></ul>
 </div>
 <figure class="hero-photo">{PIPE('pipe--hero',420)}{img('tech-riser.webp','Absolute Septic technician fitting pipe at a septic riser, pump truck parked behind him',900,900,eager=True)}<figcaption>On a job, from Absolute Septic&rsquo;s own photos.</figcaption></figure>
</div></section>

<section class="signs wrap" aria-labelledby="sg-h">
 <div class="signs-head rv">{K('When to call')}<h2 id="sg-h">Five signs the tank needs a truck.</h2></div>
 <ol class="signs-list">
  <li class="rv"><b>Slow drains</b><span>Every sink and tub, not just one.</span></li>
  <li class="rv"><b>Gurgling</b><span>Toilets and drains bubbling after a flush.</span></li>
  <li class="rv"><b>Smell</b><span>Sewage odor in the yard or near the tank.</span></li>
  <li class="rv"><b>Soggy ground</b><span>Wet, green patches over the drain field.</span></li>
  <li class="rv"><b>Alarm</b><span>The pump tank alarm is going off.</span></li>
 </ol>
 <p class="fine rv">General septic warning signs, not a diagnosis. If you see any of them, call before it backs up.</p>
</section>

<section class="line" aria-labelledby="ln-h"><div class="wrap line-grid">
 <div class="line-head rv">{K('What the trucks do','kicker--green')}<h2 id="ln-h">From one pump out to a whole new system.</h2><p>The list on Absolute Septic&rsquo;s old website ran to 26 services. These are the ones people call about most.</p><a class="btn btn--green" href="services.html">All services</a></div>
 <ol class="line-list">{''.join(f'<li class="rv"><a href="services.html#{k}"><span class="ln-n">{i+1:02d}</span><b>{n}</b><span class="ln-arrow" aria-hidden="true">&rarr;</span></a></li>' for i,(k,n,*_) in enumerate(SERV))}
  <li class="rv"><a href="services.html#mulching"><span class="ln-n">08</span><b>Forestry mulching</b><span class="tag-new">New in 2026</span></a></li></ol>
</div></section>

<section class="tickets wrap" aria-labelledby="tk-h">
 <div class="tk-head rv">{K('What jobs have cost')}<h2 id="tk-h">Five real job totals.</h2><p>From customers who listed a price with their HomeAdvisor review, 2021 to 2022. Your job will differ; a quote is free.</p></div>
 <ul class="tk-row">{''.join(f'<li class="ticket rv"><span class="tk-amt">{a}</span><span class="tk-what">{w}</span><span class="tk-when">{d}</span></li>' for a,w,d in [('$250','Pump out, on time for the appointment','Oct 2021'),('$300','Septic tank cleaning','Dec 2021'),('$350','Pump out, Dante and Chris','Jun 2022'),('$850','Pump out plus a riser collar on a lid 3 feet down','Jan 2022'),('$1,800','Service call and repair, Dante','Aug 2022')])}</ul>
 <p class="fine rv">Source: <a href="{HA}" rel="noopener">HomeAdvisor</a>. Prices are what each reviewer listed, before 2023. <span class="ph">Placeholder</span> current starting price for a standard pump out.</p>
</section>

<section class="crew" aria-labelledby="cr-h"><div class="wrap crew-grid">
 <div class="crew-copy rv">{K('Who shows up','kicker--green')}<h2 id="cr-h">Customers name the crew.</h2><p>Cody, Michael, Dante and Chris all come up by name in reviews.</p><a class="btn btn--ghost-dark" href="reviews.html">Read the reviews</a></div>
 <div class="crew-cards">{rcard(REV[0],'rcard--big')}{rcard(REV[2])}{rcard(REV[4])}</div>
</div></section>

<section id="mulch" class="mulch wrap" aria-labelledby="mu-h">
 <figure class="mulch-photo rv">{img('forestry-mulcher.webp','Forestry mulcher grinding brush on a lot',800,467)}</figure>
 <div class="mulch-copy rv">{K('New in 2026')}<h2 id="mu-h">Overgrown lot? It gets mulched, not hauled.</h2><p>Absolute Septic added forestry mulching this year: brush and small trees ground into mulch where they stand, for lot clearing, fence lines and overgrowth. Cody posted it to the Google listing on April 23, 2026.</p><a class="btn btn--ghost" href="services.html#mulching">About forestry mulching</a></div>
</section>

<section class="start wrap rv" aria-labelledby="st-h">
 <p class="start-num" aria-hidden="true">$4,000</p>
 <div><h2 id="st-h">That is what Cody had in the bank when he started.</h2><p>Absolute Septic, LLC was formed in August 2021. By April 2022 Cody held his state installer certification, and today the company runs out of Clayton with locations in Smithfield and Garner. <a href="about.html">His story</a>.</p></div>
</section>
''', ld=[ORG, bc(('Home',''))])

# ---------- SERVICES ----------
def svc_block(i, s):
    k,n,d,src,alt,w,h = s
    ph = img(src,alt,w,h) if src else '<div class="photo-ph"><span class="ph">Placeholder</span> grease trap job photo</div>'
    return f'<article id="{k}" class="svc rv"><div class="svc-copy"><span class="svc-n">{i+1:02d}</span><h2>{n}</h2><p>{d}</p></div><figure class="svc-photo">{ph}</figure></article>'
page('services.html','Septic Services, Johnston and Wake County | Absolute Septic',
 'Septic pumping, risers, repairs, alarms, drain fields, new systems, grease traps, excavation and forestry mulching from Absolute Septic. Call (919) 649-6044.', f'''
<section class="page-head"><div class="wrap">{PIPE('pipe--head',200)}<p class="crumbs"><a href="index.html">Home</a> / Services</p>{K('Services','kicker--green')}<h1>Everything between the house and the drain field.</h1>
<p class="lede">Taken from the service list on Absolute Septic&rsquo;s own website, grouped the way customers call.</p></div></section>
<div class="wrap svc-list">{''.join(svc_block(i,s) for i,s in enumerate(SERV))}
<article id="mulching" class="svc svc--feature rv"><div class="svc-copy"><span class="svc-n">08</span><h2>Forestry mulching</h2><p>A mulching head grinds brush and small trees into mulch on the spot. It clears overgrown lots, fence lines and trails without hauling debris away, and the mulch helps hold the soil.</p><p class="note"><span class="ph">Placeholder</span> machine, cutting width, minimum job size and a sample before and after.</p></div><figure class="svc-photo">{img('forestry-mulcher.webp','Forestry mulcher clearing brush',800,467)}</figure></article>
</div>
<section class="wrap how rv" aria-labelledby="how-h"><h2 id="how-h">How a job goes.</h2>
<ol class="how-list"><li><b>Call or send the form</b><span>Someone takes the address and what is going on.</span></li><li><b>A straight price</b><span>A fair price before the work starts.</span></li><li><b>Permits handled</b><span>Repairs and installs that need a county permit get one.</span></li><li><b>Done and cleaned up</b><span>The yard is left the way it was found.</span></li></ol>
<p class="fine">Steps from the &ldquo;simple process&rdquo; on Absolute Septic&rsquo;s old site.</p></section>
''', ld=[ORG, bc(('Home',''),('Services','services.html'))]+[{"@context":"https://schema.org","@type":"Service","name":s[1],"provider":{"@type":"LocalBusiness","name":"Absolute Septic, LLC"},"areaServed":"Johnston County, NC"} for s in SERV]+[{"@context":"https://schema.org","@type":"Service","name":"Forestry mulching","provider":{"@type":"LocalBusiness","name":"Absolute Septic, LLC"},"areaServed":"Johnston County, NC"}])

# ---------- REVIEWS ----------
page('reviews.html','Absolute Septic Reviews | Septic Service in Johnston County',
 'Read what Johnston and Wake County customers say about Cody Staricha and the Absolute Septic crew, from Google and HomeAdvisor. Call (919) 649-6044 today.', f'''
<section class="page-head"><div class="wrap">{PIPE('pipe--head',200)}<p class="crumbs"><a href="index.html">Home</a> / Reviews</p>{K('Reviews','kicker--green')}<h1>Eight customers, in their own words.</h1>
<p class="lede">Every review here names the person or the job. Typos are left in.</p></div></section>
<div class="wrap rv-wall">{''.join(rcard(r) for r in REV)}</div>
<section class="wrap sources rv"><h2>Where these come from</h2>
<p>The two Google reviews were shown in the review widget on Absolute Septic&rsquo;s own website (<a href="{WB}" rel="noopener">archived June 2026</a>). The six HomeAdvisor reviews are on Absolute Septic&rsquo;s <a href="{HA}" rel="noopener">HomeAdvisor profile</a>, rated 5.0 from 10 reviews. Last names are shortened to an initial.</p>
<p class="note"><span class="ph">Placeholder</span> a live Google reviews feed and the current Google rating, once Cody approves which profile to link.</p></section>
''', ld=[ORG, bc(('Home',''),('Reviews','reviews.html'))])

# ---------- ABOUT ----------
page('about.html','About Cody Staricha | Absolute Septic, Clayton NC Septic',
 'Cody Staricha started Absolute Septic in 2021 with $4,000 in the bank. Family owned, state certified installer #9043, serving Johnston and Wake County.', f'''
<section class="page-head page-head--dark"><div class="wrap ab-head">{PIPE('pipe--head',200)}<div><p class="crumbs"><a href="index.html">Home</a> / About</p>{K('About','kicker--green')}<h1>Started with $4,000 in the bank.</h1>
<p class="lede">Absolute Septic is family owned and run by Cody Staricha out of Clayton.</p></div>
<figure class="ab-photo">{img('truck-pump.webp','Absolute Septic pump truck, white with the green logo and 919-649-6044 on the tank',960,720)}<figcaption>The truck, number on the tank.</figcaption></figure></div></section>
<div class="wrap ab">
 <section class="ab-story rv"><h2>Cody&rsquo;s story</h2><p>Cody started Absolute Septic with just $4,000 in his bank account, driven by a desire to help others and a commitment to hard work. He enjoys site work because it helps clients reach their goals, whether that is building a new home or getting a septic system in. His crew takes the extra time to do it right, and the aim is to leave every property the way they found it.</p><p class="fine">Adapted from the About page on Absolute Septic&rsquo;s old website.</p>
 <p class="note"><span class="ph">Placeholder</span> a photo of Cody, how many trucks and people are on the crew now, and whether the senior and first responder discount from the old site still stands.</p></section>
 <section class="ab-facts rv"><h2>On the record</h2><dl>
  <div><dt>Aug 12, 2021</dt><dd>Absolute Septic, LLC formed, per BBB</dd></div>
  <div><dt>Apr 7, 2022</dt><dd>Cody certified as an NC onsite wastewater installer, Level II, #9043. On the state list effective September 26, 2026</dd></div>
  <div><dt>NCS&#8209;01595</dt><dd>Printed on the truck and the old site <span class="ph">TODO verify</span></dd></div>
  <div><dt>2 locations</dt><dd>Smithfield and Garner, per BBB. Yard in Clayton, per the state list</dd></div>
  <div><dt>Apr 23, 2026</dt><dd>Forestry mulching added, per Cody&rsquo;s Google post</dd></div>
 </dl><p class="fine">Sources: <a href="{CERT}" rel="noopener">NCOWCICB certification list</a>, BBB, Google.</p></section>
</div>
''', ld=[ORG, bc(('Home',''),('About','about.html'))])

# ---------- CONTACT ----------
page('contact.html','Get a Septic Quote | Absolute Septic, Smithfield and Garner',
 'Ask Absolute Septic for a septic pumping, repair, install or forestry mulching quote. Smithfield, Garner, Clayton, Raleigh and nearby. Call (919) 649-6044.', f'''
<section class="page-head"><div class="wrap">{PIPE('pipe--head',200)}<p class="crumbs"><a href="index.html">Home</a> / Get a quote</p>{K('Get a quote','kicker--green')}<h1>Tell Cody what is going on.</h1>
<p class="lede">A backup or an alarm going off: call. Anything else: send the form and the office calls back.</p></div></section>
<div class="wrap q-grid">
<form id="qform" class="rv" novalidate>
 <fieldset><legend>What do you need?</legend><div class="chips-in">{''.join(f'<label><input type="radio" name="need" value="{v}"' + (' checked' if i==0 else '') + f'> {v}</label>' for i,v in enumerate(['Pump out','Repair or alarm','Drain field','New system','Grease trap','Excavation','Forestry mulching']))}</div></fieldset>
 <div class="two"><div class="field"><label for="q-name">Name</label><input id="q-name" name="name" autocomplete="name" required></div><div class="field"><label for="q-tel">Phone</label><input id="q-tel" name="tel" type="tel" autocomplete="tel" required></div></div>
 <div class="field"><label for="q-addr">Property address or town</label><input id="q-addr" name="addr" autocomplete="street-address"></div>
 <div class="two"><div class="field"><label for="q-last">Last pumped (if you know)</label><input id="q-last" name="last" placeholder="e.g. 2021"></div><div class="field"><label for="q-lids">Can you see the lids?</label><input id="q-lids" name="lids" placeholder="Yes, no, not sure"></div></div>
 <div class="field"><label for="q-msg">What is going on?</label><textarea id="q-msg" name="msg" rows="4"></textarea></div>
 <button class="btn btn--green" type="submit">Send</button><p id="qmsg" class="note" role="status" aria-live="polite">Demo form. Nothing is sent.</p>
</form>
<aside class="rv"><div class="card"><p class="kicker kicker--green"><span class="elbow" aria-hidden="true"></span>Call</p><a class="phone" href="tel:{TEL}">{TEL_H}</a><p class="fine">On the truck, the state list and BBB. Google lists <a href="tel:{TEL2}">{TEL2_H}</a>.</p></div>
<div class="card card--light"><h2>Where the trucks go</h2><p>Smithfield, Clayton, Garner, Raleigh, Knightdale, Wake Forest, Willow Spring and Benson.</p><p class="fine">Towns listed on the old Absolute Septic site.</p></div></aside>
</div>
''', ld=[ORG, bc(('Home',''),('Get a quote','contact.html'))])

page('404.html','Page Not Found | Absolute Septic, Septic Service Clayton NC',
 'That page is not here. Head back to the Absolute Septic home page, or call (919) 649-6044 for septic pumping, repairs and installs in Johnston and Wake.',
 f'<section class="wrap nf">{K("404","kicker--green")}<h1>Nothing in this line.</h1><p class="lede">The page you wanted is not here.</p><p><a class="btn btn--green" href="index.html">Back to the home page</a></p></section>')
print('built')
