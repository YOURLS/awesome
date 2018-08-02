# Awesome YOURLS [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of awesome things related to YOURLS

## Contents

- [Plugins](#plugins)
  - [0-9](#0-9) | [A](#a) | [B](#b) | [C](#c) | [D](#d) | [E](#e) | [F](#f) | [G](#g) | [H](#h) | [I](#i) | [J](#j) | [K](#k) | [L](#l) | [M](#m) | [N](#n) | [O](#o) | [P](#p) | [Q](#q) | [R](#r) | [S](#s) | [T](#t) | [U](#u) | [V](#v) | [W](#w) | [X](#x) | [Y](#y) | [Z](#z)
- [Translations](#translations)
- [Other platforms and frameworks](#other-platforms-and-frameworks)
- [Other devices and softwares](#other-devices-and-softwares)


## Plugins

### 0-9

- [302-Instead](https://github.com/EpicPilgrim/302-instead) - Send a 302 (temporary) redirect instead of 301 (permanent), for sites where shortlinks may change
- [302-Instead](https://github.com/timcrockford/302-instead) - A fork of previous plugin, with some more options
- [404-Redirect](https://github.com/1Conan/404-redirect-YOURLS) - Set the 404 header if the link ID is unknown

### A

- [Abuse Desk for YOURLS](http://blog.yourls.org/2011/04/yourls-abuse-anti-spam-plugins/) - A Google Safe Browsing implementation for YOURLS to avoid spam links
- [Access Control Allow Origin](https://github.com/TEODE/yourls-access-control-allow-origin) - Prevents CORS issue with domain CNAMES and aliases for admin actions
- [Additional Charsets](https://github.com/josheby/yourls-additional-charsets) - Define additional character sets for short URLs
- [Advanced Reserved URLs](https://github.com/josheby/yourls-advanced-reserved-urls) - Extends the reserved word functionality, blocking short URLs containing reserved words, even if mixed case or written in leetspeak
- [Admin NoReCAPTCHA](https://github.com/amindeed/YOURLS-Admin-NoReCAPTCHA) - Protect logins with Google's No CAPTCHA reCAPTCHA (Google's ReCAPTCHA v2.0)
- [Admin reCaptcha](https://github.com/armujahid/Admin-reCaptcha) - Spam protection for private YOURLS admin interface with reCaptcha
- [Allow Aliases](https://github.com/adigitalife/yourls-allow-aliases) - Allow YOURLS to work with alias hostnames for the server
- [Allow Forward Slashes in Short URLs](https://github.com/williambargent/YOURLS-Forward-Slash-In-Urls) - Just as the name says.
- [Amazon Affiliate](https://github.com/floschliep/YOURLS-Amazon-Affiliate) - Adds your Amazon Affiliate Tag to all Amazon URLs before redirection.
- [Antispam](https://github.com/YOURLS/antispam) ⭐ - Merciless antispam plugin using the 3 major domain blacklists
- [YOURLS APC Cache](http://blog.yourls.org/2011/06/yourls-apc-cache-plugin/) - Add support for APC to reduce MySQL queries
- [API Action](https://github.com/YOURLS/API-action) ⭐ - Example plugin for YOURLS 1.6+ to show how to implement custom API actions
- [API Delete](https://github.com/claytondaley/yourls-api-delete) - Add a "delete" action to the API
- [API Edit URL](https://github.com/timcrockford/yourls-api-edit-url) - Add an "update" action to the API to edit a URL, and a "geturl" action to get the long URL of a short URL
- [Append Query String](https://github.com/drockney/append-qs) - Appends the query string to a long URL- as is
- [Auth Manager](https://github.com/nicwaller/yourls-authmgr-plugin) - Assign users to roles like "Editor" and "Contributor" to limit the changes they are permitted to make (edit URLs, manage plugins...)

### B

- [Blacklist Domains](https://github.com/apelly/YourlsBlacklistDomains) - A simple plugin to blacklist domains from shortening URLs
- [Blacklist IPs](https://github.com/LudoBoggio/YourlsBlacklistIPs) - A simple plugin to blacklist IPs from shortening URLs
- [Bulk Import and Shorten](https://github.com/vaughany/yourls-bulk-import-and-shorten) - Import links from a CSV file
- [Bulk URL Shortening](https://github.com/tdakanalis/bulk_api_bulkshortener) - Shortening of multiple URLs with one API request

### C

- [Cache Stat Pages](https://github.com/YOURLS/cache-stats-pages) ⭐ - Serve stat pages (`http://sho.rt/blah+`) from cache
- [CAS Plugin](https://github.com/nicwaller/yourls-cas-plugin) - Enable authentication through a CAS server
- [Case Insensitive](https://github.com/seandrickson/YOURLS-Case-Insensitive/) - Makes all keywords case insensitive (creates and calls all keywords lowercase)
- [Case Insensitive](https://github.com/adigitalife/yourls-case-insensitive) - Make YOURLS case insensitive: if you create `http://sho.rt/MyLink`, then variations like `mylink` or `MYLINK` will redirect to the same URL.
- [Change Error Messages](https://github.com/adigitalife/yourls-change-error-messages) - Changes the error message when a keyword or URL already exists and displays the long URL.
- [Change Password](https://github.com/vvanasten/YOURLS-Change-Password) - Allow users to change their password via the administration interface.
- [Check URL](https://github.com/adigitalife/yourls-check-url) - Check if a long URL is reachable before creating a short URL
- [API Concurrency Fix](https://bitbucket.org/laceous/yourls-concurrency-fix) - A plugin to resolve concurrency issues with the API as described in Issue 765.
- [Compliance](https://github.com/joshp23/YOURLS-Compliance) - Anti-abuse plugin, designed to address link complaints from 3rd parties.
- [Conditional Toolbar](http://blog.yourls.org/2011/03/yourls-plugin-example-conditional-toolbar/) ⭐ - A plugin to conditionally enable the toolbar: `http://sho.rt/blah` for normal redirect, `http://sho.rt/tb/blah` for a toolbar
- [Custom Header & Footer](https://github.com/scriptgeni/yourls-custom-header-footer) - A plugin administration page to add custom header and footer style and content
- [Custom Javascript](https://github.com/scriptgeni/yourls-custom-javascript) - Add custom javascript to admin pages
- [Custom Protocol](https://github.com/YOURLS/custom-protocol) ⭐ - If the user is known, this plugin adds custom protocol (eg `blah://`) to authorized protocols, otherwise restricts to `http|s`

### D

- [Disable JSONP](https://github.com/seandrickson/YOURLS-Disable-JSONP) - Disables JSONP access for the YOURLS API.
- [DNSBL](https://github.com/Diftraku/yourls_dnsbl/) - Uses various DNSBLs to check the submitter's IP and prevent shortening URLs if any malicious activity has been detected.
- [Domain Limit](https://github.com/nicwaller/yourls-domainlimit-plugin) - Limit the domains that users can create shortlinks to
- [Domain Limiter](https://bitbucket.org/quantumwebco/domain-limiter-yourls-plugin) - Fork of Nic Waller's plugin with the addition of an admin panel to edit the white list from the admin area
- [Don't Log Bots](https://github.com/YOURLS/dont-log-bots) ⭐ - Ignore bot hits in your stats (both click count as seen in the main admin page and in detailed stats)
- [Don't Log Crawlers](https://github.com/luixxiul/dont-log-crawlers/) - A fork of the `Don't Log Bots`, with more bots filtered out.
- [Don't Log Health Checker](https://github.com/guessi/yourls-dont-log-health-checker) - A fork of `Don't Log Bots`, with more bots filtered out.
- [Don't Track Admin Clicks](https://github.com/dgw/yourls-dont-track-admins) - Don't count clicks on short URL if user is logged in

### E

- [Edition Logger](https://github.com/esuarezsantana/yourls-edition-logger) - Logs to a file every url insertion, deletion, or modification, to provide traceability of users' actions allowing an open edition policy.
- [Every Click Counts](https://github.com/BstName/every-click-counts) - Click count include multiple clicks for the same client (ie there will be no browser caching of the redirection)
- [Expiry](https://github.com/joshp23/YOURLS-Expiry) -  Defines optional conditions under which links will expire, able to set time and click limited links globally or per individual links.

### F

- [Fallback URL](http://diegopeinador.blogspot.fr/2013/04/fallback-url-simple-plugin-for-yourls.html) - Redirect to a custom URL when the short URL does not exist
- [Filter Code](https://github.com/ShredCode/YOURLS-filter-code) - Allow to select 3XX Status Code to return per keyword
- [Fix long URLs](https://github.com/adigitalife/yourls-fix-long-url) - Fix long URLs that contain %20 and other similar encodings
- [Force Lowercase](https://github.com/YOURLS/force-lowercase) ⭐ - Force lowercase so `http://sho.rt/ABC` → `http://sho.rt/abc`
- [Fuzzy Keyword Suggestions](https://github.com/philhagen/ltc-fuzzy-keyword-suggestions) - Handles typos and other "near-misses" for any shortened link (eg if you have `sho.rt/dh1ik` but someone types `sho.rt/dhlik`, the 404 page will show suggestions for similar short URLs)

### G

- [GA MP](https://github.com/powerthazan/YOURS-GA-MP-Tracking) - Track YOURLS link clicks with Google Analytics Measurement protocol in Real Time
- [Git Version](https://github.com/chtaube/YOURLS-plugin-gitversion) - Add version information from the git repository into the footer of the admin page
- [Geo API](https://github.com/boxedfish/yourls-Geo-API-plugin) - Plugin to look up country code from another 3rd party API (geoiplookup.net)
- [Google Analytics Link Tagging](http://www.seodenver.com/add-google-analytics-link-tagging-yourls/) - Add GA tags (utm_source and others) to your shortened links
- [Google Auth](https://github.com/8thwall/google-auth-yourls) - Enables Google Authentication for YOURLS
- [Google Analytics YOURLS Plugin](http://www.matbra.com/en/code/google-analytics-yourls-plugin/) - Add your Google Analytics tags to admin and stat pages
- [Google Safe Browsing](https://github.com/YOURLS/google-safe-browsing) ⭐ - Check every new URL against Google's Safe Browsing Lookup service

### H

- [hexdec](https://github.com/plttn/yourls-hexdec) - Changes the sequential keywords from base36 to base16 (ie `[0-9a-f]`)
- [Hide Referrer](https://github.com/Sire/yourls-hide-referrer) - Hide referrer on all or some short links
- [Hide Version String](https://github.com/YOURLS/YOURLS/issues/1878#issuecomment-88450475) - Hide the version string in the footer
- [HTTP:BL](https://github.com/joshp23/YOURLS-httpBL) - Prevent spam using the black list from Project Honeypot.
- [HTTP Proxy](https://github.com/adigitalife/yourls-http-proxy) - Get remote content using an HTTP proxy, for instance when YOURLS is running behind a firewall (e.g. corporate intranet)
- [HTTP status per link](https://github.com/Jelle-S/YOURLS-http-status-per-link) - Plugin to allow you to select `3XX` Status Code to return per keyword.

### I

- [Identi.ca for YOURLS](http://blog.yourls.org/2011/04/yourls-identi-ca-and-tumblr-plugins/) - Share YOURLS links via identi.ca
- [YOURLS IDN](https://github.com/YOURLS/YOURLS-IDN) ⭐ - Add IDN support to YOURLS
- [YOURLS Import Export](https://github.com/GautamGupta/YOURLS-Import-Export) - A plugin to import and export YOURLS URL
- [Integrated QRCodes](https://github.com/joshp23/YOURLS-IQRCodes) - Integrated QRCodes is an updated fork of Inline QRCode, but more compact, configurable, and just as efficient with more features.
- [Interstitial Plugin for YOURLs](https://github.com/joelgratcyk/yourls-interstitial-plugin) - Display an interstitial ad when user clicks on YOURLs link with plugin enabled
- [iOS URL](https://github.com/suculent/yourls-ios-url-schemes-plugin) - Adds support for URLs starting with `itms-apps://` and `itms-services://`
- [iTunes-Affiliate](https://github.com/floschliep/YOURLS-iTunes-Affiliate) - Adds your iTunes Affiliate-Token to all iTunes URLs before redirection

### J

- [Jappix](https://github.com/jonrandoem/yourls-jappix) - Adds a JappixMini chat on your YOURLS admin pages
- [JSON Response](https://github.com/tessus/yourls-json-response) - Add `.json` (or a custom string/character) to the short URL to get info about it as a JSON response.

### K

- [Keywords, Charset & Length](https://github.com/peterberbec/yourls-keyword_charset_length) - Custom charset, custom link length and random short urls, all in one plugin, with an admin panel.
- [Keyword not found](https://github.com/8thwall/keyword-not-found-set-field-yourls) - If keyword isn't found in the database, redirect to admin page and pre-populate the short URL field
- [Keyword Prefix](https://github.com/jangrewe/yourls-keyword-prefix) - Adds a defined prefix to your short URLs

### L

- [LDAP](https://github.com/k3a/yourls-ldap-plugin) - Enables use of LDAP for user authentication.
- [Link Anonymizer](https://github.com/katzwebservices/YOURLS-Link-Anonymizer) - Generate a link that will take you to an anonymizer service.
- [Link List](https://github.com/ruthtillman/yourls-linklist) - List recent links added, in the admin interface or on a public page
- [Limit keyword length](https://github.com/adigitalife/yourls-limit-keyword-length) - This plugin limits the number of characters allowed for the custom keyword.
- [log-login](https://github.com/SweBarre/log-login) - Logs login atempts to YOURLS. To be used with fail2ban.

### M

- [Mailto](https://github.com/peterberbec/yourls-mailto) - Adds a "mailto:" sharing option, next to Twitter and Facebook
- [Mailto Bookmarklet](https://github.com/peterberbec/yourls-mailto-bookmarklet) - Adds a bookmarklet to share links by mail
- [Mass Remove Link](https://github.com/YOURLS/YOURLS/wiki/Plugin-=-Mass-Remove-Link) ⭐ - Remove several links at once. Select by date, date range, IP or URL matching.
- [Mass Update](https://github.com/Binarypark/yourls-api-mass-update) - Adds an API action to mass update links from `old_domain` to `new_domain`
- [Memcached](https://github.com/alexalouit/Yourls-Memcached) - Memcached plugin for YOURLS
- [Meta Redirect](https://github.com/pureexe/Yourls-meta-redirect) - Redirect using HTML meta tag when you prepend the short URL with an underscore (eg `http://sho.rt/_bleh`)
- [Multi User](http://www.matbra.com/en/code/multi-user-yourls-plugin/) - Add support for multiple users
- [Mobile Detect](https://github.com/guessi/yourls-mobile-detect) - Add ability to redirect by user device OS

### N

### O

### P

- [Password Protection](https://github.com/MatthewC/yourls-password-protection) - Password protect any Short URL you want so that users are prompted for a password before redirection
- [Phishtank](http://blog.yourls.org/2011/04/yourls-abuse-anti-spam-plugins/) - Prevent spam links using Phishtank's API
- [Phishtank 2.0](https://github.com/joshp23/YOURLS-Phishtank-2.0) - Functional rewrite of the old Phishtank plugin with more features
- [Piwik Stats](http://code.google.com/p/yourls/issues/detail?id=661) - Integrate statistics with Piwik
- [Piwik-YOURLS](https://github.com/interfasys/piwik-yourls) - Piwik and a few other features
- [Popular Clicks](https://github.com/miconda/yourls/tree/master/plugins/popular-clicks) - Display the top of the most clicked links during past days
- [Popular Clicks Extended](https://github.com/vaughany/yourls-popular-clicks-extended) - Shows which short links get clicked the most during a specific time frame
- [Popular Links](https://github.com/laaabaseball/Yourls-Popular-Links) - Adds an admin page that displays your shortener's most popular links
- [Preview URL](https://github.com/YOURLS/YOURLS/wiki/Plugin-=-Preview-URL) ⭐ - Add the character '~' to a short URL to display a preview screen before redirection
- [Preview URL with QR Code](https://github.com/dennydai/yourls-preview-url-with-qrcode) - Add the character '~' to a short URL to display a preview screen & QR code before redirection
- [Preview URL with QR Code And Thumbnail](https://github.com/prog-it/yourls-preview-url-with-qrcode-thumbnail) - Add the character '~' to a short URL to display a QR code and Thumbnail image before redirection
- [Public "Prefix n' Shorten"](https://github.com/YOURLS/YOURLS/wiki/Plugin-=-Public-Prefix-'n'-Shorten) ⭐ - Redirect `http://sho.rt/http://someurl.com/` to a public interface instead of the admin area
- [YOURLS Pseudonymize](https://github.com/ubicoo/yourls-pseudonymize) - This plugin "pseudonymizes" the IP addresses so that it is in line with the German privacy laws (the last 2 segments/bytes of a visitor's IP address are removed)

### Q

- [QRCode](https://github.com/YOURLS/YOURLS/wiki/Plugin-=-QRCode-ShortURL) ⭐ - Add ".qr" to short URLs to display the shorturl's QR code
- [QRCode](http://techlister.com/plugins-2/qrcode-plugin-for-yourls/354/) - Creates and displays QR Codes within YOURLS
- [QR Google Charts](http://aiaraldea.github.com/qr-google-charts/) - Another QR Code plugin, using Google Charts API
- [QRCode](https://github.com/seandrickson/YOURLS-QRCode-Plugin) - Another QR Code plugin. Get the QR code by simply clicking on a button in the Admin area (or by adding ".qr" to the end of the keyword.)
- [QueryString Forward](https://github.com/llonchj/yourls_plugins) - Forward the query string on short link to long URL (eg `http://sho.rt/kk?a=1` to `http://very.long.url/somepage/?a=1`)
- [Query String Keeper](https://github.com/jessemaps/yourls-query-string-keeper) - Pass the query string from the shortlink to the long URL (eg `http://sho.rt/kk?hey` forwards to `http://longurl/bleh/?hey`)

### R

- [Random Keywords](https://github.com/YOURLS/random-keywords) ⭐ - Assign random keywords to shorturls, like bitly (ie `http://sho.rt/hJudjK`)
- [reCaptcha](https://github.com/spbriggs/recaptcha-plugin) - YOURLS plugin implementing reCaptcha for unauthenticated users in your public interface
- [Redirect Index](https://github.com/tomslominski/yourls-redirect-index) - Redirect the user to another site if they go to the base directory of your YOURLS installation
- [Redirect with GET](https://bitbucket.org/fnkr/yourls-redirect-with-get) - Redirect with all GET parameters (eg `sho.rt/abc123?blah` redirects to `longu.rl/somepage?blah`)
- [Regenerate URL](https://github.com/TheLeonKing/yourls-api-regenerate-url) - Regenerate a new keyword for a URL that has already been shortened.
- [Remove The Share Function](https://github.com/seandrickson/YOURLS-Remove-the-Share-Function) - Remove the Share button and box that toggles the sharing options on the Admin page
- [Remove YouTube Play Indicator](https://github.com/UltraNurd/youtube-play-indicator) - Removes the triangle from the title of Youtube shortened URL
- [Reset URLs](https://gist.github.com/ozh/a0090f46569b50835520d95f9481d9fd) ⭐ - Deletes all URLs. For your test install needs.
- [Reverse Proxy](https://github.com/Diftraku/yourls_reverseproxy) - Fixes the user IPs to point to the actual user instead of your cloud provider’s infrastructure IPs (Cloudflare, Heroku...)
- [rscrub](https://github.com/joshp23/YOURLS-rscrub) - An "HTTP referrer scrubbing swiss army knife for YOURLS" (evolution of the Hide Referrer plugin)

### S

- [Semantic Scuttle](https://github.com/jonrandoem/yourls-semanticscuttle) - Allows the sharing of the URL to a Semantic Scuttle installation.
- [Separate Users](https://github.com/ianbarber/Yourls-Separate-Users) - Adds a username to each created URL, and filters the admin interface.
- [Share Files](http://www.mattytemple.com/projects/yourls-share-files/) - Add a form to upload files and share them using your YOURLS setup.
- [Share G+](https://github.com/ChrTang/yourls-share-gplus) - Adds Google+ to the Quick Share Box.
- [Share LinkedIn](https://github.com/popnt/yourls-linkedin-share) - Adds LinkedIn to the Quick Share Box.
- [Share with Tumblr](https://github.com/YOURLS/YOURLS/wiki/Plugin-=-Share-Tumblr) ⭐ - In the Quick Share box, add a one-click share to Tumblr link.
- [Shibboleth](https://github.com/fuero/yourls-shibboleth) - Enable authentication with Shibboleth
- [ShortShort](https://bitbucket.org/abaumg/yourls-shortshort/) - Checks if a URL is already shortened (e.g. t.co, bit.ly, youtu.be) to avoid nested shortened links.
- [Show Git Branch](https://github.com/ozh/show-git-branch) - Using YOURLS on a dev box under Git? Show the current branch in page footer.
- [SimpleDB Clickqueue](https://github.com/ianbarber/Yourls-SimpleDB-Clickqueue) - Queue clicks to Amazon SimpleDB before processing. This allows using a regular MySQL store even in the face of a high frequency of writes, without concern of connection limit overflow. Clicks are inserted later into the database via an import job.
- [Simple Charset](https://github.com/giveforward/yourls-simplecharset) - Define a custom character set for your short URLs (for instance to generate shorturls only using letters "23456bcdefxyz")
- [Skimlinks](http://www.mattytemple.com/2010/12/yourls-plugin-skimlinks/) - Push all links through Skimlinks to automatically embed affiliate codes
- [Snapshot](https://github.com/joshp23/YOURLS-Snapshot) - Visual preview plugin with image caching powered by PhantomJS.
- [YOURLS Social Toolbar](http://technicalnotebook.com/wiki/display/DEV/YourLS+Social+Toolbar) - A fork of the official sample toolbar plugin, with alternative display for Youtube videos.
- [YOURLS SQLite](https://github.com/ozh/yourls-sqlite) - SQLite driver for YOURLS
- [Static Titles](https://github.com/softius/yourls-static-titles) - Provide two options to avoid the network traffic when retrieving URL titles.
- [SSL for SSL](https://github.com/tipichris/ssl4ssl) - Generates SSL short links if the original link was SSL.
- [Swap Short URL](https://github.com/ggwarpig/Yourls-Swap-Short-Url) - A plugin to have `http://sho.rt/blah` while having YOURLS installed in `http://sho.rt/yourls/`

### T

- [Thumbnail URL image](https://github.com/prog-it/yourls-thumbnail-url) - Get the Thumbnail URL image (long URL) by adding `.i` to the end of the keyword
- [Time Limit Link](https://github.com/chesterrush/yourls-Time-Limit-Link) - Set a time limit for links
- [Track Custom Keyword](https://github.com/timcrockford/track-custom-keywords) - Add a new field to YOURLS designed to track if a keyword was randomly assigned or manually specified
- [Tuber](http://williamscastillo.com/code/yourls/tuber/) - Show the videos that you bookmark in their own page instead of redirecting to the video page. Works with Youtube, Vimeo, Blip.tv and DailyMotion.
- [Typer, a yourls prank plugin](https://github.com/koma5/typer) - Add an underscore * to your shortlink and the user will be shown a page where they have to type the shortlink themselves.

### U

- [Upload and Shorten](https://github.com/fredl99/YOURLS-Upload-and-Shorten) - Upload and share files with YOURLS

### V

- [Virustotal for YOURLS](http://pastie.org/1833229) - Avoid spam links with Virustotal

### W

- [wallabag](https://github.com/jonrandoem/yourls-wallabag) - Allows the sharing of the URL to a Wallabag installation (previously named Poche)

### X

### Y

- [YAPCache](https://github.com/tipichris/YAPCache) - YAPCache is an APC based cache designed to reduce the database load of YOURLS and increase performance

### Z

## Translations

YOURLS supports localization: this means if a language file for YOURLS in available in your language, YOURLS will speak your language!

- [Asturian](https://github.com/artilanes/YOURLS-Translations) (`ast_ES`)
- Brazilian: [here](https://github.com/didi3d/YOURLS-pt_BR) and [here](https://github.com/henriquecrang/YOURLS-pt_BR)  (`pt_BR`)
- [Bulgarian ](https://github.com/VoodooServ/YOURLS-bg_BG) (`bg_BG`)
- [Czech](https://github.com/KubaCZ721/YOURLS-cs_CZ) (`cs_CZ`)
- [Danish](https://github.com/jensz12/YOURLSDK) (`da_DK`)
- [Dutch](https://github.com/Beun/YOURLS-nl_NL) (`nl_NL`)
- [Farsi](https://github.com/saahmadnejad/YOURLS-fa_FA) (`fa_FA`)
- [French](https://github.com/ozh/YOURLS-fr_FR) (`fr_FR`)
- [German](https://github.com/Jules81/YOURLS-de_DE) (`de_DE`)
- [Hebrew](https://github.com/Sinros/YOURLS-he_IL-Translation) (`he_IL`)
- [Hindi](https://github.com/itsKV/YOURLS-Hindi-translation) (`hi-IN`)
- [Indonesian](https://github.com/tigefa4u/YOURLS-1.6-id_ID) (`id_ID`)
- [Italian](https://github.com/ggardin/YOURLS-it_IT) (`it_IT`)
- [Japanese](https://github.com/luixxiul/YOURLS-ja_JP) (`ja_JP`)
- [Korean](https://github.com/at4am/YOURLS-ko_KR) (`ko_KR`)
- [Polish](https://github.com/tomslominski/YOURLS-pl_PL) (`pl_PL`)
- [Portuguese](https://github.com/oscarmarcelo/YOURLS-pt_PT) (`pt_PT`)
- [Russian](https://github.com/nsauk/YOURLS-ru_RU) (`ru_RU`)
- Simplified Chinese: [here](https://github.com/guox/yourls-zh_CN/) and [here](https://github.com/Nilucifel/Yourls_zh-CN) (`zh_CN`)
- [Slovak](https://github.com/RunGroup/YOURLS-sk_SK) (`sk_SK`)
- [Slovenian](https://supan.si/gogs/davidsupan/yourls_trans/src/master) (`sl_SI`)
- [Spanish](https://github.com/kralizeck/YOURLS-es_ES) (`es_ES`)
- [Telugu](https://github.com/kalyan4786/YOURLS_Telugu_Translation) (`te_IN`)
- [Turkish](https://github.com/mugurcagdas/YOURLS_TR) (`tr_TR`)
- [Traditional Chinese](https://github.com/aee1027/YOURLS-zh_TW) (`zh_TW`)
- [Viet Nam](https://github.com/tmtung144/YOURLS) (`vi_VN`)

## Other platforms and frameworks

- [Wordpress](http://wordpress.org/extend/plugins/search.php?q=yourls) : there are numerous [WordPress plugins](http://wordpress.org/extend/plugins/search.php?q=yourls) with YOURLS support. [YOURLS Link Creator](http://wordpress.org/extend/plugins/yourls-link-creator/) is recommended.
- [Drupal](http://drupal.org/project/yourls) : YOURLS plugin (outdated)
- [Drupal alternative](https://www.drupal.org/project/shorten) : A more robust solution. Requires the [title-refetch](https://github.com/joshp23/YOURLS-title-refetch) and [API Concurrency Fix](https://bitbucket.org/laceous/yourls-concurrency-fix) plugins to be installed in YOURLS. See [this](https://www.drupal.org/project/shorten/issues/2889342) Drupal issue for details.
- [CakePHP](https://github.com/driflash/CakePHP-YOURLS-Plugin): plugin to integrate YOURLS

- [status.net](https://github.com/rthees/yourls-status-net): plugin for status.net to use YOURLS
- [Sharetronix](http://developer.sharetronix.com/mpview/12/tag:yourls): YOURLS addon for Sharetronix
- [Perl](http://github.com/pjain/WWW-Shorten-Yourls): a Perl module to shorten URLs using YOURLS
- [Ruby](https://github.com/threestage/yourls): a Ruby wrapper for the YOURLS API
- [Python](http://tflink.github.com/python-yourls/): a Python client for YOURLS
- [VB .Net](http://www.nugardt.com/open-source/yourls-api/): a VB .Net 4.0 wrapper for the YOURLS API
- [Javascript](http://neocotic.com/yourls-api/): JavaScript bindings for the YOURLS API to leverage JSONP support

## Other devices and softwares

- Mac: (Desktop URL shortening tool)[https://www.macupdate.com/app/mac/44088/yourls], (Textexpander)[http://www.chrismarquardt.com/blog.php?id=7952283233607249761]
- Android: (aYourls)[https://play.google.com/store/apps/details?id=de.mateware.ayourls], (URLy)[https://play.google.com/store/apps/details?id=com.mndroid.apps.urly], (URL Shortener)[https://play.google.com/store/apps/details?id=de.keineantwort.android.urlshortener]
- iOS: (ShortTail)[http://adamdehaven.com/blog/2015/05/shorttail-for-yourls-an-elegant-yourls-client-for-iphone/], (Clicklytics)[http://itunes.apple.com/us/app/clicklytics-track-clicks-on/id444008024?mt=8], (myYOURLS)[https://itunes.apple.com/us/app/myyourls/id661934890?mt=8]
- Chrome: (Chrouls)[https://github.com/ukoms/Chrourls]
- Firefox: (YOURLS shortener)[https://addons.mozilla.org/en-us/firefox/addon/yourls-shortener/]
- (Tweetie 2)[http://www.eugenegordin.com/etc/how-to-use-your-custom-yourls-shortener-with-tweetie-2.html]
- (Tweetbot)[http://2fatdads.com/2012/02/how-to-make-yourls-org-work-in-tweetbot/]

## Contribute

Contributions welcome! Read the [contribution guidelines](CONTRIBUTING.md) first.

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0)
