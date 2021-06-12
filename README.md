# Awesome YOURLS [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [<img src="https://github.com/YOURLS/YOURLS/raw/master/images/yourls-logo.svg" alt="YOURLS Logo" align="right" height="120">](https://github.com/YOURLS/awesome-yourls/) [![Listed in Awesome YOURLS!](https://img.shields.io/badge/Awesome-YOURLS-C5A3BE)](https://github.com/YOURLS/awesome-yourls/)

> A curated list of **awesome things** related to **[YOURLS](https://github.com/YOURLS/YOURLS)**

## Contents

- [Official Links](#official-links-) - Official guides and tools
- [Plugins](#plugins-) - what makes YOURLS so versatile and powerful.
  Currently: **<!--plugin_count-->185<!--/plugin_count-->** plugins listed.<!-- DO NOT UPDATE THIS COUNT MANUALLY -->
- [Themes](#themes-) - to customize how YOURLS looks
- [Translations](#translations-) - YOURLS in your language
- [Integrations](#integrations-) - Third-party integrations and frameworks
- [Guides & tutorials](#guides--tutorials-) - Community resources
- [Showcases](#showcases-) - Inspiration and celebrity endorsements

*Something missing or incorrect ? Want to get your work listed ? See how you can [contribute](CONTRIBUTING.md) !*

## Official Links [⇪](#readme)

Official material from the YOURLS team

- [Official Readme](https://yourls.org)
- [GitHub Repo](https://github.com/YOURLS/YOURLS)
- [Release Notes](https://github.com/YOURLS/YOURLS/releases)
- [YOURLS News](https://blog.yourls.org/)
- [Community Discussions](https://github.com/YOURLS/YOURLS/discussions)
- [YOURLS using Docker](https://hub.docker.com/_/yourls/)
- [YOURLS using Helm for Kubernetes](https://artifacthub.io/packages/helm/yourls/yourls)

## Plugins [⇪](#readme)

All known plugins - either from the community, or from the YOURLS team, marked with a ☑️

Currently we have **<!--plugin_count-->185<!--/plugin_count-->** plugins listed.
<!-- DO NOT UPDATE THIS COUNT MANUALLY -->

Willing to get your plugins featured here? Please [contribute](CONTRIBUTING.md)!

Jump to [0-9](#0-9-) | [A](#a-) | [B](#b-) | [C](#c-) | [D](#d-) | [E](#e-) | [F](#f-) | [G](#g-) | [H](#h-) | [I](#i-) | [J](#j-) | [K](#k-) | [L](#l-) | [M](#m-) | [N](#n-) | [O](#o-) | [P](#p-) | [Q](#q-) | [R](#r-) | [S](#s-) | [T](#t-) | [U](#u-) | [V](#v-) | [W](#w-) | [X](#x-) | [Y](#y-) | [Z](#z-)

### 0-9 [⇡](#plugins-)

- [302-Instead](https://github.com/EpicPilgrim/302-instead) - Send a 302 (temporary) redirect instead of 301 (permanent), for sites where shortlinks may change.
- [302-Instead](https://github.com/timcrockford/302-instead) - A fork of previous plugin, with some more options.
- [404 If Not Found](https://github.com/YOURLS/404-if-not-found)☑️ - Give a 404 Not Found if the short URL is not found.

### A [⇡](#plugins-)

- [AAF Rapid Connect auth](https://github.com/clmcavaney/aaf-rapidconnect-auth-yourls) - AAF Rapid Connect authentication plugin for YOURLS.
- [Abuse Desk for YOURLS](http://blog.yourls.org/2011/04/yourls-abuse-anti-spam-plugins/) - A Google Safe Browsing implementation for YOURLS to avoid spam links.
- [Access Control Allow Origin](https://github.com/TEODE/yourls-access-control-allow-origin) - Prevents CORS issue with domain CNAMES and aliases for admin actions.
- [Additional Charsets](https://github.com/josheby/yourls-additional-charsets) - Define additional character sets for short URLs.
- [Admin Issue Diagnostic - A.I.D.](https://github.com/PopVeKind/admin_issue_diagnostic) - Collects YOURLS environmentals and formats a template to copy/paste into a YOURLS issue.
- [Admin NoReCAPTCHA](https://github.com/amindeed/YOURLS-Admin-NoReCAPTCHA) - Protect logins with Google's No CAPTCHA reCAPTCHA (Google's ReCAPTCHA v2.0).
- [Admin reCaptcha](https://github.com/armujahid/Admin-reCaptcha) - Spam protection for private YOURLS admin interface with reCaptcha.
- [Advanced Reserved URLs](https://github.com/josheby/yourls-advanced-reserved-urls) - Extends the reserved word functionality, blocking short URLs containing reserved words, even if mixed case or written in leetspeak.
- [Allow Aliases](https://github.com/adigitalife/yourls-allow-aliases) - Allow YOURLS to work with alias hostnames for the server.
- [Allow Forward Slashes in Short URLs](https://github.com/williambargent/YOURLS-Forward-Slash-In-Urls) - Just as the name says.
- [Always-302](https://github.com/tinjaw/Always-302) - A newer alternative to 302-Instead.
- [Amazon Affiliate](https://github.com/floschliep/YOURLS-Amazon-Affiliate) - Adds your Amazon Affiliate Tag to all Amazon URLs before redirection.
- [Amazon Affiliate With Notice](https://github.com/Trsmoothie/YOURLS-Amazon-Affiliate-With-Redirect-Notice) - Adds your Amazon Affiliate Tag to all Amazon URLs before redirection with a notice of Amazon Affiliate link usage.
- [Anonymise](https://github.com/wlabarron/yourls-anonymise) - Anonymise the log data that YOURLS captures.
- [Antispam](https://github.com/YOURLS/antispam)☑️ - Merciless antispam plugin using the 3 major domain blacklists.
- [YOURLS APC Cache](https://blog.yourls.org/2011/06/yourls-apc-cache-plugin/) - Add support for APC to reduce MySQL queries.
- [API Action](https://github.com/YOURLS/API-action)☑️ - Example plugin for YOURLS 1.6+ to show how to implement custom API actions.
- [API Delete](https://github.com/claytondaley/yourls-api-delete) - Add a "delete" action to the API.
- [API Edit URL](https://github.com/timcrockford/yourls-api-edit-url) - Add an "update" action to the API to edit a URL, and a "geturl" action to get the long URL of a short URL.
- [Append Query String](https://github.com/drockney/append-qs) - Appends the query string to a long URL.
- [Auth Manager](https://github.com/nicwaller/yourls-authmgr-plugin) - Assign users to roles like "Editor" and "Contributor" to limit the changes they are permitted to make (edit URLs, manage plugins...).
- [Auth Manager Plus](https://github.com/joshp23/YOURLS-AuthMgrPlus) - Seperates user data & manages authorization with role-based access controls (RBAC).
- [Auto Login](https://gist.github.com/ozh/3fa3382eb83d26449daab4b70cd3b299)☑️ - Automatically populate login/password with test/test (for test installs)
### B [⇡](#plugins-)

- [Blacklist Domains](https://github.com/apelly/YourlsBlacklistDomains) - A simple plugin to blacklist domains from shortening URLs.
- [Blacklist IPs](https://github.com/LudoBoggio/YourlsBlacklistIPs) - A simple plugin to blacklist IPs from shortening URLs.
- [Bulk Import and Shorten](https://github.com/vaughany/yourls-bulk-import-and-shorten) - Import links from a CSV file.
- [Bulk URL Shortening](https://github.com/tdakanalis/bulk_api_bulkshortener) - Shortening of multiple URLs with one API request.

### C [⇡](#plugins-)

- [cAuth](https://github.com/joshp23/YOURLS-cAuth) - Client side SSL certificate authentication for admin pages.
- [Cache Stat Pages](https://github.com/YOURLS/cache-stats-pages)☑️ - Serve stat pages (`http://sho.rt/blah+`) from cache.
- [CAS Plugin](https://github.com/nicwaller/yourls-cas-plugin) - Enable authentication through a CAS server.
- [Case Insensitive](https://github.com/seandrickson/YOURLS-Case-Insensitive/) - Makes all keywords case insensitive (creates and calls all keywords lowercase).
- [Case Insensitive](https://github.com/adigitalife/yourls-case-insensitive) - Make YOURLS case insensitive: if you create `http://sho.rt/MyLink`, then variations like `mylink` or `MYLINK` will redirect to the same URL.
- [Change Error Messages](https://github.com/adigitalife/yourls-change-error-messages) - Changes the error message when a keyword or URL already exists and displays the long URL.
- [YOURLS GWall Change Logo](https://github.com/gioxx/YOURLS-GWallChangeLogo) - Allows you to change the image of the YOURLS logo and its alt and title tags.
- [Change Password](https://github.com/ozh/yourls-change-password)☑️ - Change your password from within YOURLS instead of editing the config file.
- [Change Password](https://github.com/vvanasten/YOURLS-Change-Password) - Allow users to change their password via the administration interface.
- [Change Title](https://happier.allowed.org/change-title) - Change the html `<title>` tag of your admin interface.
- [Check URL](https://github.com/adigitalife/yourls-check-url) - Check if a long URL is reachable before creating a short URL.
- [Compliance](https://github.com/joshp23/YOURLS-Compliance) - Anti-abuse plugin, designed to address link complaints from 3rd parties.
- [Conditional Toolbar](https://blog.yourls.org/2011/03/yourls-plugin-example-conditional-toolbar/)☑️ - A plugin to conditionally enable the toolbar: `http://sho.rt/blah` for normal redirect, `http://sho.rt/tb/blah` for a toolbar.
- [Conditional Advertisements](https://github.com/HeroCC/yourls-conditional-urlads) - A plugin to conditionally send links through various link monetizing services: `http://your.site/short` is normal, `http://your.site/a/short` redirects through AdFly.
- [Custom Header & Footer](https://github.com/mediageni/yourls-custom-header-footer) - A plugin administration page to add custom header and footer style and content.
- [Custom Javascript](https://github.com/mediageni/yourls-custom-javascript) - Add custom javascript to admin pages.
- [Custom Number of Displayed Links](https://github.com/YOURLS/YOURLS/issues/2339#issuecomment-352127623)☑️ - Change the default number of links per page, if 15 isn't your taste.
- [Custom Protocol](https://github.com/YOURLS/custom-protocol)☑️ - If the user is known, this plugin adds custom protocol (eg `blah://`) to authorized protocols, otherwise restricts to `http|s`.

### D [⇡](#plugins-)

- [Disable JSONP](https://github.com/seandrickson/YOURLS-Disable-JSONP) - Disables JSONP access for the YOURLS API.
- [DNSBL](https://github.com/Diftraku/yourls_dnsbl/) - Uses various DNSBLs to check the submitter's IP and prevent shortening URLs if any malicious activity has been detected.
- [Domain Limit](https://github.com/nicwaller/yourls-domainlimit-plugin) - Limit the domains that users can create shortlinks to.
- [Domain Limiter](https://bitbucket.org/quantumwebco/domain-limiter-yourls-plugin) - Fork of Nic Waller's plugin with the addition of an admin panel to edit the white list from the admin area.
- [Do TLS](https://github.com/joshp23/YOURLS-doTLS) - Always use SSL/TLS for a destination url if available.
- [Don't Log Bots](https://github.com/YOURLS/dont-log-bots)☑️ - Ignore bot hits in your stats (both click count as seen in the main admin page and in detailed stats).
- [Don't Log Crawlers](https://github.com/luixxiul/dont-log-crawlers/) - A fork of the `Don't Log Bots`, with more bots filtered out.
- [Don't Log Health Checker](https://github.com/guessi/yourls-dont-log-health-checker) - A fork of `Don't Log Bots`, with more bots filtered out.
- [Don't Track Admin Clicks](https://github.com/dgw/yourls-dont-track-admins) - Don't count clicks on short URL if user is logged in.
- [Download Plugin](https://github.com/krissss/yourls-download-plugin) - Download and install YOURLS plugins from the admin panel.

### E [⇡](#plugins-)

- [Edition Logger](https://github.com/esuarezsantana/yourls-edition-logger) - Logs to a file every url insertion, deletion, or modification, to provide traceability of users' actions allowing an open edition policy.
- [Email Notify](https://github.com/s22-tech/Yourls-Email-Notify) - Sends you an email with identifying information whenever someone clicks the link they were sent.
- [Emojis](https://github.com/telepathics/yourls-emojis) - Create an emoji-only short link, like `http://sho.rt/✨` or `http://sho.rt/😎🆒🔗`
- [Enhanced Auth Cookies](https://github.com/ozh/yourls-enhanced-cookies)☑️ - Enhances the cookie based authentication, making each auth cookie name unique and time based.
- [Every Click Counts](https://github.com/BstName/every-click-counts) - Click count include multiple clicks for the same client (ie there will be no browser caching of the redirection).
- [Expiry](https://github.com/joshp23/YOURLS-Expiry) -  Defines optional conditions under which links will expire, able to set time and click limited links globally or per individual links.

### F [⇡](#plugins-)

- [Fallback URL](https://github.com/ozh/yourls-fallback-url/) - Redirect to a custom URL when the short URL does not exist.
- [Favicon](https://github.com/YOURLS/yourls-favicon/)☑️ - Properly displayed favicon in all cases (home screen on iOS, Android, Chrome, Safari...).
- [Filter Code](https://github.com/ShredCode/YOURLS-filter-code) - Allow to select 3XX Status Code to return per keyword.
- [Fix long URLs](https://github.com/adigitalife/yourls-fix-long-url) - Fix long URLs that contain %20 and other similar encodings.
- [Force Lowercase](https://github.com/YOURLS/force-lowercase)☑️ - Force lowercase so `http://sho.rt/ABC` → `http://sho.rt/abc`.
- [Fuzzy Keyword Suggestions](https://github.com/philhagen/ltc-fuzzy-keyword-suggestions) - Handles typos and other "near-misses" for any shortened link (eg if you have `sho.rt/dh1ik` but someone types `sho.rt/dhlik`, the 404 page will show suggestions for similar short URLs).

### G [⇡](#plugins-)

- [GA MP](https://github.com/powerthazan/YOURLS-GA-MP-Tracking) - Track YOURLS link clicks with Google Analytics Measurement protocol in Real Time.
- [Git Version](https://github.com/chtaube/YOURLS-plugin-gitversion) - Add version information from the git repository into the footer of the admin page.
- [Geo API](https://github.com/ssecurelabs/yourls-Geo-API-plugin) - Plugin to look up country code from another 3rd party API (geoiplookup.net).
- [GeoShortURL](https://github.com/tobozo/YOURLS-GeoShortURL) - Plugin to add per-country support to existing short URLs (use it with [302-Instead](https://github.com/timcrockford/302-instead)).
- [Google Analytics Link Tagging](https://katz.co/2300/) - Add GA tags (utm_source and others) to your shortened links.
- [Google Auth](https://github.com/8thwall/google-auth-yourls) - Enables Google Authentication for YOURLS.
- [Google Safe Browsing](https://github.com/YOURLS/google-safe-browsing)☑️ - Check every new URL against Google's Safe Browsing Lookup service.
- [GTM for YOURLS](https://github.com/dorks-delivered/GTM-for-YOURLS) - Google Tag Manager for every single click.

### H [⇡](#plugins-)

- [hexdec](https://github.com/plttn/yourls-hexdec) - Changes the sequential keywords from base36 to base16 (ie `[0-9a-f]`).
- [Hide Referrer](https://github.com/Sire/yourls-hide-referrer) - Hide referrer on all or some short links.
- [Hide Version String](https://github.com/YOURLS/YOURLS/issues/1878#issuecomment-88450475) - Hide the version string in the footer.
- [HTTP:BL](https://github.com/joshp23/YOURLS-httpBL) - Prevent spam using the black list from Project Honeypot.
- [HTTP Proxy](https://github.com/adigitalife/yourls-http-proxy) - Get remote content using an HTTP proxy, for instance when YOURLS is running behind a firewall (e.g. corporate intranet).
- [HTTP status per link](https://github.com/digipolisgent/yourls_plugin_http-status-per-link) - Select `3XX` Status Code to return per keyword.

### I [⇡](#plugins-)

- [Identi.ca for YOURLS](https://blog.yourls.org/2011/04/yourls-identi-ca-and-tumblr-plugins/) - Share YOURLS links via identi.ca.
- [YOURLS IDN](https://github.com/YOURLS/YOURLS-IDN)☑️ - Add IDN support to YOURLS.
- [Image Placeholder](https://github.com/LeoColomb/yourls-image-placeholder)☑️ -  Simple image placeholder service for YOURLS.
- [YOURLS Import Export](https://github.com/GautamGupta/YOURLS-Import-Export) - A plugin to import and export YOURLS URL.
- [Integrated QRCodes](https://github.com/joshp23/YOURLS-IQRCodes) - Integrated QRCodes is an updated fork of Inline QRCode, but more compact, configurable, and just as efficient with more features.
- [Insert Fake Links](https://gist.github.com/ozh/6455d192ac443c2a12379cc94f607b43)☑️ - Insert fake links (for test installs)
- [iOS URL](https://github.com/suculent/yourls-ios-url-schemes-plugin) - Adds support for URLs starting with `itms-apps://` and `itms-services://`.
- [iTunes-Affiliate](https://github.com/floschliep/YOURLS-iTunes-Affiliate) - Adds your iTunes Affiliate-Token to all iTunes URLs before redirection.

### J [⇡](#plugins-)

- [Jappix](https://github.com/jonrandoem/yourls-jappix) - Adds a JappixMini chat on your YOURLS admin pages.
- [JSON Response](https://github.com/tessus/yourls-json-response) - Add `.json` (or a custom string/character) to the short URL to get info about it as a JSON response.

### K [⇡](#plugins-)

- [Keep Query String](https://github.com/rinogo/yourls-keep-query-string) - Adds the short URL's query string (if any) to the long URL.
- [Keywords, Charset & Length](https://github.com/peterberbec/yourls-keyword_charset_length) - Custom charset, custom link length and random short urls, all in one plugin, with an admin panel.
- [Keyword not found](https://github.com/8thwall/keyword-not-found-set-field-yourls) - If keyword isn't found in the database, redirect to admin page and pre-populate the short URL field.
- [Keyword Prefix](https://github.com/jangrewe/yourls-keyword-prefix) - Adds a defined prefix to your short URLs.

### L [⇡](#plugins-)

- [LDAP](https://github.com/k3a/yourls-ldap-plugin) - Enables use of LDAP for user authentication.
- [Link Anonymizer](https://github.com/katzwebservices/YOURLS-Link-Anonymizer) - Generate a link that will take you to an anonymizer service.
- [Link List](https://gitlab.com/ruthtillman/yourls-linklist) - List recent links added, in the admin interface or on a public page.
- [Limit keyword length](https://github.com/adigitalife/yourls-limit-keyword-length) - This plugin limits the number of characters allowed for the custom keyword.
- [Limited Links](https://github.com/LeoColomb/yourls-limited-links)☑️ -limit the number of redirections of a specific link.
- [log-login](https://github.com/SweBarre/log-login) - Logs login atempts to YOURLS. To be used with fail2ban.
- [Login Timeout](https://github.com/reanimus/yourls-login-timeout) - Adds a timeout after a certain number of failed logins to mitigate brute force logins.
- [Lookup keywords by long URL substring](https://github.com/bryzgaloff/yourls-api-lookup-keywords-by-url-substr) - Add a "lookup-url-substr" action to YOURLS API which searches keywords by long URL substring (implements `url LIKE %substr%` SQL operation).
- [lowercase username](https://github.com/Virinum/yourls-lowercase-username) - Makes the username lowercase when logging in.

### M [⇡](#plugins-)

- [Mailto](https://github.com/peterberbec/yourls-mailto) - Adds a "mailto:" sharing option, next to Twitter and Facebook.
- [Mailto Bookmarklet](https://github.com/peterberbec/yourls-mailto-bookmarklet) - Adds a bookmarklet to share links by mail.
- [Mass Remove Link](https://github.com/YOURLS/YOURLS/wiki/Plugin-=-Mass-Remove-Link) ⭐ - Remove several links at once. Select by date, date range, IP or URL matching.
- [Mass Update](https://github.com/Binarypark/yourls-api-mass-update) - Adds an API action to mass update links from `old_domain` to `new_domain`.
- [Memcached](https://github.com/alexalouit/Yourls-Memcached) - Memcached plugin for YOURLS.
- [Meta Redirect](https://github.com/pureexe/Yourls-meta-redirect) - Redirect using HTML meta tag when you prepend the short URL with an underscore (eg `http://sho.rt/_bleh`).
- [Mobile Detect](https://github.com/guessi/yourls-mobile-detect) - Add ability to redirect by user device OS.

### N [⇡](#plugins-)

- [No Traking Admins](https://github.com/joshp23/YOURLS-No-Tracking-Admins) - No loggin clicks for authenticated users (compatible with OIDC).
- [No Version Check](https://github.com/YOURLS/YOURLS/issues/2851)☑️ - Stop YOURLS from checking if a new release is available.

### O [⇡](#plugins-)

- [OAuth Sign In](https://github.com/LouisSung/YOURLS-OAuth_Sign_In) - Enable OAuth sign in support (using GitLab as an example).
- [OIDC](https://github.com/joshp23/YOURLS-OIDC) - OpenID Connect authentication against a generic OpenID Connect server.
- [Open Graph Meta Scraper](https://github.com/LK608/OG-Scraper) - Get Open Graph (OG) information for your shortened links.

### P [⇡](#plugins-)

- [Password Protection](https://github.com/MatthewC/yourls-password-protection) - Password protect any Short URL you want so that users are prompted for a password before redirection.
- [Phishtank](https://blog.yourls.org/2011/04/yourls-abuse-anti-spam-plugins/) - Prevent spam links using Phishtank's API.
- [Phishtank 2.0](https://github.com/joshp23/YOURLS-Phishtank-2.0) - Functional rewrite of the old Phishtank plugin with more features.
- [Piwik-YOURLS](https://github.com/interfasys/piwik-yourls) - Piwik and a few other features.
- [Popular Clicks](https://github.com/miconda/yourls/tree/master/plugins/popular-clicks) - Display the top of the most clicked links during past days.
- [Popular Clicks Extended](https://github.com/vaughany/yourls-popular-clicks-extended) - Shows which short links get clicked the most during a specific time frame.
- [Popular Links](https://github.com/laaabaseball/Yourls-Popular-Links) - Adds an admin page that displays your shortener's most popular links.
- [Preview URL](https://github.com/YOURLS/YOURLS/wiki/Plugin-=-Preview-URL)☑️ - Add the character '~' to a short URL to display a preview screen before redirection.
- [Preview URL with QR Code](https://github.com/dennydai/yourls-preview-url-with-qrcode) - Add the character '~' to a short URL to display a preview screen & QR code before redirection.
- [Preview URL with QR Code And Thumbnail](https://github.com/prog-it/yourls-preview-url-with-qrcode-thumbnail) - Add the character '~' to a short URL to display a QR code and Thumbnail image before redirection.
- [Public "Prefix n' Shorten"](https://github.com/YOURLS/YOURLS/wiki/Plugin-=-Public-Prefix-And-Shorten)☑️ - Redirect `http://sho.rt/http://someurl.com/` to a public interface instead of the admin area.
- [YOURLS Pseudonymize](https://github.com/ubicoo/yourls-pseudonymize) - This plugin "pseudonymizes" the IP addresses so that it is in line with the German privacy laws (the last 2 segments/bytes of a visitor's IP address are removed).
- [PUNS](https://github.com/joshp23/YOURLS-PUNS) - A Plugin Update Notification System: provides a report-generating page and an API with optional email notifications.

### Q [⇡](#plugins-)

- [QRCode](https://github.com/YOURLS/YOURLS/wiki/Plugin-=-QRCode-ShortURL)☑️ - Add ".qr" to short URLs to display the shorturl's QR code.
- [QRCode](http://techlister.com/plugins-2/qrcode-plugin-for-yourls/354/) - Creates and displays QR Codes within YOURLS.
- [QR Google Charts](http://aiaraldea.github.io/qr-google-charts/) - Another QR Code plugin, using Google Charts API.
- [QRCode](https://github.com/seandrickson/YOURLS-QRCode-Plugin) - Another QR Code plugin. Get the QR code by simply clicking on a button in the Admin area (or by adding ".qr" to the end of the keyword).
- [QueryString Forward](https://github.com/llonchj/yourls_plugins) - Forward the query string on short link to long URL (eg `http://sho.rt/kk?a=1` to `http://long.url/somepage/?a=1`).
- [Query String Keeper](https://github.com/jessemaps/yourls-query-string-keeper) - Pass the query string from the shortlink to the long URL (eg `http://sho.rt/kk?hey` forwards to `http://long.url/bleh/?hey`).

### R [⇡](#plugins-)

- [reCaptcha](https://github.com/spbriggs/recaptcha-plugin) - YOURLS plugin implementing reCaptcha for unauthenticated users in your public interface.
- [Redirect Index](https://github.com/tomslominski/yourls-redirect-index) - Redirect the user to another site if they go to the base directory of your YOURLS installation.
- [Referral Link Checkpoint](https://github.com/telepathics/yourls-ref-checkpoint) - Add a landing page to let visitors know when it is a referral link.
- [Regenerate URL](https://github.com/TheLeonKing/yourls-api-regenerate-url) - Regenerate a new keyword for a URL that has already been shortened.
- [Remove The Share Function](https://github.com/seandrickson/YOURLS-Remove-the-Share-Function) - Remove the Share button and box that toggles the sharing options on the Admin page.
- [Remove YouTube Play Indicator](https://github.com/UltraNurd/youtube-play-indicator) - Removes the triangle from the title of Youtube shortened URL.
- [Reset URLs](https://gist.github.com/ozh/a0090f46569b50835520d95f9481d9fd)☑️ - Deletes all URLs. For your test install needs.
- [Reverse Proxy](https://github.com/Diftraku/yourls_reverseproxy) - Fixes the user IPs to point to the actual user instead of your cloud provider’s infrastructure IPs (Cloudflare, Heroku...).
- [rscrub](https://github.com/joshp23/YOURLS-rscrub) - An "HTTP referrer scrubbing swiss army knife for YOURLS" (evolution of the Hide Referrer plugin).

### S [⇡](#plugins-)

- [SAML Authentication](https://github.com/wlabarron/yourls-saml) - Sign in via SAML-based single sign-on.
- [Save By Keyword](https://github.com/vitorccs/yourls-api-save-by-keyword) - API action to update the long URL of an existing keyword, or creates a new short URL.
- [Semantic Scuttle](https://github.com/jonrandoem/yourls-semanticscuttle) - Allows the sharing of the URL to a Semantic Scuttle installation.
- [Separate Users](https://github.com/ianbarber/Yourls-Separate-Users) - Adds a username to each created URL, and filters the admin interface.
- [Shaarli](https://github.com/miwasp/yourls-shaarli) - Allows the sharing of the URL to a Shaarli installation.
- [Share LinkedIn](https://github.com/popnt/yourls-linkedin-share) - Adds LinkedIn to the Quick Share Box.
- [Share with Tumblr](https://github.com/YOURLS/YOURLS/wiki/Plugin-=-Share-Tumblr)☑️ - In the Quick Share box, add a one-click share to Tumblr link.
- [Shibboleth](https://github.com/fuero/yourls-shibboleth) - Enable authentication with Shibboleth.
- [ShortShort](https://github.com/abaumg/yourls-shortshort) - Checks if a URL is already shortened (e.g. t.co, bit.ly, youtu.be) to avoid nested shortened links.
- [Show Git Branch](https://github.com/ozh/show-git-branch)☑️ - Using YOURLS on a dev box under Git? Show the current branch in page footer.
- [SimpleDB Clickqueue](https://github.com/ianbarber/Yourls-SimpleDB-Clickqueue) - Queue clicks to Amazon SimpleDB before processing. This allows using a regular MySQL store even in the face of a high frequency of writes, without concern of connection limit overflow. Clicks are inserted later into the database via an import job.
- [Skimlinks](https://mattytemple.com/plugin/yourls-plugin-skimlinks/) - Push all links through Skimlinks to automatically embed affiliate codes.
- [Skip Click Count](https://github.com/vipwangtian/yourls-skip-click-count) - Don't count clicks on short URLs.
- [SMTP Contact](https://github.com/joshp23/YOURLS-SMTP-contact) - Provides a public contact page using PHPMailer for outbound mail delivery.
- [Snapshot](https://github.com/joshp23/YOURLS-Snapshot) - Visual preview plugin with image caching powered by PhantomJS.
- [YOURLS SQLite](https://github.com/ozh/yourls-sqlite)☑️ - SQLite driver for YOURLS. It is now considered outdated.
- [YOURLS SQLite](https://github.com/Flameborn/yourls-sqlite) - A fork of the original SQLite driver for YOURLS, actively maintained.
- [Static Titles](https://github.com/softius/yourls-static-titles) - Provide two options to avoid the network traffic when retrieving URL titles.
- [SSL for SSL](https://github.com/tipichris/ssl4ssl) - Generates SSL short links if the original link was SSL.
- [Swap Short URL](https://github.com/gerbz/Yourls-Swap-Short-Url) - A plugin to have `http://sho.rt/blah` while having YOURLS installed in `http://sho.rt/yourls/`

### T [⇡](#plugins-)

- [Telegram Quickshare](https://github.com/ColinShark/YOURLS_tg-quickshare) - Quickly share a shortened URL via Telegram Messenger.
- [Title Refetch](https://github.com/joshp23/YOURLS-title-refetch) - Refetch page titles.
- [Timezones](https://github.com/YOURLS/timezones)☑️ - Tell YOURLS your time zone and how you'd like times and dates displayed.
- [Thumbnail URL image](https://github.com/stevecohenfr/yourls-thumbnail-url) - Get the Thumbnail URL image (long URL) by adding `.i` to the end of the keyword.
- [Time-Period Clicks](https://github.com/rinogo/yourls-time-period-clicks) - A simple API plugin for reporting URL clicks in a specific time period (e.g. the last week, January 1 - February 1, etc).
- [Time Limit Link](https://github.com/chesterrush/yourls-Time-Limit-Link) - Set a time limit for links.
- [Track Custom Keyword](https://github.com/timcrockford/track-custom-keywords) - Add a new field to YOURLS designed to track if a keyword was randomly assigned or manually specified.
- [Typer, a yourls prank plugin](https://github.com/koma5/typer) - Add an underscore * to your shortlink and the user will be shown a page where they have to type the shortlink themselves.

### U [⇡](#plugins-)

- [Upload and Shorten](https://github.com/fredl99/YOURLS-Upload-and-Shorten) - Upload and share files with YOURLS.
- [U-SRV](https://github.com/joshp23/YOURLS-U-SRV) - Provides secure links to files while obfuscating filesystem paths, allowing easy, secure access to files between plugins or from 3rd party scripts. Manual uploading of files is supported.
-  [Update 30X](https://github.com/joshp23/YOURLS-Update-30X) - An API plugin to test single, domain based, or all available links and update the URL in YOURLS if redirection occures at the destination.
- [URL Health Check](https://github.com/joshp23/YOURLS-URL-Health-Check) - Checks submitted URLs for validity, reachability, and redirection. In the case of redirection, the final destination URL will be stored avoiding nested redirects.

### W [⇡](#plugins-)

- [wallabag](https://github.com/jonrandoem/yourls-wallabag) - Allows the sharing of the URL to a Wallabag installation (previously named Poche).
- [Whatsapp quickshare](https://github.com/TheChicken14/Whatsapp-quickshare) - Allows you to share your short URL via whatsapp.
- [Word Based Short URLs](https://github.com/ozh/yourls-word-based-short-urls)☑️ - Generate short URLs with adjectives and nouns, like `http://sho.rt/FluffyArrogantUnicorn`.

### X [⇡](#plugins-)



### Y [⇡](#plugins-)

- [YAPCache](https://github.com/tipichris/YAPCache) - YAPCache is an APC based cache designed to reduce the database load of YOURLS and increase performance.
- [YOURS-TN](https://github.com/sgiovagnoli/YOURLS-TN) - Display thumbnails on YOURLS admin page and stats page, using thumbnail.ws.
- [YouTube Title Fix](https://github.com/joshp23/YOURLS-YouTube-title-fix) - Fetch YouTube page titles via Google API.

### Z [⇡](#plugins-)



## Themes [⇪](#readme)

This will be the next big thing when YOURLS fully support theming

- [∞²](https://github.com/tomslominski/infinity-squared) - Infinity Squared, a beautiful public page theme for YOURLS.
- [Air 66](https://github.com/air66design/air66-yourls-admin-theme) - A responsive admin theme for YOURLS.
- [Sleeky](https://github.com/Flynntes/Sleeky) - A sleek and simple frontend & backend theme for YOURLS with light and dark modes.



## Translations [⇪](#readme)

YOURLS supports localization: this means if a language file for YOURLS in available in your language, YOURLS will speak your language!

- Brazilian: [here](https://github.com/didi3d/YOURLS-pt_BR) and [here](https://github.com/henriquecrang/YOURLS-pt_BR)  (`pt_BR`)
- [Bulgarian ](https://github.com/VoodooServ/YOURLS-bg_BG) (`bg_BG`)
- [Czech](https://github.com/KubaCZ721/YOURLS-cs_CZ) (`cs_CZ`)
- [Danish](https://github.com/jensz12/YOURLSDK) (`da_DK`)
- [Dutch](https://github.com/Beun/YOURLS-nl_NL) (`nl_NL`)
- [Farsi](https://github.com/saahmadnejad/YOURLS-fa_FA) (`fa_FA`)
- [Finnish](https://github.com/re2man/YOURLS-fi_FI) (`fi_FI`)
- [French](https://github.com/ozh/YOURLS-fr_FR) (`fr_FR`)
- [German](https://github.com/DerSev/YOURLS-de_DE) (`de_DE`)
- [Hindi](https://github.com/itsKV/YOURLS-Hindi-translation) (`hi-IN`)
- [Indonesian](https://github.com/tigefa4u/YOURLS-id_ID-Translations) (`id_ID`)
- [Italian](https://github.com/ggardin/YOURLS-it_IT) (`it_IT`)
- [Japanese](https://github.com/havill/YOURLS-ja_JP) (`ja_JP`)
- [Korean](https://github.com/at4am/YOURLS-ko_KR) (`ko_KR`)
- [Norwegian (bokmål)](https://github.com/geirawsm/YOURLS-nb_NO) (`nb_NO`)
- [Polish](https://github.com/tomslominski/YOURLS-pl_PL) (`pl_PL`)
- [Portuguese](https://github.com/oscarmarcelo/YOURLS-pt_PT) (`pt_PT`)
- [Russian](https://github.com/nsauk/YOURLS-ru_RU) (`ru_RU`)
- [Simplified Chinese](https://github.com/ZvonimirSun/YOURLS-zh_CN) (`zh_CN`)
- [Slovak](https://github.com/filyph/YOURLS-sk_SK) (`sk_SK`)
- [Spanish](https://github.com/kralizeck/YOURLS-es_ES) (`es_ES`)
- [Telugu](https://github.com/kalyan4786/YOURLS_Telugu_Translation) (`te_IN`)
- [Turkish](https://github.com/mugurcagdas/YOURLS_TR) (`tr_TR`)
- [Traditional Chinese](https://github.com/alexclassroom/YOURLS-zh_TW) (`zh_TW`)
- [Viet Nam](https://github.com/tmtung144/YOURLS) (`vi_VN`)


## Integrations [⇪](#readme)

Make YOURLS work with other platforms, programming languages or tools.

### 3rd party Integrations and Frameworks  [⇡](#integrations-)

- Bash
  - [YOURLS BASH](https://github.com/ozh/yourls-bash) - a simple BASH script to shorten URLs with YOURLS
- [CakePHP](https://github.com/adrianoluis/CakePHP-YOURLS-Plugin) - Plugin to integrate YOURLS.
- [Drupal](https://www.drupal.org/project/shorten) - YOURLS for Drupal.
- [FreeBSD Freshport](https://www.freshports.org/www/yourls/) - a FreeBSD package.
- [Gnome Desktop](https://github.com/joshp23/gnome-shell-extension-yourls) - Gnome Shell extension to shorten links in the clipboard.
- Laravel
  - [Laravel YOURLS Plugin](https://github.com/phpsa/laravel-yourls-plugin)
  - [Laraval YOURLS](https://github.com/orumad/laravel-yourls)
- NodeJS
  - [JavaScript bindings for the YOURLS API](https://github.com/neocotic/yourls-api) - JavaScript bindings to leverage JSONP support.
  - [YOURLS API for nodejs](https://www.npmjs.com/package/yourls)
- Perl
  - [WWW::Shorten::Yourls](https://github.com/p5-shorten/WWW-Shorten-Yourls) - A Perl module to shorten URLs using YOURLS.
  - [AmazonAffiliatesToYourls](https://github.com/acaranta/AmazonAffiliatesToYourls) - Amazon affiliate management.
- Python
  - [pyourls3](https://pypi.org/project/pyourls3/) - A Python client for YOURLS, built for Python 3.
  - [python-yourls](https://github.com/tflink/python-yourls/) - Alternative Python 2 client for YOURLS.
  - [yourls-python](https://github.com/razerm/yourls-python) - `pip install yourls` for Python 2 or 3
- [Ruby](https://github.com/threestage/yourls) - A Ruby wrapper for the YOURLS API.
- [status.net](https://github.com/rthees/yourls-status-net) - Plugin for status.net to use YOURLS.
- Telegram
  - [Telegram bot](https://simon-eller.at/en/projects/lets-short) - A [Telegram bot](https://t.me/LetsShortBot) to shorten links.
  - [YOURLS Bot](https://gitlab.com/HirschHeissIch/yourls-bot) - Open source code base for hosting your own Telegram bot to shorten links via your own YOURLS instance. Includes access control by default, so suitable for non-public YOURLS instances.
- [VB .Net](https://www.nugardt.com/open-source/yourls-api/) - A VB .Net 4.0 wrapper for the YOURLS API.
- WordPress
  - [YOURLS Link Creator](https://wordpress.org/plugins/yourls-link-creator/)
  - [YOURLS Widget](https://gist.github.com/joshp23/3f990e6ec36e24ba53985968bbfa89f1) - Fetch and display YOURLS links and a QR code in a widget.
  - There are numerous [WordPress plugins](https://wordpress.org/plugins/search/yourls/) with YOURLS support.


### Applications [⇡](#integrations-)

- Android
  - [aYourls](https://gitlab.com/matecode/ayourls/-/tree/develop) - A dedicated app for YOURLS supporting server-side deletion (needs [API Delete](https://github.com/claytondaley/yourls-api-delete)).
  - [URL Shortener](https://play.google.com/store/apps/details?id=de.keineantwort.android.urlshortener) - Supports various shortener, including YOURLS.
  - [iC-YOURLS](https://play.google.com/store/apps/details?id=net.inscomers.yourls) - A simple YOURLS app for Android, supports receiving links from other apps.
  - [AutoAffiliate](https://play.google.com/store/apps/details?id=com.autoaffiliate) - Automatically convert someone's affiliate link to your affiliate link.
- iOS
  - [ShortTail](https://www.adamdehaven.com/blog/shorttail-for-yourls-an-elegant-yourls-client-for-iphone/) - An elegant YOURLS client for iPhone.
  - [ShortFox2](https://apps.apple.com/us/app/shortfox2/id1465812791?ls=1&t=8)
  - [Short Menu](https://shortmenu.com/ios/) - YOURLS support requires a one-time in-app purchase of about $2 USD (See also: [Setup instructions](https://shortmenu.com/support/custom-services/yourls/)).
- Chrome
  - [YOURLS](https://chrome.google.com/webstore/detail/yourls/nddaaiojgkoldnhnmkoldmkeocbooken)
- Firefox
  - [YOURLS shortener](https://addons.mozilla.org/en-US/firefox/addon/yourls-shortener/)
- Mac
  - [Short Menu](https://shortmenu.com/mac/) - Available for $6 from the App Store or directly from the developer (See also: [Setup instructions](https://shortmenu.com/support/custom-services/yourls/)).
- Windows
  - [YOURLS on Windows](https://appsonwindows.com/apk/127308/) - Run YOURLS as a Windows program.


## Guides & Tutorials [⇪](#readme)

### Installation guides [⇡](#guides--tutorials-)

- [Installing YOURLS on a Plesk-Hosted Domain](https://www.danhendricks.com/2018/10/installing-yourls-on-plesk-shared-hosting-domain/) 
- [How to Install YOURLS using Softaculous](https://www.websitehostingrating.com/how-to-install-yourls-using-softaculous/)
- [How to Install YOURLS on a VPS or shared hosting](https://thishosting.rocks/how-to-shorten-your-links-with-your-own-domain/)
- [YOURLS on Azure](https://www.juharyhanen.com/technology/create-personal-url-shortener-in-5-simple-steps/)
- CentOS
  - [How to Install YOURLS on CentOS 7](https://www.vultr.com/docs/how-to-install-yourls-on-centos-7)
  - [How to install YOURLS on Centos 7](https://www.linuxcloudvps.com/blog/how-to-install-yourls-on-centos-7/)
  - [How to Install YOURLS on CentOS 8](https://www.howtoforge.com/how-to-install-yourls-on-centos-8/)
- [YOURLS on Cloudron](https://www.cloudron.io/store/org.yourls.cloudronapp.html)
- [YOURLS on Installatron](https://installatron.com/yourls)
- [YOURLS on Fedora](https://fedoraproject.org/wiki/Install_and_configure_YOURLS_for_AutoQA)
- Guides for Ubuntu :
  - [How to install YOURLS on Ubuntu 14.04](https://www.rosehosting.com/blog/how-to-install-yourls-on-ubuntu-14-04/)
  - [How to install YOURLS on Ubuntu 18.04](https://computingforgeeks.com/how-to-install-yourls-your-own-url-shortener-on-ubuntu-18-04-bionic-beaver-linux/)
  - [How to install YOURLS on Ubuntu 20.04](https://linuxbuz.com/linuxhowto/install-yourls-ubuntu-20-04)
  - [How to Install YOURLS on Ubuntu with Nginx and Let’s Encrypt](https://linuxstans.com/how-to-install-yourls/)
- [How to install YOURLS, reverse proxy and letsencrypt on Unraid](https://technicalramblings.com/blog/how-to-install-yourls-and-reverse-proxy-it-using-linuxserver-letsencrypt-on-unraid/)

### Installation guides in other languages [⇡](#guides--tutorials-)

- [宝塔面板搭建短链接服务 YOURLS](https://lza59.com/archives/yourls.html)
- [Cómo instalar YOURLS](https://www.websitehostingrating.com/es/how-to-install-yourls-using-softaculous/)
- [Installer YOURLS, un système d'URL raccourcies](https://www.justegeek.fr/tuto-installer-yourls-un-systeme-durl-raccourcies/)
- [Трекер Yourls ваш собственный сокращатель ссылок (URL)](https://wiki.dieg.info/yourls)

### Other tutorials [⇡](#guides--tutorials-)

- [YOURLS with Tweetie 2](http://www.eugenegordin.com/etc/how-to-use-your-custom-yourls-shortener-with-tweetie-2.html)
- [YOURLS with Tweetbot](https://2fatdads.com/2012/02/how-to-make-yourls-org-work-in-tweetbot/)


## Showcases [⇪](#readme)

### Sites running YOURLS with a unique design or concept  [⇡](#showcases-)

- https://oe.cd/ - Europe OECD's internal URL shortener with a neat interface and private features.
- https://kiwi.gg/ - A sexy shortener home page with stats and details.
- https://u.nu/ - Very neat public interface and their own command line tool.
- https://yourwish.es/ -  Easily share an Amazon wishlist.
- http://vbly.us - YOURLS early adopter, once taken down by Libya! ([story](https://mashable.com/2010/10/06/vbly-domain-seizure/?europe=true)).

### Celebrity endorsements (sort of) [⇡](#showcases-)

- Early review on [Lifehacker](https://lifehacker.com/make-your-own-url-shortening-service-5335216).
- http://mclrn.co/ by [McLaren Cars](https://www.mclaren.com/).
- https://smashed.by/ by [Smashing Magazine](https://www.smashingmagazine.com/).
- https://cuny.is/ by the [City University of New York](https://www.cuny.edu/).
- https://dhurl.org/ by [Dreamhost](https://yourls.org/dreamhost).

YOURLS has also been used by the NASA, Virgin and Epic Games. Sweet :)


## Contribute [⇪](#readme)

Contributions welcome! Read the [contribution guidelines](CONTRIBUTING.md) first.

## License [⇪](#readme)

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

