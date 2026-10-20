// Seasonal day/night hero theme, based on the time in Amsterdam.
// Preview with ?season=winter|spring|summer|autumn and/or ?time=day|night
(function () {
    const hero = document.querySelector('.hero');
    if (!hero) {
        return;
    }

    const seasons = ['winter', 'spring', 'summer', 'autumn'];

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
            hour: 'numeric',
            minute: 'numeric',
            hourCycle: 'h23'
        }).formatToParts(new Date()).forEach(part => { parts[part.type] = Number(part.value); });
        return { month: parts.month - 1, hour: parts.hour + parts.minute / 60 }; // month: 0 = January
    }

    function currentSeason(month) {
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
    const season = seasons.includes(requestedSeason) ? requestedSeason : currentSeason(now.month);
    const time = ['day', 'night'].includes(requestedTime) ? requestedTime : currentTime(now.month, now.hour);
    hero.dataset.season = season;
    hero.dataset.time = time;

    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        return;
    }

    const config = {
        autumn: { count: 18, size: [14, 24], duration: [10, 18], drift: 60, spin: 540 },
        winter: { count: 50, size: [3, 7], duration: [8, 16], drift: 30, spin: 0 },
        spring: { count: 22, size: [8, 13], duration: [10, 17], drift: 50, spin: 360 },
        summer: { count: 4, size: [18, 30], duration: [22, 34], drift: 25, spin: 0 },
        fireflies: { count: 14, size: [3, 5], duration: [4, 8], drift: 30, spin: 0, y: [45, 85] }
    }[season === 'summer' && time === 'night' ? 'fireflies' : season];
    const yRange = config.y || [5, 35];

    const random = (min, max) => min + Math.random() * (max - min);
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
