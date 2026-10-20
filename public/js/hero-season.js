// Seasonal hero theme. Preview a season with ?season=winter|spring|summer|autumn
(function () {
    const hero = document.querySelector('.hero');
    if (!hero) {
        return;
    }

    const seasons = ['winter', 'spring', 'summer', 'autumn'];

    function currentSeason(date) {
        const month = date.getMonth(); // 0 = January
        if (month <= 1 || month === 11) return 'winter';
        if (month <= 4) return 'spring';
        if (month <= 7) return 'summer';
        return 'autumn';
    }

    const requested = new URLSearchParams(window.location.search).get('season');
    const season = seasons.includes(requested) ? requested : currentSeason(new Date());
    hero.dataset.season = season;

    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        return;
    }

    const config = {
        autumn: { count: 18, size: [14, 24], duration: [10, 18], drift: 60, spin: 540 },
        winter: { count: 50, size: [3, 7], duration: [8, 16], drift: 30, spin: 0 },
        spring: { count: 22, size: [8, 13], duration: [10, 17], drift: 50, spin: 360 },
        summer: { count: 4, size: [18, 30], duration: [22, 34], drift: 25, spin: 0 }
    }[season];

    const random = (min, max) => min + Math.random() * (max - min);
    const container = document.createElement('div');
    container.className = 'hero-particles';
    container.setAttribute('aria-hidden', 'true');

    for (let i = 0; i < config.count; i++) {
        const particle = document.createElement('span');
        const duration = random(config.duration[0], config.duration[1]);
        particle.className = 'hero-particle';
        particle.style.setProperty('--x', random(0, 100).toFixed(1) + '%');
        particle.style.setProperty('--y', random(5, 35).toFixed(1) + '%');
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
