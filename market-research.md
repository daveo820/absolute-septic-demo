# Market research: Absolute Septic, Johnston and Wake County (septic)

Checked 8 October 2026. Lighthouse 12, mobile profile, one run each from the same box, so treat single numbers as rough. Screenshots are in `research/` (compressed).

## 1. Is the lead real?

| Lead claim | What I found | Verdict |
|---|---|---|
| absolute-septic.com returns 404 on every page | 404 on www and bare domain, on the homepage, /about-7290 and /services; 3 repeat requests from the box, a separate fetch from another network, and a real Chrome render on desktop (1440px) and iPhone 13 all got the same black "404 Page not found" screen. Screenshots: `research/current-site-404-desktop.jpg`, `research/current-site-404-mobile.jpg` | Holds up |
| Live through June 2026 | Wayback has 200 captures of the homepage every month from Jan to 7 Jun 2026; nothing after | Holds up |
| Domain | Registered Sept 2021 at GoDaddy, renewed to Sept 2027 (RDAP, last changed 23 Sep 2026), Cloudflare DNS. So Absolute Septic still holds the domain; the site behind it is gone | New detail. Easy to fix: point the domain at a new site |
| Why it died | The old site ran on HighLevel/LeadConnector (the "Client Support Area" and "Web Marketing by Excavation Marketing Pros" footer). A 404 on a live domain usually means the platform account behind it was closed | Likely, not proven. Ask Cody before pitching |
| Google profile shows no website | Job finder's Google Maps screenshot (8 Oct) shows "Add website" | Holds up per screenshot; I could not load Maps reviews myself (limited view) |
| Owner Cody M. Staricha | BBB (Member Manager) and the state certified installer list (Cody Matthew Staricha, cert #9043, Level II, since 4/7/2022, on the list effective 9/26/2026) | Holds up |
| 4.6 from 144 reviews | Exa snapshot (Sep 2026): 4.6 from 144. Google Maps on 8 Oct: 4.4 | Partly wrong: 4.6 is stale, Google shows 4.4 today |
| Active business | Owner Google post 23 Apr 2026 (forestry mulching); newest review that looks genuine is 3 Mar 2026; state certification current through 31 Dec 2026 | Holds up |

## 2. What the old site got wrong (from the June 2026 archive)
- It told visitors to "CALL US 512-641-9695", an Austin, Texas area code, under the main quote button. Almost certainly a leftover from the agency template.
- The About page says Cody serves "Franklin, Wayne, and Orange counties". The service towns are in Wake and Johnston.
- Two sets of hours on the same page: "Mon to Fri 9:00 am to 5:00 pm" and "Monday to Sunday, 12:00 am to 11:59 pm".
- Two phone numbers (873-3925 on the site and Google, 649-6044 on the truck and state records) and four street addresses across listings.
- A "free guide" pop up ("Ignore at your own peril") and 26 thin "near Johnston County" city and blog pages.
- **The review widget.** It showed only 5 star reviews (181 counted). 26 of the 30 shown are dated within six weeks (4 Aug to 17 Sep 2025) and can't be tied to specific jobs, so the demo does not quote them. Details are in the LuminArch notes, not here.

## 3. Competitors

| Site | Where | Perf | A11y | BP | SEO | LCP | Weight |
|---|---|---|---|---|---|---|---|
| dumpandpumpseptic.com | Raleigh | 85 | 72 | 57 | 100 | 1.7s | 3.2 MB |
| bobbydavisseptic.com | Raleigh, Durham | 81 | 93 | 100 | 100 | 4.8s | 0.5 MB |
| smithfieldseptic.com | Smithfield, Johnston County (direct rival) | 76 | 100 | 100 | 100 | 6.0s | 0.9 MB |
| neuseriverseptic.com | Clayton (direct rival) | 73 | 90 | 79 | 92 | 11.3s | 1.8 MB |
| a1septictankplus.com | Raleigh | 66 | 96 | 79 | 100 | 6.3s | 1.4 MB |
| septicblueraleigh.com | Franchise, Raleigh | 46 | 96 | 79 | 85 | 18.6s | 3.5 MB |
| roto-rooter.com | National | 35 | 82 | 71 | 85 | 5.7s | 2.8 MB |
| mrrooter.com/raleigh | Franchise | 26 | 67 | 57 | 85 | 28.7s | 89 MB |
| **absolute-septic.com today** | | n/a | | | | | 404 |
| **Absolute Septic concept (local, uncompressed)** | | **98** | **100** | **100** | 66* | 2.1s | 237 KiB |

\* SEO is held down on purpose by noindex and the robots.txt block. The only SEO audit it fails is the crawl block.

### What the strong sites do
1. **The truck is the hero.** Bobby Davis, Septic Blue and Neuse River all lead with their own pump truck or tech. Absolute has the same asset: a clean branded truck and a tech at a riser.
2. **Phone first.** Smithfield Septic puts the number in the hero, the header and a sticky bar. Every rival has it in the header.
3. **Johnston County by name.** Smithfield Septic's h1 is "Septic Tank Pumping in Smithfield and Johnston County"; Neuse River names Clayton. Absolute's best towns are the same ones.
4. **A trust number.** Bobby Davis shows "30 years in business"; Mr. Rooter shows 1,035 reviews at 4.7. Absolute's honest equivalents are the state installer certification and named crew members in reviews.
5. **Plain answers.** Smithfield Septic asks for the address and what the system is doing, which is exactly what a septic call needs.

### Where the opening is
- The two direct Johnston County rivals score 73 and 76 on performance and take 6 to 11 seconds to show their main content on a phone. A fast, phone first site is a real edge in a trade where people search in a panic.
- Nobody in the set gives straight price examples. Absolute has five real ones from HomeAdvisor ($250 to $1,800).
- Forestry mulching is new, and none of these septic rivals offer it on their sites.

## 4. Risks for the pitch
- **Reviews.** See section 2. Any review growth plan has to be real review requests after real jobs.
- **Rating is sliding:** 4.6 in the September snapshot, 4.4 on Google today. BBB rating is B minus for one unanswered complaint.
- **Phone numbers.** If 873-3925 is a tracking number from the closed platform, it may stop ringing. Worth asking Cody first; that alone could be the hook.
- **He may already be rebuilding** with the same or another agency. The domain was renewed on 23 Sep 2026.
- **Photos:** a couple of the archived photos (mulcher, excavator) could be agency stock.
