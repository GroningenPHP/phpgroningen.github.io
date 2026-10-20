// Seasonal day/night hero theme, based on the time in Amsterdam.
// Preview with ?season=winter|spring|summer|autumn|sinterklaas|christmas|newyear
// and/or ?time=day|night
(function () {
    const hero = document.querySelector('.hero');
    if (!hero) {
        return;
    }

    // Holiday seasons reuse the colours of a regular season (data-season)
    // and add their own decorations (data-holiday)
    const holidayColours = { sinterklaas: 'autumn', christmas: 'winter', newyear: 'winter' };
    const seasons = ['winter', 'spring', 'summer', 'autumn', ...Object.keys(holidayColours)];

    // Approximate sunrise/sunset in Groningen per month (local clock time, hours)
    const daylight = [
        [8.75, 16.9], [8.0, 17.75], [7.0, 18.75], [6.9, 20.5], [5.9, 21.4], [5.3, 22.1],
        [5.6, 21.9], [6.4, 21.0], [7.3, 19.9], [8.1, 18.6], [8.1, 16.9], [8.8, 16.5]
    ];

    function amsterdamNow() {
        const parts = {};
        new Intl.DateTimeFormat('en-GB', {
            timeZone: 'Europe/Amsterdam',
            month: 'numeric',
            day: 'numeric',
            hour: 'numeric',
            minute: 'numeric',
            hourCycle: 'h23'
        }).formatToParts(new Date()).forEach(part => { parts[part.type] = Number(part.value); });
        return { month: parts.month - 1, day: parts.day, hour: parts.hour + parts.minute / 60 }; // month: 0 = January
    }

    function currentSeason(month, day) {
        const date = (month + 1) * 100 + day; // e.g. 1205 = 5 December, ranges are inclusive
        if (date >= 1228 || date <= 108) return 'newyear';
        if (date >= 1220) return 'christmas';
        if (date >= 1114 && date <= 1210) return 'sinterklaas';
        if (month <= 1 || month === 11) return 'winter';
        if (month <= 4) return 'spring';
        if (month <= 7) return 'summer';
        return 'autumn';
    }

    function currentTime(month, hour) {
        // Half an hour of twilight on both sides before switching to night
        const [sunrise, sunset] = daylight[month];
        return hour < sunrise - 0.5 || hour >= sunset + 0.5 ? 'night' : 'day';
    }

    const params = new URLSearchParams(window.location.search);
    const now = amsterdamNow();
    const requestedSeason = params.get('season');
    const requestedTime = params.get('time');
    const theme = seasons.includes(requestedSeason) ? requestedSeason : currentSeason(now.month, now.day);
    const holiday = holidayColours[theme] ? theme : null;
    const season = holiday ? holidayColours[holiday] : theme;
    const time = ['day', 'night'].includes(requestedTime) ? requestedTime : currentTime(now.month, now.hour);
    hero.dataset.season = season;
    hero.dataset.time = time;
    if (holiday) {
        hero.dataset.holiday = holiday;
    }

    const random = (min, max) => min + Math.random() * (max - min);
    const content = hero.querySelector('.hero-content');
    const addLayer = (className, html) => {
        const layer = document.createElement('div');
        layer.className = className;
        layer.setAttribute('aria-hidden', 'true');
        if (html) {
            layer.innerHTML = html;
        }
        hero.insertBefore(layer, content);
        return layer;
    };

    // Christmas: a string of fairy lights hanging in scallops across the top
    if (holiday === 'christmas') {
        const scallops = window.innerWidth < 768 ? 2 : 4;
        const perScallop = 9;
        let wire = '';
        let bulbs = '';
        for (let i = 0; i < scallops; i++) {
            const x = (i * 100) / scallops;
            const w = 100 / scallops;
            wire += `M${x} 2 Q${x + w / 2} 50 ${x + w} 2 `;
            for (let j = 1; j < perScallop; j++) {
                const t = j / perScallop;
                // Point on the quadratic curve in the 0-60 box
                const y = 2 + 96 * t * (1 - t);
                bulbs += `<span style="left:${(x + w * t).toFixed(2)}%;top:${(y / 60 * 100).toFixed(1)}%;--delay:${(-random(0, 3)).toFixed(1)}s"></span>`;
            }
        }
        addLayer('hero-garland',
            `<svg viewBox="0 0 100 60" preserveAspectRatio="none"><path d="${wire}"/></svg>${bulbs}`);
    }

    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        return;
    }

    // Sinterklaas: the pakjesboot (steamboat) sails along the canal
    if (holiday === 'sinterklaas') {
        addLayer('hero-steamboat', `<div class="hero-steamboat-boat"><svg viewBox="0 0 120 56">
            <path class="flag" d="M88 4v16M88 4l14 4-14 4z"/>
            <rect class="chimney" x="50" y="10" width="11" height="20"/>
            <rect class="chimney-top" x="49" y="8" width="13" height="5"/>
            <rect class="cabin" x="30" y="28" width="56" height="12" rx="2"/>
            <circle class="porthole" cx="40" cy="34" r="2.6"/>
            <circle class="porthole" cx="52" cy="34" r="2.6"/>
            <circle class="porthole" cx="64" cy="34" r="2.6"/>
            <circle class="porthole" cx="76" cy="34" r="2.6"/>
            <path class="hull" d="M4 40h112l-9 13H15z"/>
            <path class="stripe" d="M6 43h108l-1.4 2H7.6z"/>
        </svg><i></i><i></i><i></i></div>`)
            .firstChild.style.animationDelay = (-random(5, 50)).toFixed(0) + 's'; // already under way on load
    }

    // Christmas: Santa on his sleigh, led by two reindeer (Rudolph in front)
    if (holiday === 'christmas') {
        const reindeer = (x, y, nose) => `<g transform="translate(${x} ${y})">
                <path class="legs" d="M29 29l10 4M27 30l7 6M11 28L1 31M13 29l-9 6"/>
                <path class="deer" d="M6 24l-4-3 3 0zM30 24l7-12 4 1-6 13z"/>
                <ellipse class="deer" cx="19" cy="26" rx="14" ry="6"/>
                <ellipse class="deer" cx="42" cy="11" rx="5.5" ry="3" transform="rotate(-12 42 11)"/>
                <path class="antlers" d="M38 9l-3-7m1 3l-4-2m2-1l1-3M40 8l1-6m0 3l3-2"/>
                ${nose ? '<circle class="nose" cx="47.3" cy="10.2" r="1.8"/>' : ''}
            </g>`;
        addLayer('hero-sleigh', `<div class="hero-sleigh-ride"><svg viewBox="0 0 196 50">
            <path class="reins" d="M53 23Q90 18 120 24M120 24Q150 18 172 20"/>
            ${reindeer(86, 4, false)}
            ${reindeer(138, 0, true)}
            <ellipse class="sack" cx="22" cy="23" rx="9" ry="9"/>
            <path class="santa" d="M35 31q2-14 10-14 7 1 7 13z"/>
            <circle class="face" cx="46" cy="13" r="4"/>
            <path class="white" d="M42 14q4 9 8 0z"/>
            <path class="santa" d="M42 11q3-8 10-4l-2 4z"/>
            <circle class="white" cx="52.5" cy="7" r="1.8"/>
            <path class="sleigh" d="M14 40l-2-14q0-4 6-2l12 6h28l6-8q4-2 4 4l-2 14z"/>
            <path class="runner" d="M18 40v4M60 40v4M6 44h64q8 0 8-6"/>
        </svg></div>`)
            .firstChild.style.setProperty('--delay', random(1, 4).toFixed(1) + 's');
    }

    // New Year: fireworks bursting left and right of the text
    if (holiday === 'newyear') {
        const fireworks = addLayer('hero-fireworks');
        const bursts = time === 'night' ? 6 : 3;
        const sparks = 16;
        const place = (burst) => {
            const left = Math.random() < 0.5;
            const x = left ? random(4, 28) : random(72, 96);
            burst.style.setProperty('--x', x.toFixed(1) + '%');
            burst.style.setProperty('--y', random(10, 42).toFixed(1) + '%');
            burst.style.setProperty('--hue', Math.floor(random(0, 360)));
            burst.style.setProperty('--radius', random(45, 85).toFixed(0) + 'px');
        };
        for (let i = 0; i < bursts; i++) {
            const burst = document.createElement('div');
            burst.className = 'hero-firework';
            burst.style.setProperty('--delay', (i * 1.1 + random(0, 0.8)).toFixed(2) + 's');
            burst.style.setProperty('--duration', random(2.6, 3.6).toFixed(2) + 's');
            for (let j = 0; j < sparks; j++) {
                const spark = document.createElement('span');
                spark.style.setProperty('--angle', ((360 / sparks) * j).toFixed(0) + 'deg');
                burst.appendChild(spark);
            }
            place(burst);
            // Move to a new spot with a new colour every time it goes off
            burst.firstChild.addEventListener('animationiteration', () => place(burst));
            fireworks.appendChild(burst);
        }
    }

    const particleType = holiday === 'newyear'
        ? (time === 'night' ? null : 'confetti')
        : holiday === 'christmas' ? 'winter'
            : holiday === 'sinterklaas' ? 'pepernoten'
                : season === 'summer' && time === 'night' ? 'fireflies' : season;
    if (!particleType) {
        return;
    }

    const config = {
        autumn: { count: 18, size: [14, 24], duration: [10, 18], drift: 60, spin: 540 },
        winter: { count: 50, size: [3, 7], duration: [8, 16], drift: 30, spin: 0 },
        spring: { count: 22, size: [8, 13], duration: [10, 17], drift: 50, spin: 360 },
        summer: { count: 4, size: [18, 30], duration: [22, 34], drift: 25, spin: 0 },
        fireflies: { count: 14, size: [3, 5], duration: [4, 8], drift: 30, spin: 0, y: [45, 85] },
        pepernoten: { count: 18, size: [8, 13], duration: [9, 15], drift: 40, spin: 360 },
        confetti: { count: 40, size: [6, 10], duration: [7, 12], drift: 50, spin: 720 }
    }[particleType];
    const yRange = config.y || [5, 35];

    const container = document.createElement('div');
    container.className = 'hero-particles';
    container.setAttribute('aria-hidden', 'true');

    for (let i = 0; i < config.count; i++) {
        const particle = document.createElement('span');
        const duration = random(config.duration[0], config.duration[1]);
        particle.className = 'hero-particle';
        particle.style.setProperty('--x', random(0, 100).toFixed(1) + '%');
        particle.style.setProperty('--y', random(yRange[0], yRange[1]).toFixed(1) + '%');
        particle.style.setProperty('--size', random(config.size[0], config.size[1]).toFixed(1) + 'px');
        particle.style.setProperty('--duration', duration.toFixed(1) + 's');
        // Negative delay so the sky is already populated on page load
        particle.style.setProperty('--delay', (-random(0, duration)).toFixed(1) + 's');
        particle.style.setProperty('--drift', random(-config.drift, config.drift).toFixed(0) + 'px');
        particle.style.setProperty('--spin', (random(-1, 1) * config.spin).toFixed(0) + 'deg');
        container.appendChild(particle);
    }

    hero.insertBefore(container, hero.querySelector('.hero-content'));
})();
