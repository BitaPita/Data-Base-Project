document.addEventListener('DOMContentLoaded', function() {
    const gallery = document.querySelector('.image-gallery');
    const hammer = new Hammer(gallery);

    let startX = 0;
    let scrollLeft = 0;

    hammer.on('panstart', (ev) => {
        startX = ev.center.x;
        scrollLeft = gallery.scrollLeft;
    });

    hammer.on('panmove', (ev) => {
        const deltaX = ev.center.x - startX;
        gallery.scrollLeft = scrollLeft - deltaX;
    });

    hammer.on('panend', (ev) => {
        //Optional: Add inertia and snapping to nearest image
    });
});
