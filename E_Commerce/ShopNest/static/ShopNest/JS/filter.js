

function filterArtikel(kategorie){
    const container = document.getElementById('artikelContainer');
    const artikel = document.getElementsByClassName('artikel');

    for (let i = 0; i < artikel.length; i++) {
        artikel[i].style.display = 'none';
    }

    if (kategorie === 'alle') {
        for (let i = 0; i < artikel.length; i++) {
            artikel[i].style.display = 'block';
        }
    } else {
        let ausgewaehlteArtikel = document.getElementsByClassName(kategorie);
        for (let i = 0; i < ausgewaehlteArtikel.length; i++) {
            ausgewaehlteArtikel[i].style.display = 'block';
        }
    }


};