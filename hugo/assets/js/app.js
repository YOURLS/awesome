/**
 * Client-side filtering for the awesome list
 */
(function () {
    'use strict';

    var $ = function (id) { return document.getElementById(id); };
    var rows = Array.prototype.slice.call(document.querySelectorAll('.row'));
    var tabs = Array.prototype.slice.call(document.querySelectorAll('.tab'));
    var facets = Array.prototype.slice.call(document.querySelectorAll('.facet'));
    var notes = Array.prototype.slice.call(document.querySelectorAll('.note'));

    // Themes are laid out in columns instead of full-width rows.
    var GRID = ['themes'];

    // An empty section means "everything", which is the default view: a
    // search for "captcha" should reach plugins and guides at once.
    var state = { section: '', category: '', q: '', sort: '' };

    // Translations come sorted by English name from data/. The native order is
    // computed once; 'und' is the root collation, which groups scripts together.
    var byEnglish = rows.filter(function (row) { return row.dataset.section === 'translations'; });
    var collator = new Intl.Collator('und');
    var byNative = byEnglish.slice().sort(function (a, b) {
        return collator.compare(a.dataset.native || '', b.dataset.native || '');
    });
    var afterTranslations = byEnglish.length ? byEnglish[byEnglish.length - 1].nextElementSibling : null;
    var sortButtons = Array.prototype.slice.call(document.querySelectorAll('#sort button'));

    /**
     * Normalize a tag so it can be typed after a hash: "dark mode" -> "dark-mode".
     *
     * @param {string} value The raw tag
     * @return {string} The typeable form
     */
    function slug(value) {
        return value.toLowerCase().trim().replace(/\s+/g, '-');
    }

    /**
     * Escape a string for use inside a regular expression.
     *
     * @param {string} value Raw user input
     * @return {string} The escaped form
     */
    function escapeRe(value) {
        return value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }

    /**
     * Collect the text of an element, one space between each text node.
     *
     * textContent would glue adjacent elements together once the HTML is
     * minified ("<span>Translations</span><h3>Finnish" -> "TranslationsFinnish"),
     * and words would no longer start on a boundary.
     *
     * @param {Element} element The element to read
     * @return {string} Its text, with every node kept apart
     */
    function textOf(element) {
        var walker = document.createTreeWalker(element, NodeFilter.SHOW_TEXT);
        var parts = [];
        while (walker.nextNode()) { parts.push(walker.currentNode.nodeValue); }
        return parts.join(' ');
    }

    // Read once, never recomputed: the rendered text is the full-text index,
    // and the chips give the exact tag and account values behind # and @.
    rows.forEach(function (row) {
        row._hay = textOf(row).toLowerCase();
        row._tags = Array.prototype.map.call(
            row.querySelectorAll('.chip:not(.chip--cat):not(.chip--handle):not(.badge)'),
            function (chip) { return slug(chip.dataset.tag); }
        );
        row._handles = Array.prototype.map.call(
            row.querySelectorAll('.chip--handle'),
            function (chip) { return chip.dataset.tag.toLowerCase().trim(); }
        );
    });

    /**
     * Test one search word against one row
     *
     * "#tag" and "@account" are exact filters on the curated values; anything else matches the start of a word
     * in the rendered text, so "perl" finds Perl but not "properly".
     *
     * @param {Element} row The row to test
     * @param {string} word One whitespace-separated search word
     * @return {boolean} Whether the row matches
     */
    function wordMatches(row, word) {
        if (word.charAt(0) === '#') {
            return row._tags.indexOf(word.slice(1)) !== -1;
        }
        if (word.charAt(0) === '@') {
            return row._handles.indexOf(word) !== -1;
        }
        return new RegExp('\\b' + escapeRe(word)).test(row._hay);
    }

    /**
     * Order the translation rows by English or native name.
     *
     * They form one contiguous block in the list, so they are moved back in
     * front of whatever follows that block. Only they move, so that never changes.
     *
     * @param {Element[]} order The translation rows, in the wanted order
     */
    function sortTranslations(order) {
        order.forEach(function (row) { $('list').insertBefore(row, afterTranslations); });
    }

    /**
     * Show only the rows matching the current section, category and query.
     */
    function render() {
        var words = state.q ? state.q.split(/\s+/) : [];
        var hits = 0;
        var total = 0;
        var perSection = {};
        var perFacet = {};
        var matching = 0;

        rows.forEach(function (row) {
            var found = words.every(function (word) { return wordMatches(row, word); });
            if (found) {
                matching++;
                perSection[row.dataset.section] = (perSection[row.dataset.section] || 0) + 1;
                var key = row.dataset.section + '\u0000' + row.dataset.category;
                perFacet[key] = (perFacet[key] || 0) + 1;
            }

            var inSection = !state.section || row.dataset.section === state.section;
            if (inSection) { total++; }
            var ok = found
                && inSection
                && (!state.category || row.dataset.category === state.category);
            row.hidden = !ok;
            if (ok) { hits++; }
            // The category is redundant once the reader has filtered on it, and
            // the section name only helps while sections are mixed together.
            var label = row.querySelector('[data-cat-label]');
            if (label) { label.hidden = Boolean(state.category); }
            var section = row.querySelector('.section-tag');
            if (section) { section.hidden = Boolean(state.section); }
        });

        tabs.forEach(function (tab) {
            tab.setAttribute('aria-selected', String(tab.dataset.section === state.section));
            var count = tab.dataset.section ? (perSection[tab.dataset.section] || 0) : matching;
            tab.querySelector('i').textContent = count;
            tab.classList.toggle('is-empty', count === 0);
        });
        facets.forEach(function (facet) {
            facet.hidden = facet.dataset.section !== state.section;
            facet.setAttribute('aria-pressed', String(facet.dataset.category === state.category));
            var count = facet.dataset.goto
                ? (perSection[facet.dataset.goto] || 0)
                : (perFacet[facet.dataset.section + '\u0000' + facet.dataset.category] || 0);
            facet.querySelector('em').textContent = count;
            facet.classList.toggle('is-empty', count === 0);
        });

        var current = facets.filter(function (f) {
            return f.dataset.section === state.section && f.dataset.category === state.category;
        })[0];
        $('blurb').textContent = current ? current.dataset.blurb : '';
        $('blurb').hidden = !current;

        // Columns only make sense when a single description-less section is shown.
        $('list').classList.toggle('list--grid', GRID.indexOf(state.section) !== -1);
        $('list').dataset.showing = state.section;
        notes.forEach(function (note) { note.hidden = note.dataset.note !== state.section; });

        // Sorting by native name only applies while translations are shown alone.
        var native = state.section === 'translations' && state.sort === 'native';
        sortTranslations(native ? byNative : byEnglish);
        $('list').dataset.sort = native ? 'native' : '';
        $('sort').hidden = state.section !== 'translations';
        sortButtons.forEach(function (button) {
            button.setAttribute('aria-pressed', String(button.dataset.sort === (native ? 'native' : '')));
        });

        $('rail').hidden = !facets.some(function (f) { return f.dataset.section === state.section; });
        $('empty').hidden = hits > 0;

        var label = document.querySelector('.tab[data-section="' + state.section + '"]')
            .firstChild.textContent.trim().toLowerCase();
        var where = state.section ? ' in ' + label : '';
        $('count').innerHTML = state.q || state.category
            ? '<b>' + hits + '</b> of ' + total + where
            : '<b>' + rows.length + '</b> entries across ' + (tabs.length - 1) + ' sections';

        sync();
    }

    /**
     * Mirror the current filters in the address bar so any view is shareable.
     */
    function sync() {
        var params = new URLSearchParams();
        if (state.section) { params.set('in', state.section); }
        if (state.category) { params.set('category', state.category); }
        if (state.q) { params.set('q', state.q); }
        if (state.section === 'translations' && state.sort) { params.set('sort', state.sort); }
        var query = params.toString();
        history.replaceState(null, '', query ? '?' + query : location.pathname);
    }

    $('tabs').addEventListener('click', function (event) {
        var tab = event.target.closest('.tab');
        if (!tab) { return; }
        state.section = tab.dataset.section;
        state.category = '';
        render();
    });

    $('sort').addEventListener('click', function (event) {
        var button = event.target.closest('button');
        if (!button) { return; }
        state.sort = button.dataset.sort;
        render();
    });

    $('facets').addEventListener('click', function (event) {
        var facet = event.target.closest('.facet');
        if (!facet) { return; }
        // In the mixed view the rail switches section; inside a section it
        // toggles a category.
        if (facet.dataset.goto) {
            state.section = facet.dataset.goto;
            state.category = '';
        } else {
            state.category = facet.dataset.category === state.category ? '' : facet.dataset.category;
        }
        render();
    });

    /**
     * Put chip value in the search box ('#tag', '@name' or 'text')
     *
     * @param {Element} chip The chip that was clicked.
     */
    function searchChip(chip) {
        var value = chip.dataset.tag;
        if (!chip.classList.contains('badge') && !chip.classList.contains('chip--handle')) {
            value = '#' + slug(value);
        }
        $('q').value = value;
        state.q = value.toLowerCase();
    }

    $('list').addEventListener('click', function (event) {
        var chip = event.target.closest('.chip');
        if (!chip) { return; }

        // A category chip filters; a tag or account chip searches.
        if (chip.classList.contains('chip--cat')) {
            var row = chip.closest('.row');
            state.section = row.dataset.section;
            state.category = row.dataset.category;
        } else {
            searchChip(chip);
        }
        render();
        window.scrollTo({ top: 0 });
    });

    if ($('popular')) {
        $('popular').addEventListener('click', function (event) {
            var chip = event.target.closest('.chip');
            if (!chip) { return; }
            searchChip(chip);
            render();
        });
    }

    $('q').addEventListener('input', function (event) {
        state.q = event.target.value.trim().toLowerCase();
        render();
    });

    $('clear').addEventListener('click', function () {
        $('q').value = state.q = '';
        render();
        $('q').focus();
    });

    // Ctrl+K shortcut to search, like on yourls.org
    document.addEventListener('keydown', function (event) {
        if ((event.ctrlKey || event.metaKey) && event.key === 'k') {
            event.preventDefault();
            $('q').focus();
            $('q').select();
        }
    });

    /**
     * Switch the colour scheme and remember the choice.
     *
     * @param {string} name Either 'light' or 'dark'.
     */
    function setTheme(name) {
        // Which icon shows is decided in CSS from data-theme, so the correct one
        // is painted before this script runs.
        document.documentElement.dataset.theme = name;
        $('theme').setAttribute('aria-label',
            name === 'dark' ? 'Switch to light theme' : 'Switch to dark theme');
        try { localStorage.setItem('theme', name); } catch (error) { /* private mode */ }
    }

    setTheme(document.documentElement.dataset.theme);
    $('theme').addEventListener('click', function () {
        setTheme(document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark');
    });

    // --- narrow-screen navigation menu ---
    var burger = $('burger');
    var menu = $('nav-menu');

    /**
     * Open or close the navigation panel.
     *
     * @param {boolean} open Whether the panel should be visible.
     */
    function setMenu(open) {
        document.querySelector('.nav').classList.toggle('nav--open', open);
        burger.setAttribute('aria-expanded', String(open));
        burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    }

    burger.addEventListener('click', function () {
        setMenu(burger.getAttribute('aria-expanded') !== 'true');
    });

    document.addEventListener('keydown', function (event) {
        if (event.key === 'Escape' && burger.getAttribute('aria-expanded') === 'true') {
            setMenu(false);
            burger.focus();
        }
    });

    document.addEventListener('click', function (event) {
        if (burger.getAttribute('aria-expanded') !== 'true') { return; }
        if (!event.target.closest('.nav-right')) { setMenu(false); }
    });

    var params = new URLSearchParams(location.search);
    if (params.get('in')) { state.section = params.get('in'); }
    if (params.get('category')) { state.category = params.get('category'); }
    if (params.get('sort') === 'native') { state.sort = 'native'; }
    if (params.get('q')) {
        state.q = params.get('q').toLowerCase();
        $('q').value = params.get('q');
    }
    render();
}());
